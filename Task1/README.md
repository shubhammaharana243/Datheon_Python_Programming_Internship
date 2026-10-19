# 🎮 Hangman Word Guessing Game

A simple, interactive, console-based **Hangman game built with Python** as part of the Datheon Python Programming Internship.

The game randomly selects a secret word from different categories, and the player must guess the word one letter at a time before running out of attempts. Visual ASCII gallows art updates with each incorrect guess.

## ✨ Features

- 🎲 **Random Word Selection** — Randomly selects a word from predefined word lists.
- 🗂️ **Multiple Categories** — Includes Animals, Space, Fruits, Body Parts, Food, Programming, Sports, and Technology.
- 💡 **Category Hint** — Displays the category of the secret word to help the player.
- 🎨 **ASCII Hangman Art** — Visual gallows art updates with each incorrect guess.
- 🔤 **Letter-by-Letter Guessing** — Guess the secret word one letter at a time.
- 🔁 **Duplicate Guess Detection** — Prevents repeated guesses from counting as incorrect attempts.
- ✅ **Input Validation** — Accepts only a single alphabetic character per guess.
- 🏆 **Win and Lose Conditions** — Displays the result and reveals the secret word when the game ends.

## 🛠️ Technologies Used

- Python 3
- `random` module

## 📋 Requirements

- Python 3.x installed on your computer.
- A terminal or command prompt.

No external Python packages are required.

## 🚀 How to Run

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project folder**

```bash
cd <your-project-folder>
```

**3. Run the game**

```bash
python hangman.py
```

On some systems, you may need to use:

```bash
python3 hangman.py
```

## 🎯 How to Play

1. Run the Python file to start the game.
2. Read the category hint displayed on the screen.
3. Enter one letter to guess the secret word.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses update the ASCII Hangman drawing.
6. Avoid making more than six incorrect guesses.
7. Guess the complete word to win!

**Note:** Repeating a previously guessed letter does not count as an incorrect guess.

## 🖥️ Example Gameplay

```text
====== Welcome to Hangman! ======

Hint: The word belongs to this category: ANIMAL

Word: _ _ _ _ _
Guess a letter: T

Correct guess!

Word: T _ _ _ _

Guess a letter: Z

Wrong guess
```

*The actual output depends on the randomly selected category and word.*

## 📂 Project Structure

```text
Datheon_Python_Programming_Internship/
│
├── Task1/
│   ├── hangman.py
│   └── README.md
```

## 📚 What I Learned

Through this project, I practiced:

- Python functions and modular programming.
- Lists and dictionaries.
- Random selection using the `random` module.
- Loops and conditional statements.
- String manipulation and input validation.
- Tracking guessed letters.
- Implementing game logic and win/lose conditions.
- Displaying ASCII art in the terminal.

## 🎓 Internship Task

This project was developed as part of **Task 1: Hangman Word Guessing Game (Console)** for the Datheon Python Programming Internship.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [shubhammaharana243](https://github.com/shubhammaharana243)

---

⭐ If you find this project interesting, feel free to explore the code and share your feedback!
