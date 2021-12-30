from core import CharWalk
import pygame

class Game:
    def __init__(self, screen, start_x, start_y, end_x, end_y, heroes, fps=60):
        self.screen = screen
        self.fps = fps
        self.heroes = pygame.image.load(heroes).convert_alpha()
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.__init_game()

    def __init_game(self):
        self.heroes = pygame.transform.scale(self.heroes, (128 * 4, 128 * 4))
        # self.heroes = pygame.transform.scale(self.heroes, (16 * 4, 48*4))
        self.role = CharWalk(self.heroes, CharWalk.DIR_DOWN, self.start_x, self.start_y)  # 读取出发坐标
        self.role.goto(self.end_x, self.end_y)  # 读取到达坐标
