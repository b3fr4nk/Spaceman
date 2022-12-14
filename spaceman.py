import random

unique_letters = []
wrong_guesses = []
correct_guesses = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)


    return secret_word

def is_word_guessed(secret_word, correct_guesses):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been guessed correctly.

    Returns: 
        bool: True only if all the letters of secret_word are in correct_guesses, False otherwise
    '''
    #Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    return len(correct_guesses) == len(unique_letters)

def get_guessed_word(secret_word, correct_guesses):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been guessed correctly so far.

    Returns: 
        list: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    output_phrase = []

    for i in range(len(secret_word)):
        output_phrase.append("_")

    for guess in correct_guesses:
        for letter in range(len(secret_word)):
            if guess == secret_word[letter]:
                output_phrase[letter] = secret_word[letter]
    return output_phrase




def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #Check if the letter guess is in the secret word
    for letter in unique_letters:
        if guess == letter:
            correct_guesses.append(guess)
            return True
    return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    dead = False

    #show the player information about the game according to the project spec
    print("Welcome to Spaceman the PG version of hangman \n You will guess one letter at a time. If you guess wrong one part of the spaceman will be drawn. Once the spaceman is fully drawn you lose")
    
    while not dead:
        #Ask the player to guess one letter per round and check that it is only one letter
        guess = input("Guess a letter: ")
        if guess in wrong_guesses or guess in correct_guesses:
            print("you have already guessed that letter!")
            continue

        #Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("congrats you guessed a letter")
            print(get_guessed_word(secret_word, correct_guesses))
        
        else:
            wrong_guesses.append(guess)
            #check if the game has been won or lost
            if len(wrong_guesses) > 6:
                print("you lose your spaceman is dead")
                break
            else:
                print(f"your guess is not part of the word, you have {7 - len(wrong_guesses)} guesses left")
        #check if word is guessed and respond accordingly
        if is_word_guessed(secret_word, correct_guesses):
                print(f"congrats you guessed the word with {7 - len(wrong_guesses)} guesses remaining")
                break
        else:
            print("word is not guessed yet")




#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
