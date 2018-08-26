import Heroplane
from pygame.locals import *
import pygame
import time
import Bullet
import Ememyplane
import BasePlane
move_x,move_y=0,0
def main():
    global move_x,move_y
    #1. 创建窗口
    # 参数1 分辨率 必须为元组
    # 参数2 标志位 如果不用什么特性，就指定0 可以指定为FULLSCREEN
    # 参数3 色深
    # 返回一个pygame.Surface对象，代表了在桌面上出现的那个窗口
    screen = pygame.display.set_mode((480,852),0,32)
    # 2. 创建一个背景图片
    background = pygame.image.load("../feiji/background.png")
    # 3. 创建一个飞机图片
    screen_temp=pygame.display.set_mode((480,852),0,32)
    H=Heroplane.HeroPlane(screen_temp)
    Ememynum=3        #控制敌机数量
    Elist=[0]*Ememynum
    #创建敌机
    for i in range(Ememynum):
      Elist[i]=Ememyplane.EnemyPlane(screen_temp)  #这里可以改成函数随机生成飞机可以写成数组对象，出界就remove
    pygame.key.set_repeat(10)
    # 4. 把背景图片放到窗口中显示
    kl=False; kr=False;ku=False;kd=False;ks=False#实现同时按键移动
    while True:
        # 4.1 设定需要显示的背景图
        # 把图片的左上角贴到窗口的(0,0)点
        screen.blit(background, (0, 0))
        if(H.image_index <=3):
          H.display(Elist)
          H.fire()
        for E in Elist:
         #print(E)
         if(E.image_index <=3):
          E.display()
          E.move()
          E.fire()  # 敌机开火
         else:del E
        # 4.2 更新需要显示的内容
        pygame.display.update()
        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type ==QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if kl==True:
                    H.move_left()
                if kr==True:
                    H.move_right()
                if ku==True:
                    H.move_up()
                if kd==True:
                    H.move_down()
                if ks==True:
                    pass
                    #H.fire()
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    kl = True
                    #H.move_left()
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    kr = True
                    #H.move_right()
                elif event.key == K_w or event.key == K_UP:
                    print('up')
                    ku = True
                    #H.move_up()
                elif event.key == K_s or event.key == K_DOWN:
                    print('down')
                    kd = True
                    #H.move_down()
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
                    ks=True
                    #H.fire()
                elif event.key == K_b:
                    print('b')
                    H.bomb()
                elif event.key == K_l:
                    print('l')
                    E.bomb()
            elif event.type == KEYUP:
                kl = False
                kr = False
                ku = False
                kd = False
                ks = False
        # 适当延时让CPU效率降下来
        time.sleep(0.01)
if __name__=='__main__':
  main()