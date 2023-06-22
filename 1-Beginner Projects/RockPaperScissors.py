import random
import sys

class RPS:
    def __init__(self):

        self.user: str  = input('Enter your Name: ')
        print(f'Welcome to RPS 9000 {self.user}!')
        print("To stop the game, enter 'quit'")
        print('------')

        self.moves: dict = {'rock': '💎',
                            'paper': '📃',
                            'scissors': '✂'}

        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        user_input: str = input('Rock, Paper or Scissors? >> ').lower()

        if user_input == 'exit' or user_input == 'quit':
            print('Thanks for playing, Goodbye!')
            sys.exit()

        if user_input not in self.valid_moves:
            print('Invalid move!')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_input, ai_move)
        self.check_moves(user_input, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('------')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('------')

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a tie")
            print(f"Score: {self.user} {self.user_score} - {self.ai_score} AI")
        elif user_move == 'rock' and ai_move == 'scissors':
            self.user_score += 1
            print('You win!')
            print(f"Score: {self.user} {self.user_score} - {self.ai_score} AI")
        elif user_move == 'scissors' and ai_move == 'paper':
            self.user_score += 1
            print('You win!')
            print(f"Score: {self.user} {self.user_score} - {self.ai_score} AI")
        elif user_move == 'paper' and ai_move == 'rock':
            self.user_score += 1
            print('You win!')
            print(f"Score: {self.user} {self.user_score} - {self.ai_score} AI")
        else:
            self.ai_score += 1
            print('AI wins!')
            print(f"Score: {self.user} {self.user_score} - {self.ai_score} AI")

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()



