import pygame
import Base
class BaseBullet(Base.Base):
    def __init__(self, screen_temp, x, y, image_name):
    #     self.x = x
    #     self.y = y
    #     self.screen = screen_temp
    #     self.image = pygame.image.load(image_name)
       super().__init__(screen_temp, x, y, image_name)
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))