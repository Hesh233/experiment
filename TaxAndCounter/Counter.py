import re
import mysql.connector
import datetime
import time
from tkinter import *
import tkinter.messagebox
btn=[]
hy=50
hx=200
tempx=0
tempy=50
k=1
w=Tk()
w.geometry("600x600")
string=""
Label(w,text="计算器,有删除7天前数据功能").pack()
la=Label(w,text="")
la.pack()
menubar=Menu(w)
fmenu = Menu(menubar)
fmenu.add_command(label="退出1")
fmenu.add_command(label="退出2")
fmenu.add_command(label="退出3")
menubar.add_cascade(label='菜单1还没写完',menu=fmenu)
menubar.add_cascade(label='菜单2',menu=fmenu)
menubar.add_cascade(label='菜单3',menu=fmenu)
fmenu.bind("<Button-1>",quit)
w['menu']=menubar
f=Frame(w,width=500,height=500,bd=4,relief=GROOVE)
f.pack(fill=X,pady=5)
def quit(event):
    print("asjoidawh")
def show(event):
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'admin',
        'port': 3306,
        'database': 'db_test',
        'charset': 'utf8'
    }
    list = {}
    listtime={}
    try:
        cnn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
    cursor = cnn.cursor()
    try:
        text1 = Text(f, width=50, height=30)
        sql_query = 'select keyvalue,date,id from cal ;'
        cursor.execute(sql_query)
        for keyvalue, date, id in cursor:
            # print (name, age)
            list[id] = [keyvalue, date]
            listtime[id]=date
            text1.insert(INSERT, str(["id:%s"%id, "值:%s"%keyvalue, "日期:%s"%date])+"\n")
        for i in list:
            print((listtime.get(i)-datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')).days)
            if(listtime.get(i)-datetime.datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'%Y-%m-%d %H:%M:%S')).days<-7:
                query ="delete from cal where id ='%s'"%(i)
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    Label(f, text="时间问题就不弄出来了，你能看懂的").place(x=hx-25 , y=hy + 250)
    text1.place(x=hx-80 , y=hy + 300)
    cnn.commit()
    cursor.close()
    cnn.close
def save(event):
   try:
    conn = mysql.connector.connect(user="root", password="admin",database = "db_test")
    cursor = conn.cursor()
    cursor.execute("insert into cal(keyvalue,date) values (%s,%s)", [string,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))])
    conn.commit()
    cursor.close()
    conn.close()
    tkinter.messagebox.showinfo("信息", "已保存")
   except E:
       print("sql操作出现错误")
def Buttonn(event):
    global string
    #print(string+"字符串是")
    print(event.widget['text'])
    if re.compile(r'[0-9]',re.I).match(str(event.widget['text'])):
       string=string+str(event.widget['text'])
       la.config(text=string)
    elif event.widget['text']=="=":
      #  print(abs(eval(string))//10)
        if string=="":
            pass
        else:
         print(string)
         try:
           # setlocale('English_US',LC_NUMERIC)
           # string=atof(string)
           print(eval(string))
           # if abs(eval(string))>=1000:
           #     k = 1
           #     for i in range(1,100):
           #        if abs(eval(string))//k>0 and abs(eval(string))//k<10:
           #           k=i
           #           break
           #        k*=10
           # print(k)
           la.config(text=eval(string))
           print(string + "字符串是")
         except:
           la.config(text="输入内容格式有误!")
         string=str(eval(string))
    elif event.widget['text'] == "←":
       string=string[:-1]
       la.config(text=string)
    elif event.widget['text']=="c":
        string=""
        la.config(text="")
    else:
        string = string + str(event.widget['text'])
        la.config(text=string)
for i in range(1,10):
    btn.append(Button(f,text=i,width=3, height=1,bd=3))
    btn[i-1].bind('<Button-1>',Buttonn)
    if i%3-1!=0and i!=1:
     btn[i-1].place(x=50*i-tempx+hx,y=tempy)
    else:tempy+=50;tempx=50*i;btn[i-1].place(x=50*i-tempx+hx,y=tempy)
btn0=Button(f,text=0,width=3, height=1,bd=3)
btn0.bind('<Button-1>',Buttonn)
btn0.place(x=hx,y=hy+200)
btneq=Button(f,text="=",width=3, height=4,bd=3)
btneq.bind('<Button-1>',Buttonn)
btneq.place(x=hx+150,y=150+hy)
btnc=Button(f,text="c",width=3, height=1,bd=3)
btnc.bind('<Button-1>',Buttonn)
btnc.place(x=hx,y=hy)
btna=Button(f,text="+",width=3, height=1,bd=3)
btna.bind('<Button-1>',Buttonn)
btna.place(x=hx+50,y=hy)
btna=Button(f,text="-",width=3, height=1,bd=3)
btna.bind('<Button-1>',Buttonn)
btna.place(x=hx+100,y=hy)
btns=Button(f,text="/",width=3, height=1,bd=3)
btns.bind('<Button-1>',Buttonn)
btns.place(x=hx+150,y=hy+100)
btnx=Button(f,text="*",width=3, height=1,bd=3)
btnx.bind('<Button-1>',Buttonn)
btnx.place(x=hx+150,y=hy+50)
btnb=Button(f,text="←",width=3, height=1,bd=3)
btnb.bind('<Button-1>',Buttonn)
btnb.place(x=hx+150,y=hy)
btnsav=Button(f,text="保存",width=3, height=1,bd=3)
btnsav.bind('<Button-1>',save)
btnsav.place(x=hx+50,y=hy+200)
btnshow=Button(f,text="查询",width=3, height=1,bd=3)
btnshow.bind('<Button-1>',show)
btnshow.place(x=hx+100,y=hy+200)
w.mainloop()
