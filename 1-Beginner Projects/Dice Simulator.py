# We're going to have a prompt that says,
# How many dice would you like to roll?
# # Here we can enter numbers such as one and it will
# give us the result of that roll.
# # We can also enter numbers such as three,
# and it's going to give us three results of three different
# dice rolls.

import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():

    while True:
        try:
            user_input: str = input('How many dice do you want to roll?: ')
            if user_input.lower() == 'exit' or user_input.lower() == 'stop':
                print('Thanks for playing')
                break

            list = roll_dice(int(user_input))
            print(*list, sep = ', ' )
            print('total =', sum(list))

        except ValueError:
            print('Please enter a valid number')

if __name__ == '__main__':
    main()

