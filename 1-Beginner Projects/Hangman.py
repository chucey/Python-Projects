from random import choice

def run_game():
    word: str = choice(['apple', 'secret', 'banana', 'python'])

    username: str = input('What is your name?: ')

    # Setup
    guessed: str = ''
    tries: int = 5
    print(f'Welcome to Hangman, {username}! You have {tries} chances to guess the word')

    while tries > 0:
        blanks: int = 0
        print('Word: ', end = '')
        for char in word:
            if char in guessed:
                print(char, end= '')
            else:
                print('_', end= '')
                blanks += 1

        print()  # adds a blank line

        if blanks == 0:
            print('You got it!')
            break

        guess: str = input('Enter a letter: ')
        guess = guess.lower()

        if guess in guessed:
            print(f'You already tried "{guess}." Try another letter')
            continue

        if len(guess) > 1:

            if guess.lower() == 'quit':
                print('Thanks for playing, Goodbye')
                break

            if guess.lower() == word:
                print("You got it!")
                break

            if len(guess) > len(word):
                tries -= 1
                print(f'Too many letters, Try again. {tries} chances remaining')
                continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, "{guess}" is not in the word. {tries} chances remaining')

            if tries == 0:
                print('No more tries, You lose')
                break



if __name__ == '__main__':
    run_game()
