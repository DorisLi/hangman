# Hangman game
#

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = False
    cp_sw = secretWord[:]
    for s in cp_sw:
        if s in lettersGuessed:
            secretWord = secretWord.replace(s,'')
    if secretWord == "":
       result = True
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for a in secretWord:
        if a in lettersGuessed:
            result = result + a + ' '
        if a not in lettersGuessed:
            result += '_ '
    return result 


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a_letters = string.ascii_lowercase
    result = ''
    for k in a_letters:
        if k not in lettersGuessed:
            result += k
    return result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    lettersGuessed = []
    i = 0
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord) , ' letters long.')
    print('-------------')
    
    while i < 8:        
        print('You have ', (8 - i) , ' guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        letterGuessed = input('Please guess a letter: ').lower()
        if letterGuessed in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        else:
            lettersGuessed.append(letterGuessed)
            if letterGuessed in secretWord:
                now = getGuessedWord(secretWord, lettersGuessed)
                print('Good Guess:', now)
                print('-------------')
                if now == secretWord:
                    break
            else:
                print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                i += 1
    if isWordGuessed(secretWord, lettersGuessed): 
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was else. ')
     
    

    
    





# Simple test

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
