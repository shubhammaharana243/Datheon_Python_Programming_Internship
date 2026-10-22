# 📂 Smart File Organizer & Cleanup Utility

A Python-based file organization tool that automatically organizes files into category-wise folders based on their file extensions. Built as **Task 3** of the Datheon Python Programming Internship.

## 🚀 Overview

The Smart File Organizer helps keep directories clean and organized by automatically sorting files into appropriate folders such as Images, Documents, Videos, Music, Archives, Code, Applications, and Others.

It also provides a Dry Run preview mode, duplicate filename handling, an Undo feature, and logging for successful operations and errors.

## ✨ Features

- **Automatic File Organization:** Sorts files into folders according to their file extensions.
- **Dynamic Folder Creation:** Creates category folders automatically when required.
- **Dry Run Mode:** Previews planned file movements without moving files or creating folders.
- **Duplicate Filename Handling:** Generates unique filenames to avoid overwriting existing files.
- **Undo Last Organization:** Restores successfully moved files to their original locations during the current session, where restoration is safe.
- **Error Handling:** Handles file access and movement errors with informative messages.
- **Execution Logging:** Reports successful movements and failed operations.
- **Organization Summary:** Displays the number of files moved and categories used.
- **Command-Line Interface:** Simple interactive menu for easy operation.

## 🗂️ Supported File Categories

| Category | Example Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg` |
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.csv`, `.pptx` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm` |
| Music | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Code | `.py`, `.js`, `.html`, `.css`, `.java`, `.sql` |
| Applications | `.exe`, `.msi`, `.apk`, `.deb`, `.rpm` |
| Others | Files with unrecognized extensions |

## 🛠️ Technologies Used

- **Python 3**
- `os` — Directory scanning with `os.scandir()`
- `pathlib` — Path handling and file information
- `shutil` — Moving and restoring files
- `logging` — Operation and error messages
- `time` — Simple processing animation

All listed modules are part of Python's standard library; no external packages are required.

## 📥 Installation

**1. Clone the repository**

```bash
git clone https://github.com/shubhammaharana243/python-file-organizer.git
```

**2. Navigate to the project directory**

```bash
cd python-file-organizer
```

**3. Run the organizer**

If your main script is named `organizer.py`:

```bash
python organizer.py
```

On Windows, you can also use:

```bash
py organizer.py
```

## ▶️ Usage

After running the program, the interactive menu provides the following options:

```text
============================================
       SMART FILE ORGANIZER
       Datheon Internship - Task 3
============================================
1. Organize Files
2. Preview Changes (Dry Run)
3. Undo Last Organization
4. Exit

Enter your choice (1-4):
```

### 1. Organize Files

Select option `1` and enter the directory path you want to organize.

Example:

```text
Enter folder path to organize:
> C:\Users\YourName\Downloads
```

The program scans the directory, identifies file types, creates category folders as needed, and moves files to their appropriate destinations.

### 2. Preview Changes (Dry Run)

Select option `2` to preview the planned organization.

Example:

```text
DRY RUN — PREVIEW MODE
No files will be moved or modified.

[PREVIEW] photo.jpg -> Images/photo.jpg
[PREVIEW] report.pdf -> Documents/report.pdf
[PREVIEW] main.py -> Code/main.py

PREVIEW SUMMARY
Files scanned      : 3
Files to organize  : 3
Files moved        : 0

Preview completed. No changes made.
```

The displayed filenames and counts are examples; actual results depend on the selected directory.

### 3. Undo Last Organization

Select option `3` to restore files moved during the current program session.

The program checks for conflicts at the original locations and avoids overwriting existing files.

### 4. Exit

Select option `4` to close the application.

## 📁 Example Directory Structure

**Before organization**

```text
Downloads/
├── photo.jpg
├── report.pdf
├── main.py
├── video.mp4
└── archive.zip
```

**After organization**

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Code/
│   └── main.py
├── Videos/
│   └── video.mp4
└── Archives/
    └── archive.zip
```

## 🛡️ Safety and Limitations

- Test the program on a sample directory before using it on important files.
- Dry Run previews planned changes but does not guarantee that subsequent moves will succeed.
- Existing filenames are handled by generating unique destination names.
- Undo history is maintained in memory and is not preserved after the program exits.
- Files that cannot be accessed or moved may be skipped or reported as failures.
- The program organizes files in the selected directory's top level; it does not recursively organize nested folders.

## 🎯 Internship Objective

This project demonstrates practical Python programming skills, including directory traversal, file classification, file operations, exception handling, logging, and command-line application development.

**Internship:** Datheon Python Programming Internship  
**Task:** Task 3 — Automated File Organizer & Cleanup Utility  
**Developer:** [Shubham Maharana](https://github.com/shubhammaharana243)

## 📜 License

This project is intended for educational and portfolio purposes.
