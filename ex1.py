
import tkinter as tk




class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.openfile = tk.Button(self)
        self.openfile["text"] = "打开..."
        self.openfile["command"] = self.say_hi
        self.openfile.pack(side="top")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")



root = tk.Tk()
app = Application(master=root)
app.mainloop()