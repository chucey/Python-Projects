import pygame
from pygame.font import Font
from pygame.time import Clock
import random
import sys

class DodgySquare:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        # screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Dodgy Square')

        # colours
        self.white: tuple = (255,255,255)
        self.black: tuple = (0,0,0)
        self.red: tuple = (255,99,71)
        self.blue: tuple = (65, 105, 225)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)
        self.font_2: Font = pygame.font.Font(self.default_font, 22)

        # Player
        self.player_size: int = 30
        self.player_position: list[int] = [0,0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_position: list[int] = []
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_freq: int = 20 # low = many enemies, high = few enemies

        # clock
        self.clock: Clock = pygame.time.Clock()

        # game data
        self.game_over: bool = False
        self.score: int = 0
        self.frame_count: int= 0

    def create_enemy(self):
        enemy_pos: list[int] = [random.randint(0, self.screen_width- self.enemy_size),
                                -self.enemy_size]
        self.enemy_list.append(enemy_pos)

    def update_enemy_positions(self):
        if self.frame_count % self.enemy_freq == 0:
            self.create_enemy()

        for idx, enemy_pos in enumerate(self.enemy_list):
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                self.enemy_list.pop(idx)
                self.score += 1
                self.enemy_speed += 0.1

                if self.enemy_freq > 10:
                    if self.score % 15:
                        self.enemy_freq -= 2

    def detect_collision(self, player_pos: list[int], enemy_pos: list[int]) -> bool:
        px, py = player_pos
        ex, ey = enemy_pos

        if px <= ex < (px + self.player_size) or (ex <= px < (ex + self.enemy_size)):
            if py <= ey < (py + self.player_size) or (ey <= py < (ey + self.enemy_size)):
                return True
        return False

    def show_game_over(self):
        game_over_text = self.font.render('Game Over', True, self.white)
        restart_text = self.font_2.render('Press the Space Bar to restart', True, self.white)
        self.screen.blit(game_over_text, (self.screen_width //2 -90, self.screen_height //2 - 35))
        self.screen.blit(restart_text, (self.screen_width //2 -170, self.screen_height //2 - 11))


    def replay_game(self):
        # reset enemies
        self.enemy_list = []
        self.enemy_speed: float = 3
        self.enemy_freq: int = 20

        # reset game data
        self.game_over: bool = False
        self.frame_count: int = 0
        self.score: int = 0

    def draw_character(self, color: tuple, position: list[int], size:int):
        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # restart game
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_SPACE:
                        self.replay_game()

                # Get the current mouse position
                mouse_pos: tuple[int,int] = pygame.mouse.get_pos()

                # Updates the player position to follow the mouse
                self.player_position[0] = mouse_pos[0] - self.player_size // 2
                self.player_position[1] = mouse_pos[1] - self.player_size // 2

                # make sure the player stays om screen
                self.player_position[0] = max(0, min(self.player_position[0], self.screen_width - self.player_size))
                self.player_position[1] = max(0, min(self.player_position[1], self.screen_height - self.player_size))

            if not self.game_over:
                self.update_enemy_positions()

                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_position, enemy_pos):
                        self.game_over = True
                        break

                # Reset everything for the next frame
                self.screen.fill(self.black)

                # Draw the player
                self.draw_character(self.white, self.player_position, self.player_size)

                # Draw the enemies
                for enemy_pos in self.enemy_list:
                    if self.score >= 100:
                        self.draw_character(self.red, enemy_pos, self.enemy_size)
                    else:
                        self.draw_character(self.blue, enemy_pos, self.enemy_size)

                # Display score
                score_text = self.font.render(f'Score: {self.score}', True, self.white)
                self.screen.blit(score_text, [10,10])

                # Increment frame count
                self.frame_count += 1
            else:
                self.show_game_over()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = DodgySquare()
    game.run()
