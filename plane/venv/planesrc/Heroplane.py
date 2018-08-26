import pygame
import Bullet
import BasePlane
import time
class HeroPlane(BasePlane.BasePlane):
    def __init__(self, screen_temp):
        self.countE=0
        self.Elist=[]
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.hero1=pygame.image.load("../feiji/hero1.png")
        self.hero2=pygame.image.load("../feiji/hero2.png")
        self.image =self.hero1
        self.bullet_list = []
        # 爆炸效果用的如下属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.__create_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号
        self.bulletcount = 0
       # super().__init__(self.screen, self.x, self.y,self.image)
       # super().__init__(screen_temp, 210, 700, "../feiji/hero1.png")  # super().__init__()
    def __create_images(self):
        self.bomb_list.append(pygame.image.load("../feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("../feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("../feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("../feiji/hero_blowup_n4.png"))
    def bomb(self):
        self.hit = True
    def turn(self):
        if self.image == self.hero1:
            self.image = self.hero2
        else:
            self.image = self.hero1
    def move_up(self):
        self.y -= 5
        self.turn()
    def move_down(self):
        self.y += 5
        self.turn()
    def move_left(self):
        self.x -= 5
        self.turn()
    def move_right(self):
        self.x += 5
        self.turn()
    def display(self,Elist):
        # 显示飞机
        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index >3:
                time.sleep(1)
                exit()  # 调用exit让游戏退出
                # self.image_index = 0
        else:
        # 显示飞机
             self.screen.blit(self.image, (self.x, self.y))
        # 显示飞机发射出去的所有子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            for E in Elist:
             #print(Elist.__len__())
              if bullet.judge(E)and E.hit==True and E.hitt==False:  # 判断子弹是否越界和碰撞and防止溢出  判断写好一半
                #print(self.countE)
                E.hitt=True
                self.bullet_list.remove(bullet)
                break
              if E.hit == True:
                 self.countE += 1
            if bullet.judgge() :
                self.bullet_list.remove(bullet)
    def fire(self):
        if self.bulletcount%30==0:
           self.bullet_list.append(Bullet.Bullet(self.screen, self.x, self.y))
        self.bulletcount+=1
        #self.Elist=Elist
        # for E in Elist:
        #     print(E)

