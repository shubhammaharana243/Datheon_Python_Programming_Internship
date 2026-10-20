# 🎮 Hangman Word Guessing Game

A console-based **Hangman Word Guessing Game built with Python** as part of the Datheon Python Programming Internship.

The game randomly selects a secret word from an English word list. Players guess the hidden word one letter at a time while trying to avoid six incorrect guesses.

## ✨ Features

- 🎲 **Random Word Selection** — Selects a secret word randomly from an English word list.
- 📚 **English Word List** — Uses `google-10000-english-no-swears.txt` as the word-list resource.
- 💡 **Category Hints** — Displays a category hint to help the player.
- 🎨 **ASCII Hangman Art** — Updates the gallows drawing with each incorrect guess.
- 🔤 **Letter-by-Letter Guessing** — Reveals correctly guessed letters in the secret word.
- 🔁 **Duplicate Guess Detection** — Prevents repeated guesses from counting as incorrect attempts.
- ✅ **Input Validation** — Accepts only a single alphabetic character per guess.
- 🏆 **Win and Lose Conditions** — Displays the game result and reveals the secret word when the game ends.

## 🛠️ Technologies Used

- Python 3
- `random` module
- Python standard library

## 📋 Requirements

- Python 3.x
- A terminal or command prompt

No external Python packages are required.

## 📂 Project Structure

```text
Datheon_Python_Programming_Internship/
│
└── Task1/
    ├── hangman.py
    ├── google-10000-english-no-swears.txt
    └── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shubhammaharana243/Datheon_Python_Programming_Internship.git
```

### 2. Navigate to Task1

```bash
cd Datheon_Python_Programming_Internship/Task1
```

### 3. Run the game

```bash
python hangman.py
```

On some systems, use `python3 hangman.py` instead.

**Note:** Keep the English word-list file in the location expected by your Python code.

## 🎯 How to Play

1. Start the game from your terminal.
2. Read the category hint displayed on the screen.
3. Enter one letter to guess the secret word.
4. Correct guesses reveal matching letters.
5. Incorrect guesses update the ASCII Hangman drawing.
6. Avoid making more than six incorrect guesses.
7. Guess the complete word to win!

Repeated guesses do not count as incorrect attempts.

## 🖥️ Example Gameplay

```text
====== Welcome to Hangman! ======

Hint: The word belongs to this category: ANIMAL

Word: _ _ _ _ _
Guess a letter: T

Correct guess!

Guess a letter: Z

Wrong guess
```

*The actual output depends on the randomly selected word.*

## 📚 What I Learned

- Python functions and modular programming
- Lists, dictionaries, and sets
- Random word selection
- Loops and conditional statements
- String manipulation and input validation
- Tracking guessed letters
- File handling and working with text files
- Implementing game logic and ASCII art

## 🎓 Internship Task

Developed as **Task 1: Hangman Word Guessing Game (Console)** for the Datheon Python Programming Internship.

## 👨‍💻 Author

**Shubham Maharana**

GitHub: [shubhammaharana243](https://github.com/shubhammaharana243)

---

⭐ Feedback and suggestions are welcome!
