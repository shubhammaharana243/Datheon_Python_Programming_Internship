# 🐍 Datheon Python Programming Internship

## 🚀 About the Internship

I'm excited to share my work from the **Datheon Python Programming Internship**. During this internship, I completed four Python-based projects that helped me improve my programming skills, problem-solving abilities, and understanding of practical Python applications.

Each task focused on different Python concepts, including game development, stock portfolio tracking, file automation, and chatbot development.

---

## 📌 Projects Overview

### 🎮 Task 1: Hangman Word Guessing Game

A command-line word-guessing game developed using Python.

**Features**
- Random word selection from a word list.
- Interactive letter guessing.
- ASCII Hangman graphics.
- Input validation.
- Detection of repeated guesses.
- Win and lose conditions.

**Technologies Used**
- Python
- `random` module

**What I Learned**
- Working with loops and conditional statements.
- Using sets to track guessed letters.
- Handling user input.
- Implementing game logic.

---

### 📈 Task 2: Stock Portfolio Performance Tracker

A Python application that tracks stock investments and calculates portfolio performance.

**Features**
- Accepts stock ticker symbols, purchase prices, and quantities.
- Validates ticker symbols against a CSV file containing company symbols.
- Fetches stock prices using `yfinance`.
- Calculates invested capital and current market value.
- Calculates profit or loss.
- Exports portfolio results to a CSV file.

**Technologies Used**
- Python
- `csv` module
- `yfinance` library

**Output**
- `portfolio_summary.csv`

**What I Learned**
- Reading and writing CSV files.
- Working with external Python libraries.
- Retrieving stock price information.
- Performing financial calculations.
- Handling invalid inputs and exceptions.

---

### 📂 Task 3: Smart File Organizer

A Python utility that organizes files into categories based on their extensions.

**Features**
- Automatically categorizes files into folders.
- Supports multiple file types, including images, documents, videos, music, archives, code, and applications.
- Handles duplicate filenames to prevent overwriting.
- Provides a dry-run mode to preview changes.
- Maintains a history of successful file movements.
- Supports undo functionality.
- Uses logging to record relevant events.

**Technologies Used**
- Python
- `os` module
- `shutil` module
- `logging` module
- `time` module
- `pathlib` module

**What I Learned**
- File and directory management.
- Working with file paths.
- Automating repetitive tasks.
- Handling filename conflicts.
- Implementing undo functionality.
- Using logging and exception handling.

---

### 🤖 Task 4: Datheon AI Assistant Chatbot

A simple FAQ-based chatbot that responds to questions about the internship using predefined data stored in a JSON file.

**Features**
- Loads FAQ information from a JSON file.
- Recognizes greeting messages.
- Responds to questions about internship working hours.
- Answers questions about projects and submissions.
- Provides certificate-related information.
- Recognizes exit commands such as `bye`, `exit`, and `quit`.
- Uses a fallback response when a question is not recognized.

**Technologies Used**
- Python
- `json` module
- `re` module (Regular Expressions)

**What I Learned**
- Reading structured data from JSON files.
- Using regular expressions for keyword matching.
- Processing and normalizing user input.
- Building a simple rule-based chatbot.
- Organizing FAQ data separately from application logic.

---

## 🛠️ Technologies and Concepts

| Technology | Application |
|---|---|
| Python | Core programming language |
| `random` | Random word selection in the Hangman game |
| `csv` | Reading stock symbols and exporting portfolio results |
| `yfinance` | Retrieving stock market information |
| `os` and `pathlib` | File and directory management |
| `shutil` | Moving and restoring files |
| `logging` | Recording application events |
| `json` | Loading chatbot FAQ data |
| `re` | Pattern matching and keyword recognition |
| Git and GitHub | Version control and project hosting |

---

## 📁 Repository Structure

```text
Datheon_Python_Programming_Internship/
│
├── Task1/
│   └── Hangman game files
│
├── Task2/
│   ├── portfolio.py
│   └── constituents.csv
│
├── Task3/
│   └── Smart File Organizer files
│
├── Task4/
│   ├── chatbot.py
│   └── sample_faq.json
│
├── portfolio_summary.csv
└── README.md
```

*Note: The exact filenames and locations may vary depending on the files included in the repository.*

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shubhammaharana243/Datheon_Python_Programming_Internship.git
```

### 2. Navigate to the Project Folder

```bash
cd Datheon_Python_Programming_Internship
```

### 3. Install the Required Dependency

Task 2 uses the `yfinance` library.

```bash
pip install yfinance
```

The other tasks primarily use Python's standard library.

### 4. Run a Task

Navigate to the appropriate task folder and run its Python script.

For example:

```bash
python Task1/hangman.py
```

```bash
python Task2/portfolio.py
```

For Tasks 3 and 4, use the actual Python filenames in their respective folders.

**Important:** Keep the required data files in the locations expected by the scripts. Task 2 requires its stock-symbol CSV file, and Task 4 requires `Task4/sample_faq.json`.

---

## 📚 Key Learnings

Throughout these four projects, I strengthened my understanding of:

- Python fundamentals and problem-solving.
- Functions, loops, conditions, and data structures.
- File handling and automation.
- CSV and JSON data processing.
- Regular expressions using the `re` module.
- Working with external libraries.
- Input validation and exception handling.
- Modular programming and code organization.
- Version control using Git and GitHub.

---

## 🙏 Acknowledgment

A **big thank you to Datheon** for providing me with this Python Programming Internship opportunity.

Working on these projects helped me apply my Python knowledge in practical scenarios and gain more confidence in developing useful applications.

I'm grateful for this learning experience and look forward to improving my skills, building more projects, and continuing my journey as a developer. 🚀

---

## 🔗 Connect and Explore

**GitHub Repository:**  
[Datheon Python Programming Internship](https://github.com/shubhammaharana243/Datheon_Python_Programming_Internship)

**LinkedIn:**  
Add links to your individual Task 1, Task 2, Task 3, and Task 4 LinkedIn posts here.

---

## 🏷️ Tags

`Python` `PythonProgramming` `Internship` `Datheon` `GitHub` `FileHandling` `Automation` `RegularExpressions` `JSON` `CSV` `ProjectBasedLearning`