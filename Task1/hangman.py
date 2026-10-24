import random
word_file = "google-l0000-english-no-swears.txt"
# Display the Hangman drawing based on wrong guesses
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

# Load the word list from the text file
def data_in_word_file():
    data = []
    try:
        with open(word_file, "r") as f:
            data= f.read().splitlines()
    except FileNotFoundError:
        print("\ngoogle-l0000-english-no-swears.txt file does not exist\n")
        return False
    
    return data

# main function
def main():
    word_list = data_in_word_file()
    # execute remian code when file is found
    if word_list:
        # Randomly select a word from the word list
        random_word = random.choice(word_list)

        wrong_guesses = 0
        # Initialize the wrong guess counter and maximum attempts
        max_tries = 6

        # Store letters that the player has already guessed
        guessed = set()

        print("\n====== Welcome to Hangman! ======")
        print("-"*33)

        # Continue the game until the player runs out of attempts
        while max_tries > wrong_guesses:

            output = ""
            for i in random_word:
                if i in guessed:
                    output += i + " "
                else:
                    output += "_ "
            # Display the current Hangman stage
            hangman(wrong_guesses)

            print(f"Word: {output}")
            # Check whether the player has guessed the entire word
            if "_" not in output:
                print("\nCongratulations! You won!")
                print(f"The word was: {random_word}")
                break
            print("\nPlease enter a single letter!\n")

            guess = input("Guess a letter: ").strip().lower()

            # Validate the input to allow only one alphabetic character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue

            if guess in guessed:
                print("You already guessed that letter.")
                continue

            guessed.add(guess)

            # Check whether the guessed letter is present in the word
            if guess in random_word:
                print("\nCorrect guess!")
            else:
                wrong_guesses+=1
                print("\nWrong guess")

        else:
            hangman(wrong_guesses)
            print("\nGame over")
            print(f"The word was: {random_word}\n")
        
# Run the game when this file is executed directly
if __name__== "__main__":
    main()