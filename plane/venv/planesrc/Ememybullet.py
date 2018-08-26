import pygame
import Bullet
import BaseBullet
class Ememybullet(BaseBullet.BaseBullet):
    def __init__(self, screen_temp, x, y):
        super().__init__(screen_temp, x + 25, y + 40, "../feiji/bullet1.png")
        # self.x = x+25
        # self.y = y+40
        # self.screen = screen_temp
        # self.image = pygame.image.load("../feiji/bullet1.png")
    def move(self):
        self.y+=10       #子弹移动速度
    # def display(self):
    #     self.screen.blit(self.image, (self.x, self.y))
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False