import random
import string

WORDLIST_FILENAME = "D:\Hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    if secretWord=="":
        return True
    else:
        if secretWord[0] not in lettersGuessed:
            return False
        else:
            return True and isWordGuessed(secretWord[1:], lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    g=""
    for s in secretWord:
        if s in lettersGuessed:
            g=g+s
        else:
            g=g+'_'
    return g



def getAvailableLetters(lettersGuessed):
    import string
    x=string.ascii_lowercase
    for s in lettersGuessed:
        if s in x:
            x=x.replace(s,"")
    return x
    

def hangman(secretWord):
    secretWord=secretWord.lower()
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    print "-------------"
    g=8
    lettersGuessed=[]
    while isWordGuessed(secretWord, lettersGuessed)==False and g!=0:
        print "You have "+str(g)+" guesses left."
        print "Available letters: "+getAvailableLetters(lettersGuessed)
        guess=str(raw_input("Please guess a letter: "))
        guess=guess.lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print "Good guess: "+getGuessedWord(secretWord, lettersGuessed)
                print "-------------"
            else:
                g-=1
                print "Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed)
                print "-------------"
                
        else:
            print "Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was else."
    
   
