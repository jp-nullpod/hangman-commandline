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
def listToString(s):  
    str1 = ''  
    for ele in s:  
        str1 += ele   
 
    return str1  

def hangmanLogic(mysteryWord, letterEntered, guessedWord):    
    index = 0
    while index < len(mysteryWord):
        index = mysteryWord.find(letterEntered, index)
        if index == -1:
            break

        temp = list(guessedWord)
        temp[index] = letterEntered
        guessedWord = listToString(temp)
        index += 1

    return guessedWord

def niceDisplay(guessedWord, numberOfTries):
    for char in guessedWord:
        if char == '_':
            print(' _ ',end='')
        else:
            print(' ' + char + ' ',end='')
        
    print('\n\nNumber of tries left: ', numberOfTries ,'\n')
    
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

    while numberOfTries > 0:
        letterEntered = ''
        while len(letterEntered) != 1 or letterEntered in alreadyUsed:
            letterEntered = input('Please enter a letter: ')
            if letterEntered in alreadyUsed:
                print('You have already typed this character before\n')
                alreadyUsed.sort()
                print('Already used ', alreadyUsed)
            
        alreadyUsed.append(letterEntered)
        previousGuessedWord = guessedWord
        guessedWord = hangmanLogic(mysteryWord, letterEntered, guessedWord)

        if mysteryWord == guessedWord:
            win = True
            break

        if previousGuessedWord == guessedWord:
            numberOfTries -= 1
        
        # niceDisplay(guessedWord, numberOfTries)

def main():
    answer = 'y'
    while answer == 'y':
        playGame()
        answer = input('\nPress \'y\' to continue or any key to exit the app... ')

if __name__ == "__main__":
    main()