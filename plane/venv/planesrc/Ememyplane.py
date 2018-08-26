import Ememybullet
import pygame
import random
import BasePlane
class EnemyPlane(BasePlane.BasePlane):
    x=2
    y=2
    """敌机的类"""
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        # self.screen = screen_temp
        # self.image = pygame.image.load("../feiji/enemy0.png")
        # self.bullet_list = []#存储发射出去的子弹对象引用
        super().__init__(screen_temp, random.randint(0, 480),0, "../feiji/enemy0.png")  # super().__init__()
        # 爆炸效果用的如下属性
        self.hit = False# 表示是否要爆炸
        self.hitt= False#子弹和Ememyplane碰撞是否完成的判断位
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.__create_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    def __create_images(self):
            self.bomb_list.append(pygame.image.load("../feiji/enemy0_down1.png"))
            self.bomb_list.append(pygame.image.load("../feiji/enemy0_down2.png"))
            self.bomb_list.append(pygame.image.load("../feiji/enemy0_down3.png"))
            self.bomb_list.append(pygame.image.load("../feiji/enemy0_down4.png"))

    def bomb(self):
        self.hit = True
    def display(self):
        # 显示飞机
        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        #print(self.y)       #测试坐标
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                pass
                #time.sleep(1)
                #exit()  # 调用exit让游戏退出
                # self.image_index = 0
        else:
            # 显示飞机
            self.screen.blit(self.image, (self.x, self.y))

        # 显示飞机发射出去的所有子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)
    direction = "right"
    def move(self):
        self.y+=5
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(Ememybullet.Ememybullet(self.screen, self.x, self.y))