def playGame():
    pass


def main():
    answer = 'y'
    while answer == 'y':
        playGame()
        answer = input('\nPress \'y\' to continue or any key to exit the app... ')

if __name__ == "__main__":
    main()