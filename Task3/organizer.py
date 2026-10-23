# Import modules for file operations, logging, and path management
import os
import shutil
import logging
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger("file_organizer")

# Define file extensions and their corresponding categories
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp",
        ".svg", ".bmp", ".ico", ".tiff", ".tif"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".m4v", ".3gp"
    ],
    "Music": [
        ".mp3", ".wav", ".flac", ".aac",
        ".ogg", ".m4a", ".wma", ".opus"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2", ".xz", ".tar.gz"
    ],
    "Code": [
        ".py", ".js", ".html", ".css", ".java",
        ".c", ".cpp", ".h", ".hpp", ".php",
        ".sql", ".json", ".xml", ".yaml", ".yml",
        ".ts", ".tsx", ".jsx"
    ],
    "Applications": [
        ".exe", ".msi", ".appx", ".apk", ".deb", ".rpm"
    ]
}
# Classify files based on their extensions
class FileClassifier:
    def __init__(self, file_types):
        self.file_types = {
            category: tuple(
                sorted(
                    (ext.lower() for ext in extensions),
                    key=len,
                    reverse=True
                )
            )
            for category, extensions in file_types.items()
        }

    def classify(self, filename):
        filename = filename.lower()

        for category, extensions in self.file_types.items():
            if filename.endswith(extensions):
                return category

        return "Others"

# Scan the selected folder and find files to organize
def scan_files(folder):
    try:
        with os.scandir(folder) as entries:
            for entry in entries:
                try:
                    if entry.is_file(follow_symlinks=False):
                        yield Path(entry.path)
                except OSError as exc:
                    logger.error(
                        "Could not inspect %s: %s",
                        entry.name, exc
                    )
    except OSError as exc:
        logger.error("Could not scan folder %s: %s", folder, exc)

# Generate unique destination paths to prevent filename conflicts
def unique_destination(destination, reserved=None):
    reserved = reserved if reserved is not None else set()
    candidate = destination
    counter = 1

    while candidate.exists() or candidate in reserved:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        counter += 1

    reserved.add(candidate)
    return candidate

# Create an organization plan without moving any files
def plan_organization(folder, classifier):
    reserved = set()
    plan = []

    for source in scan_files(folder):
        if source.name == "organizer.log":
            continue

        category = classifier.classify(source.name)
        destination = folder / category / source.name

        destination = unique_destination(destination, reserved)

        plan.append({
            "source": source,
            "destination": destination,
            "category": category
        })

    return plan
# Organize files into categories and record successful moves
class FileOrganizer:
    def __init__(self, source_folder, classifier):
        self.source_folder = Path(source_folder)
        self.classifier = classifier
        self.history = []

    def organize(self):
        plan = plan_organization(
            self.source_folder, self.classifier
        )

        for item in plan:
            source = item["source"]
            destination = item["destination"]

            try:
                # Recheck before creating the folder or moving.
                if not source.is_file():
                    logger.warning("Skipped missing file: %s", source)
                    continue

                destination.parent.mkdir(
                    parents=True, exist_ok=True
                )

                # Do not overwrite a file that appeared meanwhile.
                if destination.exists():
                    destination = unique_destination(destination)

                shutil.move(str(source), str(destination))

                # Record only successful moves.
                self.history.append({
                    "source": source,
                    "destination": destination
                })

                logger.info(
                    "[SUCCESS] %s -> %s/",
                    source.name, destination.parent.name
                )

            except (OSError, shutil.Error) as exc:
                logger.error(
                    "[FAILED] %s: %s", source.name, exc
                )

        return self.history
    
# Preview file organization without moving any files
class FileOrganizerDryRun:
    def __init__(self, source_folder, classifier):
        self.source_folder = Path(source_folder)
        self.classifier = classifier

    def organize_dryrun(self):
        return plan_organization(
            self.source_folder, self.classifier
        )

