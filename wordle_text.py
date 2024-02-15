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

    wordle_ongoing = True
    while wordle_ongoing:
        print("")
        win_words = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", 
                    "Great!", "Phew!"]
        secret_word = random.choice(secret_words)
        unused_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        previous_guesses = list()
        current_round = 0
        tries = 6
        game_over = False
        while (not game_over) and (current_round < tries):
            guess = check_valid_guess(all_words)
            status_string = get_status(secret_word, guess)
            unused_letters = update_unused_letters(guess, unused_letters)
            previous_guesses.append(status_string)
            previous_guesses.append(guess)
            for str in previous_guesses:
                print(str)
            print("")
            print_unused_letters(unused_letters)
            if (guess == secret_word):
                game_over = True
                break
            current_round += 1
        if current_round < tries:
            print("You win. " + win_words[current_round] + "\n")
        else:
            print("Not quite. The secret word was " + secret_word + ".\n")
        restart = input("Do you want to play again? Type Y for yes: ")
        if restart != 'y':
            wordle_ongoing = False

def print_unused_letters(unused_letters):
    print("Unused letters:", end = " ")
    for letter in unused_letters[:-1]:
        print(letter, end = " ")
    print(unused_letters[-1] + "\n")

def update_unused_letters(guess, unused_letters):
    for letter1 in guess:
        if letter1 in unused_letters:
            unused_letters.remove(letter1)
    return unused_letters
        
def get_status(secret_word, guess):
    green_status = ""
    full_status = ""
    secret_word_letters = list(secret_word)
    for letter1, letter2 in zip(secret_word, guess):
        if letter1 == letter2:
            green_status += "G"
            secret_word_letters.remove(letter1)
        else:
            green_status += "-"
    for letter1, letter2 in zip(green_status, guess):
        if letter1 == "G":
            full_status += "G"
        elif letter2 in secret_word_letters:
            full_status += "O"
            secret_word_letters.remove(letter2)
        else:
            full_status += "-"
    return full_status

def check_valid_guess(all_words):
    valid_guess = False
    while not valid_guess:
        guess = input("Enter your guess. A 5 letter word: ").upper()
        print("")
        if guess not in all_words:
            print(guess + " is not a valid word. Please try again.\n")
        else:
            valid_guess = True
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
