import random

def hangman(value):
    hangman_art=[
'''
     +---+
         |
         |
         |
         |
    ========
''',
'''
     +---+
     |   |
         |
         |
         |
    ========
''',
'''
     +---+
     |   |
     O   |
         |
         |
    ========
''',
'''
     +---+
     |   |
     O   |
     |   |
         |
    ========
''',
'''
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
''',
'''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
''',
'''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
''',
    ]

    print(hangman_art[value])

def data_in_word_file():
    data = []
    with open("Task1/google-10000-english-no-swears.txt", "r") as f:
        data= f.read().splitlines()

    return data

def main():
    random_word = random.choice(data_in_word_file())

    wrong_guesses = 0
    max_tries = 6

    guessed = set()

    print("\n====== Welcome to Hangman! ======")
    print("-"*33)


    while max_tries > wrong_guesses:

        output = ""
        for i in random_word:
            if i in guessed:
                output += i + " "
            else:
                output += "_ "

        hangman(wrong_guesses)

        print(f"Word: {output}")

        if "_" not in output:
            print("\nCongratulations! You won!")
            print(f"The word was: {random_word}")
            break
        print("\nPlease enter a single letter!\n")

        guess = input("Guess a latter: ").strip().lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("You already guessed that letter.")
            continue

        if guess in guessed:
            print("You already guessed that latter.")
            continue

        guessed.add(guess)

        if guess in random_word:
            print("\nCorrect guess!")
        else:
            wrong_guesses+=1
            print("\nWrong guess")

    else:
        hangman(wrong_guesses)
        print("\nGame over")
        print(f"The word was: {random_word}\n")


if __name__== "__main__":
    main()