class Chess:
    def __init__(self):
        self.a=[[1 for i in range(23)] for i in range(23)]    #防止出界
        self.player=("A","B")
        self.k=0      #下棋先后，0：A先，1：B先
        #check=((-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1))
        #self.answer=False
    def outrange(self):                 #打印棋盘内容
       for i in range(3,19):
          for j in range(3,19):
              if i == 3 :
                  self.a[i][j] = j-3
              if j == 3:
                  self.a[i][j] = i - 3
              if i in range(4,19)and j in range(4,19):
                  self.a[i][j]="*"
    def printchess(self):                 #打印棋盘
       for i in range(3,19):
           for j in range(3,19):
             if i == 3and self.a[i][j]>9:
                   print(self.a[i][j],end=" ")
                   continue
             if j==3and self.a[i][j]>9:
                 print(self.a[i][j],end=" ")
                 continue
             print(self.a[i][j],end="  ")
           print()
    def checkwin(self,k):                   #判断输赢
        for i in range(4,19):
            for j in range(4,19):
                 if((self.a[i][j]==self.player[k]and self.a[i-1][j-1]==self.player[k]and self.a[i-2][j-2]==self.player[k]and self.a[i-3][j-3]==self.player[k]and self.a[i-4][j-4]==self.player[k])or(self.a[i][j]==self.player[k]and self.a[i+1][j+1]==self.player[k]and self.a[i+2][j+2]==self.player[k]and self.a[i+3][j+3]==self.player[k]and self.a[i+4][j+4]==self.player[k])or(self.a[i][j]==self.player[k]and self.a[i-1][j]==self.player[k]and self.a[i-2][j]==self.player[k]and self.a[i-3][j]==self.player[k]and self.a[i-4][j]==self.player[k])or(self.a[i][j]==self.player[k]and self.a[i][j+1]==self.player[k]and self.a[i][j+2]==self.player[k]and self.a[i][j+3]==self.player[k]and self.a[i][j+4]==self.player[k])):#遍历棋盘判断，写起来比较简单
                     self.printchess()
                     print(self.player[k]+"win")
                     return True
                 else:
                     return False
    def setchess(self,x,y,k):                 #下子
        self.a[x][y]=self.player[k]
    def input(self,k):                #负责输入
        try:
            x = int(input("玩家" + self.player[k] + "输入下棋X(横)坐标")) + 3            #服务器想法:if k=0输入xy并上传 if k=1等待对方输入xy
            y = int(input("玩家" + self.player[k] + "输入下棋Y(纵)坐标")) + 3            #如果传不了参数，考虑写多一个input（）函数
        except:
            print("输入格式有误，请输入1-15整数")
            return self.input(k)
        if  x not in range(4,19)and  y not in range(4,19):
            print("输入格式有误，请输入1-15整数")
            return self.input(k)
        elif self.a[x][y]=="*":
            self.setchess(x,y,k)
        else:
            print("已有子，重新下子")
            return self.input(k)                 #输入部分
        return self.changeplayer(k)

    def changeplayer(self,k):
        if self.checkwin(k)==False:            #交换玩家
            if k == 0:
                k = 1
                self.printchess()               #交换前打印一次棋盘
            elif k == 1:
                k = 0
                self.printchess()               #交换前打印一次棋盘
            return self.input(k)
def main():
    c=Chess()
    c.outrange()
    c.printchess()
    c.input(0)
if __name__ == '__main__':
    main()