# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


# def is_word_guessed(secret_word, letters_guessed):
#     for char in secret_word:
#         if char in letters_guessed:
#             is_guessed = True
#         else:
#             is_guessed = False
#             break
#     return is_guessed
# # 3.3.2. The in operator
# # The `in` operator returns whether a given element is contained in a list or tuple.
# # `in` works somewhat differently with strings. It evaluates to True if one string is a substring of another string.


# # is_word_guessed('ffffffe', ['a', 'p', 'l', 'e'])

# def get_guessed_word(secret_word, letters_guessed):
#     now_guessed_word = ''
#     for char in secret_word:
#         if char in letters_guessed:
#             now_guessed_word += char
#         else:
#             now_guessed_word += "_ "           
#     return(now_guessed_word)

# # get_guessed_word('apple', ['a', 'p'])


# def get_available_letters(letters_guessed):
#     available_letter = ""
#     for char in string.ascii_lowercase:
#         if char not in letters_guessed:
#             available_letter += char
#     return(available_letter)

# # get_available_letters(['a', 'b'])


# def hangman(secret_word):
#     print("Welcome to the game Hangman. I'm thinking of a word that has", len(secret_word), "letters.")
#     guesses_left = 6
#     warnings_left = 3
#     valid_input = string.ascii_lowercase + string.ascii_uppercase
#     vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']
#     guessed_letters_list = []
    
#     while guesses_left >= 1:
#             print('you have', guesses_left, 'guesses left.')
#             print('you have', warnings_left, "warning left.")
#             print('available letter:', get_available_letters(guessed_letters_list))
#             letter_guessed = input ("Please guess a letter: ")
# # If the input is invalid            
#             if letter_guessed not in valid_input:
#                 if warnings_left >= 1:
#                     warnings_left = warnings_left - 1
#                     print(warnings_left)

#                 else:
#                     if guesses_left >= 1:
#                         guesses_left = guesses_left - 1
#                     else:
#                         print('sorry you ran out of guess, you lost rồi my dude.')
# # If the input is valid
#             else:
# # if the guessed letter is right
#                 if letter_guessed in secret_word:
#                     guessed_letters_list.append(letter_guessed)
#                     print('congrats. you guessed right.', get_guessed_word(secret_word, guessed_letters_list))
#                     if is_word_guessed == True:
#                         print("congrats! you won!")
# # If the guessed letter is wrong
#                 else:
#                     guessed_letters_list.append(letter_guessed)
#                     if letter_guessed in vowels:
#                         guesses_left -= 2
#                         if guesses_left <= 0:
#                             print("you lost r my dude")
#                         else:
#                             pass
#                     else:
#                         guesses_left -= 1
#                         if guesses_left <= 0:
#                             print("you lost r my dude")
#                         else:
#                             pass

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word_no_gap = my_word.strip('')
    if len(my_word_no_gap) != len(other_word):
        is_match = False
    else:
        for char, index in enumerate(my_word_no_gap):
            if char == "_":
                pass
            else:
                if char != other_word[index]:
                    is_match = False
                    break
                else:
                    is_match = True
    print(is_match)
    return(is_match)

match_with_gaps('te_ t', "tact")




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
