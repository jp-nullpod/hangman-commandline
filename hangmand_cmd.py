import random

def createPlayBoard():
    words = []
    file = open('./hangman_words_db','r')
    for line in file:
        words.append(line.rstrip()) # remove unnecessary spaces from the list
    file.close()
    return words

def pickRandomWord(words):
    total = len(words)-1
    index = random.randint(0,total)
    return words[index]

def initGuessedWord(mysteryWord):
    """a utility function to display the underscores with spaces for the hidden mystery word"""
    guessedWord = ''
    wordLength = len(mysteryWord)
    
    for i in range(wordLength):
        guessedWord += '_'

    return guessedWord

def playGame():
    # builds a list of words from the hangman word file
    words = createPlayBoard()
    # pick a random word from the list created
    mysteryWord = pickRandomWord(words)
    # default number of tries in a game, this might as well be in a config file
    numberOfTries = 10
    # display _ for the mystery word
    guessedWord = initGuessedWord(mysteryWord)
    win = False
    # array to keep letters already used before by the user
    alreadyUsed = []

def main():
    answer = 'y'
    while answer == 'y':
        playGame()
        answer = input('\nPress \'y\' to continue or any key to exit the app... ')

if __name__ == "__main__":
    main()