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
def random_cate_word():
    word_dict = {
        "ANIMAL":["CAT", "DOG", "HORSE", "LION", "TIGER", "ELEPHANT", "GIRAFFE", "ZEBRA","BEAR", "DONKEY", "MONKEY", "KANGAROO", "DOLPHIN"],

        "SPACE": ["MOON", "STAR", "SUN", "ROCKET", "ALIEN", "SPACE", "ASTRONOMY", "SUPERNOVA", "GRAVITY", "NEBULA"],

        "FRUIT":["APPLE", "BANANA", "MANGO", "GUAVA", "GRAPES", "PINEAPPLE", "PAPAYA", "WATERMELON"],

        "BODY PART": ["HAND", "FOOT", "HEAD", "NOSE", "EYES", "HAIR", "NECK", "LIVER", "KIDNEY", "SKELETON", "BONE", "FACE", "EARS", "MOUTH"],

        "FOOD": ["BURGER", "PIZZA", "SUSHI", "SANDWICH", "CHOCOLATE", "PASTA", "TACOS", "BIRYANI", "SAMOSA", "DOSA"],

        "PROGRAMMING": ["CODE", "LOOP", "BUG", "DATA", "FILE", "VARIABLE", "STRING", "ARRAY", "CLASS", "OBJECT", "INPUT", "OUTPUT", "DICTIONARY", "INHERITANCE", "COMPILER", "POLYMORPHISM", "ENCAPSULATION"],

        "SPORTS": ["FOOTBALL", "CRICKET", "HOCKEY", "TENNIS", "BOXING", "CHESS", "GOLF", "BADMINTON", "MARATHON", "BALL", "REFEREE", "BAT"],

        "TECHNOLOGY": ["ALGORITHM", "CYBERSECURITY", "BLOCKCHAIN", "SATELLITE", "AI", "PROCESSOR", "MICROCHIP", "RAM"],
    }

    categories= list(word_dict.keys())

    ran_category = random.choice(categories)
    ran_word = random.choice(word_dict[ran_category])

    return [ran_category, ran_word]

def main():
    random_pair = random_cate_word()

    random_category= random_pair[ 0]
    random_word = random_pair[1]

    wrong_guesses = 0
    max_tries = 6

    guessed = []

    print("\n====== Welcome to Hangman! ======")
    print("-"*33)
    print(f"\nHint: The word belongs to this category: {random_category}")


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

        guess = input("Guess a latter: ").strip().upper()

        if len(guess)!= 1 or not guess.isalpha():
            print("You already guessed that letter.")
            continue

        if guess in guessed:
            print("You already guessed that latter.")
            continue

        guessed.append(guess)

        if guess in random_word:
            print("\nCorrect guess!")
        else:
            wrong_guesses+=1
            print("\nWrong guess")
            print(f"Hint: The word belongs to this category: {random_category}")

    else:
        hangman(wrong_guesses)
        print("\nGame over")
        print(f"The word was: {random_word}\n")


if __name__== "__main__":
    main()