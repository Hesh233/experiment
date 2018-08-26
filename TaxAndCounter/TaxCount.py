from tkinter import *
import tkinter.messagebox
from math import *
import random
import re
def Buttonn(a,b,c,d):
    try:
        a=a.get()
        print(a)
        a=float(a)
        b=b.get()
        b=float(b)
        c=c.get()
        c=float(c)
        d=d.get()
        print(type(c))
        d=int(d)
    except:
        tkinter.messagebox.showerror("错误", "输入内容格式有误，请重新输入")
        print("输入内容格式有误，请重新输入")
    if a>0 and a<=100000000 and a>b:
        if a<c:
            ans=a-b
        else:ans=a-a*d/100-b
        tkinter.messagebox.showinfo("信息", "税金为:%s"%ans)
    elif a<b:
        tkinter.messagebox.showerror("错误", "五险一金应小于税前工资")
    else:tkinter.messagebox.showerror("错误", "输入内容格式有误，请重新输入")

def quit(a):
    a.destroy()
def main():
    w = Tk()
    w.geometry("300x300")
    f = Frame(w, width=500, height=500, bd=4, relief=GROOVE)
    f.pack(fill=X, pady=5)
    text1 = Entry(f)
    text1.place(x=140,y=50)
    text2 = Entry(f)
    text2.place(x=140, y=75)
    text3 = Entry(f)
    text3.place(x=140, y=100)
    text4 = Entry(f)
    text4.place(x=140, y=125)
    la=Label(f, text="请输入税前工资（元）")
    la.place(x=5, y=50)
    lb=Label(f, text="请输入五险一金（元）")
    lb.place(x=5, y=75)
    lc=Label(f, text="请输入起征点（元）")
    lc.place(x=5, y=100)
    ld=Label(f, text="请输入税率（%）")
    text4.insert(INSERT,3)
    ld.place(x=5, y=125)
    #btns = Button(f, text="点击猜猜", width=9, height=1, bd=3)
    btns =Button(text=u'查询', command=lambda: Buttonn(a=text1,b=text2,c=text3,d=text4))
    btns.place(x=100, y=180)
    btns = Button(text=u'退出', command=lambda: quit(a=w))
    btns.place(x=150, y=180)
    w.mainloop()
if __name__ == '__main__':
    main()