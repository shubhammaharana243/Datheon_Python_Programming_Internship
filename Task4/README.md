# 🤖 Datheon AI Assistant — Task 4

A simple, rule-based chatbot built with Python that answers frequently asked questions about the Datheon internship program. It uses a JSON file to store FAQ data and regular expressions to recognize user messages and provide relevant responses.

## 📌 Project Overview

The Datheon AI Assistant is a command-line chatbot designed to provide quick answers to common internship-related questions.

The chatbot loads its FAQ data from a JSON file, processes user input, identifies keywords using Python's `re` module, and displays the corresponding answers.

It also supports greetings, recognizes exit commands, and provides a fallback response when it cannot understand a question.

## ✨ Features

- **JSON-Based FAQ Storage:** Loads greetings and frequently asked questions from an external JSON file.
- **Greeting Detection:** Recognizes common greetings and responds with a welcome message.
- **FAQ Matching:** Identifies questions about internship hours, project submissions, and certificates.
- **Regular Expressions:** Uses Python's `re` module to match keywords in user messages.
- **Case-Insensitive Input:** Converts user messages to lowercase for easier matching.
- **Input Cleaning:** Uses `.strip()` to remove unnecessary whitespace.
- **Graceful Exit:** Allows users to leave the chatbot using `bye`, `exit`, or `quit`.
- **Fallback Responses:** Provides a default message when no matching keyword is found.
- **Interactive CLI:** Offers a simple command-line interface with a clean welcome banner.

## 🛠️ Technologies Used

- **Python 3** — Core programming language.
- **JSON** — Stores FAQ questions, answers, and greetings.
- **Regular Expressions (`re`)** — Detects keywords and matches user messages.

### Python Modules

| Module | Purpose |
|---|---|
| `json` | Loads FAQ data from the JSON file. |
| `re` | Searches user input for matching patterns. |

Both modules are included in Python's standard library, so no additional package installation is required.

## 📂 Project Structure

```text
Task4/
│
├── chatbot.py
├── sample_faq.json
└── README.md
```

> **Note:** Replace `chatbot.py` with your actual Python filename if it is different.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shubhammaharana243/Datheon_Python_Programming_Internship.git
```

### 2. Navigate to the Project Directory

```bash
cd Datheon_Python_Programming_Internship/Task4
```

### 3. Run the Chatbot

```bash
python chatbot.py
```

Make sure Python 3 is installed and `sample_faq.json` is available at the path specified in the Python script.

## 💬 Example Interaction

```text
========================================
       DATHEON AI ASSISTANT
========================================
  Ask me anything about your internship!

You: hello
Bot: Hello! Welcome to Datheon Support.

You: What are the internship working hours?
Bot: [Answer loaded from sample_faq.json]

You: How do I submit my project?
Bot: [Answer loaded from sample_faq.json]

You: When will I receive my certificate?
Bot: [Answer loaded from sample_faq.json]

You: bye
Bot: Goodbye! Have a great day!
```

> The FAQ responses shown above are illustrative placeholders. The actual answers depend on the contents of `sample_faq.json`.

## 🧠 Concepts Learned

While developing this project, I practised the following Python concepts:

- Functions and return statements.
- Reading external JSON files using `json.load()`.
- Lists and dictionaries.
- Loops and conditional statements.
- User input handling with `input()`.
- String methods such as `.lower()` and `.strip()`.
- Regular expressions using `re.search()` and `re.escape()`.
- Generator expressions.
- Keyword matching and basic rule-based chatbot logic.
- Exception-free program flow and graceful termination.


## 🎯 Project Objective

The objective of this project is to practise Python programming by building a simple, interactive chatbot that can answer predefined questions using JSON data and rule-based text matching.

## 👨‍💻 Author

**Shubham Maharana**

- GitHub: [@shubhammaharana243](https://github.com/shubhammaharana243)
- Internship: Datheon Python Programming Internship
- Task: Task 4 — AI Chatbot

---

⭐ If you find this project useful, feel free to explore the repository and its other Python projects.