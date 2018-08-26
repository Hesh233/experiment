#先运行服务端server，再运行客户端，A是client，B是serverr，输入完后必须等待对方输入
import socket
import time
import ChessN
import string
host = socket.gethostname()
port = 12345
print("主机端使用")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(3)
sock,addr = s.accept()
c = ChessN.Chess()
c.outrange()
#c.printchess()
print('Connection built')
info = sock.recv(1024).decode()
count=0
k=1
while info != 'exit':
    #print(info)
    info=info.split(",")
    if count==0:
        #print(info)
        #print(type(info))
        try:
          info[0],info[1],info[2]
        except:
            print("对方赢了")
            break
        c.setchess(int(info[0]),int(info[1]),0)
        c.printchess()
        c.checkwin(int(info[2]))
        send_mes = c.input(k) + c.changeplayer(k)
        send_mes = ','.join(send_mes)
        c.checkwin(int(info[2]))
    if count!=0:
        print(info)
        print(type(info))
        try:
          print(info[0],info[1],info[2])
        except:
            print("对方赢了")
            break
        c.setchess(int(info[0]), int(info[1]),0)
        c.checkwin(int(info[2]))
        try:
           send_mes = c.input(k) + c.changeplayer(k)
        except:
            print("你赢了!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        send_mes = ','.join(send_mes)
        # if c.checkwin(1):
        #     send_mes = "你赢了!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        #     break
        # c.checkwin(int(info[2]))
    count+=1

    #print('客户端:'+str(info))
    #send_mes = input()
    #send_mes =str(send_mes)
    sock.send(send_mes.encode())
    if send_mes =='exit':
        break
    info = sock.recv(1024).decode() #下次发信息前卡在这
    time.sleep(1)                   #防止粘包
    #print ("对方发送")
    c.printchess()
sock.close()
s.close()
