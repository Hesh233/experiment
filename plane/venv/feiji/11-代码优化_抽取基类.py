# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
import random

class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []#存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):

        BasePlane.__init__(self, screen_temp, 210, 700, "./feiji/hero1.png") #super().__init__()
    '''
    #move_a, move_d, move_w, move_s = 0, 0, 0, 0
    
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
        
    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5
    '''
    def move_yidong(self,move_a,move_y):
        self.x+=move_a
        self.y+=move_y
    
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    """敌机的类"""
    def __init__(self, screen_temp):
        a=random.randint(0,420-50)
        BasePlane.__init__(self, screen_temp, a, 0, "./feiji/enemy0.png")
        self.direction = "right"#用来存储飞机默认的显示方向
    '''
    def move(self):
        
        if self.direction=="right":
            self.x += 5
        elif self.direction=="left":
            self.x -= 5

        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"
    '''
    def move(self):
        self.y+=1
        if self.direction=="right":
            self.x += 3
        elif self.direction=="left":
            self.x -= 3
        if self.y>852-39 :
            self.y=0
            self.x=random.randint(0,480-50)
        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"
        
        
    def fire(self):
        random_num = random.randint(1,100) 
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def move(self):
        self.y-=20

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./feiji/bullet1.png")

    def move(self):
        self.y+=5

    def judge(self):
        if self.y>852:
            return True
        else:
            return False
move_x,move_y=0,0
def key_control(hero_temp):
    global move_x,move_y
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                move_x = -5
            elif event.key == K_d or event.key == K_RIGHT:
                move_x = 5
            elif event.key == K_UP or event.key == K_w:
                move_y = -5
            elif event.key == K_DOWN or event.key == K_s:
                move_y = 5
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
            elif event.key == K_ESCAPE:
                quit()
        elif event.type == KEYUP:
            # 如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0
    hero_temp.move_yidong(move_x,move_y)
    '''
    # 计算出新的坐标
    x += move_x
    y += move_y
    
    '''
    '''
    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是d或者right
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero_temp.move_up()
            #检测按键是否是d或者right
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                
                hero_temp.move_down()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
        elif event.type == KEYUP:
    '''               
    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            elif event.key == K_UP or event.key == K_w:
                hero_temp.move_up()
            elif event.key == K_DOWN or event.key == K_s:
                hero_temp.move_down()
            elif event.key == K_SPACE:
                #print('space')
                hero_temp.fire()
        elif event.type == KEYUP:
            # 某一个方向的键盘被松开，这个方向的偏移量赋为0
            if event.key == K_a or event.key == K_LEFT:
                move_a = 0
            elif event.key == K_d or event.key == K_RIGHT:
                move_d = 0
            elif event.key == K_UP or event.key == K_w:
                move_w = 0
            elif event.key == K_DOWN or event.key == K_s:
                move_s = 0
    
    # 按下键盘时，飞机对应的移动偏移量会变成1，飞机的位置进行相应的加减操作，刷新显示来控制飞机的移动
    # 如果一直按住键盘不动，飞机对应的移动偏移量就会一直为1，飞机的位置就会随着while的不断循环而改变

    # 飞机移动后的位置
    x = x + move_d - move_a
    y = y + move_s - move_w
　　# 标记2
    '''
    '''
    # 控制飞机的范围，不能超出屏幕，还要考虑到子弹应该能够发射到任意一个地方
    # 左右边界飞机应该可以进入一半
    if x > screen_width-mv_image_width/2:
        x = screen_width-mv_image_width/2
    elif x < 0-mv_image_width/2:
        x = 0-mv_image_width/2
    # 下边界的话能够看到飞机头部就行
    if y > screen_height-mv_image_height/5:
        y = screen_height-mv_image_height/5
    # 上边界不允许飞机进入
    elif y < 0:
        y = 0
    '''

def main():
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2. 创建一个背景图片
    background = pygame.image.load("./feiji/background.png")

    #3. 创建一个飞机对象
    hero = HeroPlane(screen)

    #4. 创建一个敌机
    #enemy = EnemyPlane(screen)

    ''' # 飞机的移动偏移量，每个方向设置一个
    move_a, move_d, move_w, move_s = 0, 0, 0, 0
    '''
    #设置屏幕大小
    #screen_width = 480
    #screen_height = 852
    #mv_image = pygame.image.load(image)

    '''    # 获取飞机的长度
    mv_image_width = mv_image.get_width()

    # 获取飞机的宽度
    mv_image_height = mv_image.get_height()

    # 飞机的起始位置，应该在下面的正中间
    x, y = screen_width/2-mv_image_width/2, screen_height-mv_image_height
    '''
    enemy=[]
    for i in range(3):
        enemy.append(EnemyPlane(screen))
    while True:
        screen.blit(background, (0,0))
        hero.display()
        '''
        enemy.display()
        enemy.move()#调用敌机的移动方法
        enemy.fire()#敌机开火
        '''
        for i in range(3):
            enemy[i].display()
            enemy[i].move()#调用敌机的移动方法
            enemy[i].fire()#敌机开火
            
            
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
