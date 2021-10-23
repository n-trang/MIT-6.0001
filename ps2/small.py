
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

def match_with_gaps(my_word):
    matched_word = []
    my_word_no_spaces = []
    meaningful_character = []
#fillter `space` character out of `my_word`
    for char in my_word:
        if char != ' ':
            my_word_no_spaces.append(char)
        else:
            pass
# find `list` of tuples which each element is a set of meaningful character and its index.
    for index, char in enumerate(my_word_no_spaces):
        if char != "_":
            meaningful_character.append((index, char))
        else:
            pass
        print("meaningful", meaningful_character)
# Check first condition: `my_word` and `word` has the same length.
    for word in wordlist:
        if len(word) != len(my_word_no_spaces):
            pass
    else:
# Check second condition: if they match or not:
            for set in meaningful_character:
                index = set[0]
                print(set[1] == word[index])
                return(matched_word)
    
match_with_gaps('a_ _ _ e')
