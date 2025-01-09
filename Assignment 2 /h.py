def is_word_guessed(secret_word, letters_guessed):
    # Check if all letters in secret_word are in letters_guessed
    return all(letter in letters_guessed for letter in secret_word)


def hangman(secret_word):
    # Initialize letters_guessed as an empty list
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-----------------------------")
    
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            warnings_left -= 1
            if warnings_left > 0:
                print(f"Invalid input. You have {warnings_left} warnings left.")
            else:
                print("You have no warnings left. You lose a guess.")
                guesses_left -= 1
            print("-----------------------------")
            continue

        if guess in letters_guessed:
            warnings_left -= 1
            if warnings_left > 0:
                print(f"You've already guessed that letter. You have {warnings_left} warnings left.")
            else:
                print("You have no warnings left. You lose a guess.")
                guesses_left -= 1
            print("-----------------------------")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word.")
            guesses_left -= 1

        print("-----------------------------")

        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations! You guessed the word: {secret_word}")
            print(f"Your score is: {guesses_left * len(set(secret_word))}")
            return

    print(f"Sorry, you ran out of guesses. The word was: {secret_word}")

