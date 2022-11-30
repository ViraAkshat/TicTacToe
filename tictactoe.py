import pygame
import sys
from random import randint

WIN_SIZE = 450
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pygame.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.field_image = self.get_scaled_image(path='resources/field.png', res=[WIN_SIZE]*2)
        self.o_image = self.get_scaled_image(path='resources/o.png', res=[CELL_SIZE]*2)
        self.x_image = self.get_scaled_image(path='resources/x.png', res=[CELL_SIZE]*2)

        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]
        
        self.player = randint(0, 1)

        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        
        self.winner = None
        self.game_steps = 0
    
    def check_winner(self):
        for line_indices in self.line_indices_array:
            sum_line = sum([self.game_array[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:
                self.winner = 'XO'[sum_line == 0]
                self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                    vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]

    def run_game_process(self):
        current_cell = vec2(pygame.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pygame.mouse.get_pressed()[0]

        if left_click and self.game_array[row][col] ==  INF and not self.winner:
            self.game_array[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()

    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != INF:
                    self.game.screen.blit(self.x_image if obj else self.o_image, vec2(x, y)*CELL_SIZE)
    
    def draw_winner(self):
        if self.winner:
            pygame.draw.line(self.game.screen, 'red', *self.winner_line, CELL_SIZE // 8)

    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()

    @staticmethod
    def get_scaled_image(path, res):
        img = pygame.image.load(path)
        return pygame.transform.smoothscale(img, res)
    
    def print_caption(self):
        pygame.display.set_caption(f'Player"{"OX"[self.player]}" turn!')
    
    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIN_SIZE]*2)
        self.clock = pygame.time.Clock()
        self.tic_tac_toe = TicTacToe(self)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)

if  __name__ == '__main__':
    game = Game()
    game.run()