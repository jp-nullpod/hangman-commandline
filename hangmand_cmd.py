
def createPlayBoard():
    words = []
    file = open('./hangman_words_db','r')
    for line in file:
        words.append(line.rstrip())
    file.close()
    return words


def playGame():
    words = createPlayBoard()

def main():
    answer = 'y'
    while answer == 'y':
        playGame()
        answer = input('\nPress \'y\' to continue or any key to exit the app... ')

if __name__ == "__main__":
    main()