# Restore files to their original locations
class FileUndo:
    def undo(self, history):
        restored = 0
        failed = 0

        for item in reversed(history):
            source = item["source"]
            destination = item["destination"]

            try:
                if not destination.is_file():
                    logger.warning(
                        "Cannot restore missing file: %s",
                        destination
                    )
                    failed += 1
                    continue

                if source.exists():
                    logger.error(
                        "Restore conflict; original path exists: %s",
                        source
                    )
                    failed += 1
                    continue

                shutil.move(str(destination), str(source))
                restored += 1

                logger.info("[RESTORED] %s", source.name)

                folder = destination.parent
                try:
                    folder.rmdir()
                except OSError:
                    pass

            except (OSError, shutil.Error) as exc:
                logger.error(
                    "Undo failed for %s: %s", destination, exc
                )
                failed += 1

        return restored, failed

# Ask the user for a folder path and validate it
def get_folder():
    raw_path = input(
        "\nEnter folder path to organize:\n> "
    ).strip().strip('"')

    if not raw_path:
        print("Folder path cannot be empty.")
        return None

    folder = Path(raw_path).expanduser()

    try:
        if folder.is_dir():
            return folder.resolve()

        print("Invalid path or folder does not exist.")
        return None
    except OSError as exc:
        logger.error("Invalid folder: %s", exc)
        return None

# Display a short processing animation
def load_animation():
    print("Processing", end="", flush=True)

    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)

    print()

# Preview how files will be organized without making changes
def dryrun(file_types):
    folder = get_folder()
    if folder is None:
        return

    classifier = FileClassifier(file_types)
    preview = FileOrganizerDryRun(folder, classifier)

    print("\nDRY RUN — PREVIEW MODE")
    print("No files will be moved or modified.\n")

    # Generate the organization preview
    plan = preview.organize_dryrun()
    load_animation()

    for item in plan:
        source = item["source"]
        destination = item["destination"]

        print()
        print(
            f"[PREVIEW] {source.name} -> "
            f"{destination.parent.name}/{destination.name}"
        )

    print("\nPREVIEW SUMMARY")
    print(f"Files scanned      : {len(plan)}")
    print(f"Files to organize  : {len(plan)}")
    print("Files moved        : 0")
    print("\nPreview completed. No changes made.")

    input("\nPress Enter to return to menu...")

# Organize files in the user-selected folder
def organize_file(file_types):
    folder = get_folder()
    if folder is None:
        return None

    # Initialize the classifier and file organizer
    classifier = FileClassifier(file_types)
    organizer = FileOrganizer(folder, classifier)

    print("\nStarting file organization...")
    load_animation()

    # Execute the organization and collect the move history
    history = organizer.organize()

    categories = {
        item["destination"].parent
        for item in history
    }

    print("\nORGANIZATION SUMMARY")
    print(f"Files moved         : {len(history)}")
    print(f"Categories used     : {len(categories)}")
    print("Check log messages above for failed moves.")

    input("\nPress Enter to return to menu...")

    return history

# Display the main menu and available operations
def show_menu():
    print("\n" + "=" * 44)
    print("       SMART FILE ORGANIZER")
    print("       Datheon Internship - Task 3")
    print("=" * 44)
    print("1. Organize Files")
    print("2. Preview Changes (Dry Run)")
    print("3. Undo Last Organization")
    print("4. Exit")

# Display the main menu and available operations
def main():
    history = []
    undo = FileUndo()

    # Keep the application running until the user chooses to exit
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            result = organize_file(FILE_TYPES)
            if result:
                history = result

        elif choice == "2":
            dryrun(FILE_TYPES)

        elif choice == "3":
            if not history:
                print("\nNo organization history available.")
                input("Press Enter to continue...")
                continue

            print("\nUNDO LAST ORGANIZATION")
            restored, failed = undo.undo(history)

            print("\nUNDO SUMMARY")
            print(f"Files restored : {restored}")
            print(f"Files failed   : {failed}")

            history = [
                item for item in history
                if item["destination"].exists()
                and not item["source"].exists()
            ]

            input("\nPress Enter to return to menu...")

        elif choice == "4":
            print("\nThank you for using Smart File Organizer!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Run the application when this script is executed directly
if __name__ == "__main__":
    main()
