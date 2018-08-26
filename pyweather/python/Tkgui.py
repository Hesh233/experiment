from tkinter import *
import datetime
import time
import tkinter.messagebox
import mysql.connector
import requestsa
import demorequests
import json

from utils.const_value import API, KEY, UNIT, LANGUAGE
from utils.helper import getLocation
location='广州'
id=0
name=0
country=0
path=0
timezone=0
timezone_offset=0
now=0
def save():
    global location
    global id
    global name
    global country
    global path
    global timezone
    global timezone_offset
    global now
    global last_update
    global text
    global temperature
    try:
        conn = mysql.connector.connect(user="root", password="admin", database="db_test")
        cursor = conn.cursor()
        cursor.execute("insert into db_temp(name,country,timezone,timezone_offset,text,temperature) values (%s,%s,%s,%s,%s,%s)",
                       [name,country,timezone,timezone_offset,text,temperature])
        conn.commit()
        cursor.close()
        conn.close()
        tkinter.messagebox.showinfo("信息", "保存成功")
    except E:
        print("sql操作出现错误")
        tkinter.messagebox.showerror("错误", "保存失败")
def quit(a):
    a.destroy()
def getLocation():
    """get location from user input
    default beijing
    """
    argvs = sys.argv
    locationa = argvs[1] if len(argvs) >= 2 else location
    return locationa
def reflesh(a,b,c,d,e,f,g,h,i):
    global location
    global id
    global name
    global country
    global path
    global timezone
    global timezone_offset
    global now
    global last_update
    global text
    global temperature
    location = a.get()
    locationl = getLocation()
   # print(locationl)
    try:
        result = requestsa.fetchWeather(location)

        #print(result)
        result = json.loads(result)
           # print(type(result))
        result=result["results"]

      #  print(type(result))
      #  print(result[0])
        result = result[0]
        result1=result['now']
        result2=result['last_update']
        result = result['location']
        #print(result)
        id=result['id']
        name=result['name']
        country=result['country']
        path=result['path']
        timezone=result['timezone']
        print(timezone)
        timezone_offset=result['timezone_offset']
        now=result1
        last_update=result2
        text=now['text']
        temperature=now['temperature']
    except:
        tkinter.messagebox.showerror("错误", "输入内容格式有误，请重新输入")
    b.config(text=("名字:",name))
    c.config(text=("国家:",country))
    d.config(text=("位于:",path))
    e.config(text=("时间区域:",timezone))
    f.config(text=("时区:",timezone_offset))
    i.config(text=("现在天气:",text))
    g.config(text=("最后更新时间:",last_update))
    h.config(text=("最高温度:",temperature,"C"))

def getinf():
    global id
    global name
    global country
    global path
    global timezone
    global timezone_offset
    global now
    global last_update
    global text
    global temperature
    locationl = requestsa.getLocation()
    result = requestsa.fetchWeather(locationl)
    #print(result)
    result = json.loads(result)
    #print(type(result))
    result=result["results"]
    #print(type(result))
    #print(result[0])
    result = result[0]
    result1=result['now']
    result2=result['last_update']
    result = result['location']
    #print(result)
    id=result['id']
    name=result['name']
    country=result['country']
    path=result['path']
    timezone=result['timezone']
    timezone_offset=result['timezone_offset']
    now=result1
    last_update=result2
    text=now['text']
    temperature=now['temperature']
def main():
    global id
    global name
    global country
    global path
    global timezone
    global timezone_offset
    global now
    global last_update
    global text
    global temperature
    getinf()
    w = Tk()
    w.geometry("600x300")
    f = Frame(w, width=500, height=500, bd=4, relief=GROOVE)
    f.pack(fill=X, pady=5)
    # lid = Label(f, text=("id:",id))
    # lid.pack()
    lname = Label(f, text=("名字:",name))
    lname.pack()
    lcountry = Label(f, text=("国家:",country))
    lcountry.pack()
    lpath = Label(f, text=("位于:",path))
    lpath.pack()
    ltimezone = Label(f, text=("时间区域:",timezone))
    ltimezone.pack()
    ltimezone_offset = Label(f, text=("时区:",timezone_offset))
    ltimezone_offset.pack()
    lnow = Label(f, text=("现在天气:",text))
    lnow.pack()
    ltemperature = Label(f, text=("最高温度:",temperature,"C"))
    ltemperature.pack()
    llast_update = Label(f, text=("最后更新时间:",last_update))
    llast_update.pack()
    Label(w, text=("请输入市区名:")).place(x=80, y=210)
    btns = Button(text=u'退出', command=lambda: quit(a=w))
    btns.place(x=270, y=250)
    btnr = Button(text=u'查询', command=lambda: reflesh(a=text1,b=lname,c=lcountry,d=lpath,e=ltimezone,f=ltimezone_offset,g=ltemperature,h=llast_update,i=lnow))
    btnr.place(x=320, y=210)
    btnss = Button(text=u'保存', command=lambda: save())
    btnss.place(x=360, y=210)
    text1 = Entry(w)
    text1.place(x=170,y=210)
    w.mainloop()
if __name__ == '__main__':
    main()