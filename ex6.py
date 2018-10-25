import tkinter as tk
import pymysql
import time
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.state = tk.StringVar()
        self.state.set("Wait")
        self.button1 = tk.Button(self,text = "开始",command = self.input)
        self.Lstate = tk.Label(self, textvariable=self.state)
        self.button2 = tk.Button(self,text = "关闭",command = self.quitdemo)
        self.button1.grid(row = 0,column = 0)
        self.button2.grid(row = 0,column = 1)
        self.Lstate.grid(row = 1)
        self.pack()
    def input(self):
        self.time = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS brady")
        restemp = cursor.fetchall()
        self.state.set(str(restemp))
        cursor.execute("USE brady")
        self.state.set(str(cursor.fetchall()))
        cursor.execute("CREATE TABLE IF NOT EXISTS time(time varchar(20))")
        self.state.set(str(cursor.fetchall()))
        cursor.execute("INSERT INTO time VALUES('%s')" % (self.time))
        self.state.set(str(cursor.fetchall()))
    def quitdemo(self):
        self.destroy()
        root2.destroy()

class msgbox(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.state = 1
        self.stateVar = tk.StringVar()
        self.stateVar.set("State: Wait")
        self.createwiget()
    def createwiget(self):
        self.labeluser = tk.Label(self, text="User:")
        self.labelpassword = tk.Label(self, text="Password:")
        self.textuser = tk.Entry(self)
        self.textpassword = tk.Entry(self)
        self.buttonlogin = tk.Button(self, text="登录", command=self.login)
        self.buttonquit = tk.Button(self, text="退出", command=self.demoquit)
        self.labelstate = tk.Label(self, textvariable=self.stateVar)
        self.labeluser.grid(row=0, column=0)
        self.textuser.grid(row=0, column=1)
        self.labelpassword.grid(row=1, column=0)
        self.textpassword.grid(row=1, column=1)
        self.buttonlogin.grid(row=2, column=0)
        self.buttonquit.grid(row=2, column=1)
        self.labelstate.grid(row = 3,column = 1,sticky = tk.W)
        self.pack()

    def login(self):
        user = self.textuser.get()
        password = self.textpassword.get()
        try:
            global db
            db = pymysql.connect("localhost", user, password)
            self.state = 1
        except:
            self.state = 0
        if self.state == 1:
            self.stateVar.set("State: Success")
            self.destroy()
            root.destroy()
            global root2
            root2 = tk.Tk()
            root2.config(width = 500)
            root2.config(height = 500)
            Application(master=root2)
        else:
            self.stateVar.set("State: Fail")

    def demoquit(self):
        self.destroy()
        root.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    temp2 = msgbox(master=root)
    temp2.mainloop()