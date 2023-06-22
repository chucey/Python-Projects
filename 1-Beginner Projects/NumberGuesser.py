# For this Python project, we're going to be creating
# a number guessing game.
# And the first thing that's going to happen is that it's
# going to print to the console to guess the number
# in the range from whatever we specify,
# which in this example is going to be 1 to 10.
# You have three chances to guess the correct number


from random import randint

low_number, high_number = 1 , 10
random_number: int = randint(low_number, high_number)
guess_count = 0


print(f'Guess the number in the range from {low_number} to {high_number}')

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number')
        continue

    guess_count += 1

    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it')
        break

    if guess_count == 3:
        print('out of guesses')
        break

