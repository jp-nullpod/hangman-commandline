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

def playGame():
    # builds a list of words from the hangman word file
    words = createPlayBoard()
    # pick a random word from the list created
    mysteryWord = pickRandomWord(words)

def main():
    answer = 'y'
    while answer == 'y':
        playGame()
        answer = input('\nPress \'y\' to continue or any key to exit the app... ')

if __name__ == "__main__":
    main()