import os
from tkinter import *
#os.system("python filename")
def Buttonn(a):
    if a==1:
        os.system("python D:\\python资料\\plane\\venv\\planesrc\\first.py")
    if a==2:
        os.system("python D:\\python资料\\PlayChess\\client.py")#这里控制台不能这样调用
    if a==3:
        os.system("python D:\\python资料\\PlayChess\\server.py")
    if a==4:
        os.system("python D:\\python资料\\pyweather\\python\\Tkgui.py")
    if a==5:
        os.system("python D:\\python资料\\TaxAndCounter\\Counter.py")
    if a == 6:
        os.system("python D:\\python资料\\TaxAndCounter\\TaxCount.py")
w = Tk()
w.geometry("300x300")
f = Frame(w, width=500, height=500, bd=4, relief=GROOVE)
f.pack(fill=X, pady=5)
btn1 = Button(text=u'111', command=lambda: Buttonn(a=1))
btn1.place(x=150, y=30)
btn2 = Button(text=u'222', command=lambda: Buttonn(a=2))
btn2.place(x=150, y=70)
btn3 = Button(text=u'333', command=lambda: Buttonn(a=3))
btn3.place(x=150, y=110)
btn4 = Button(text=u'444', command=lambda: Buttonn(a=4))
btn4.place(x=150, y=140)
btn5 = Button(text=u'555', command=lambda: Buttonn(a=5))
btn5.place(x=150, y=180)
btn5 = Button(text=u'666', command=lambda: Buttonn(a=6))
btn5.place(x=150, y=220)
w.mainloop()