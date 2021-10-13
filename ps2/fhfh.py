
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
print(wordlist)
def match_with_gaps(my_word):
    my_word_no_spaces = []
    for char in my_word:
        if char != ' ':
            my_word_no_spaces.append(char)
        else:
            pass
    for index, char in enumerate(my_word_no_spaces):
        if char != wordlist[index]:
            print("no matches!")
        else:
            print(wordlist)
match_with_gaps ("t_ _ t")
