import pygame
import BaseBullet
import Ememyplane
class Bullet(BaseBullet.BaseBullet):
    def __init__(self, screen_temp, x, y):
        super().__init__(screen_temp, x + 40, y - 20, "../feiji/bullet.png")
        # self.x = x+40
        # self.y = y-20
        # self.screen = screen_temp
        # self.image = pygame.image.load("../feiji/bullet.png")
    def move(self):
        self.y-=20
    # def display(self):
    #     self.screen.blit(self.image, (self.x, self.y))
    def judgge(self):
        if self.y < 0:
            return True
        else:
            return False
    def judge(self,E):
        #print(E.x)
        #print(E)
        if self.y in range(int(E.y), int(E.y + 30)) and self.x in range(
                int(E.x - 10),int(E.x + 50)):
            E.bomb()
            return True
        if self.y < 0:
            return True
        else:
            return False