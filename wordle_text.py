# Name: Arnav Bhasin
# UTEID: ab78845
#
# On my honor, Arnav Bhasin, this programming assignment is my own work
# and I have not provided this code to any other student

import random


def main():
    """ Plays a text based version of Wordle.
        1. Read in the words that can be choices for the secret word
        and all the valid words. The secret words are a subset of
        the valid words.
        2. Explain the rules to the player.
        3. Get the random seed from the player if they want one.
        4. Play rounds until the player wants to quit.
    """
    secret_words, all_words = get_words()
    welcome_and_instructions()

    wordleOngoing = True
    while wordleOngoing:
        print("")
        winWords = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", "Great!", "Phew!"]
        secret_word = random.choice(secret_words)
        unusedLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        previousGuesses = list()
        currentRound = 0
        tries = 6
        gameOver = False
        while (not gameOver) and (currentRound < tries):
            guess = checkValidGuess(all_words)
            status_string = getStatus(secret_word, guess)
            unusedLetters = updateUnusedLetters(guess, unusedLetters)
            previousGuesses.append(status_string)
            previousGuesses.append(guess)
            for str in previousGuesses:
                print(str)
            print("")
            printUnusedLetters(unusedLetters)
            if (guess == secret_word):
                gameOver = True
                break
            currentRound += 1
        if currentRound < tries:
            print("You win. " + winWords[currentRound] + "\n")
        else:
            print("Not quite. The secret word was " + secret_word + ".\n")
        restart = input("Do you want to play again? Type Y for yes: ")
        if restart != 'y':
            wordleOngoing = False

def printUnusedLetters(unusedLetters):
    print("Unused letters:", end = " ")
    for letter in unusedLetters[:-1]:
        print(letter, end = " ")
    print(unusedLetters[-1] + "\n")

def updateUnusedLetters(guess, unusedLetters):
    for letter1 in guess:
        if letter1 in unusedLetters:
            unusedLetters.remove(letter1)
    return unusedLetters
        
def getStatus(secret_word, guess):
    green_status = ""
    orange_status = ""
    combined_status = ""
    secret_word_letters = list(secret_word)
    new_guess = ""
    for letter1, letter2 in zip(secret_word, guess):
        if letter1 == letter2:
            green_status += "G"
            secret_word_letters.remove(letter1)
        else:
            green_status += "-"
            new_guess += letter1
    # print("green status: " + green_status)
    # print(secret_word_letters)
    """
    beets
    beset
    """
    # print("new guess: " + new_guess)
    for letter1 in new_guess:
        if letter1 in secret_word_letters:
            orange_status += "O"
            secret_word_letters.remove(letter1)
        else:
            orange_status += "-"
    # print("orange status: " + orange_status)
    # print("Zipped: " + str(list(zip(green_status, orange_status))))
    idx = 0
    for i in green_status:
        if i == "-":
            combined_status += orange_status[idx]
            idx += 1
        else:
            combined_status += i
    # for letter1, letter2 in zip(green_status, orange_status):
    #     if letter1 == "G":
    #         combined_status += "G"
    #     elif letter2 == "O":
    #         combined_status += "O"
    #     else:
    #         combined_status += "-"
    # print("combined status" + combined_status)
    return combined_status

def checkValidGuess(all_words):
    validGuess = False
    while not validGuess:
        guess = input("Enter your guess. A 5 letter word: ").upper()
        print("")
        if guess not in all_words:
            print(guess + " is not a valid word. Please try again.\n")
        else:
            validGuess = True
            return guess    

def welcome_and_instructions():
    """
    Print the instructions and set the initial seed for the random
    number generator based on user input.
    """
    print('Welcome to Wordle.')
    instructions = input('\nEnter y for instructions, anything else to skip: ')
    if instructions == 'y':
        print('\nYou have 6 chances to guess the secret 5 letter word.')
        print('Enter a valid 5 letter word.')
        print('Feedback is given for each letter.')
        print('G indicates the letter is in the word and in the correct spot.')
        print('O indicates the letter is in the word but not that spot.')
        print('- indicates the letter is not in the word.')
    set_seed = input(
        '\nEnter y to set the random seed, anything else to skip: ')
    if set_seed == 'y':
        random.seed(int(input('\nEnter number for initial seed: ')))


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


if __name__ == '__main__':
    main()
