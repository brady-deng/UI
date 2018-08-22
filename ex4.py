import tkinter.filedialog
import tkinter as tk

from aip import AipSpeech



# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filename = tk.StringVar()
        self.rate = tk.StringVar()
        self.result = tk.StringVar()
        self.filename.set('')
        self.rate.set("采样率："+'16000')
        self.result.set('State:'+'请选择文件...')
        # self.pack()
        self.create_frame()
        self.create_widgets()

    def create_frame(self):
        self.frame_speechRec = tk.Frame(width = 550,height = 100, bg = 'green')
        self.frame_speechRec.grid(row = 0,column = 0)
        self.frame_wordRec = tk.Frame(width = 550,height = 100,bg = 'white')
        self.frame_wordRec.grid(row = 1,column = 0)
        self.frame_speechRec.grid_propagate(0)
        self.frame_wordRec.grid_propagate(0)
    def create_widgets(self):

        self.openfile = tk.Button(self.frame_speechRec)
        self.openfile["text"] = "打开..."
        self.openfile["command"] = self.open_file
        self.openfile["bg"] = 'green'
        self.openfile["fg"] = 'white'
        self.openfile.grid(row = 0,column = 0,sticky = tk.W)
        self.filepath = tk.Label(self.frame_speechRec)
        self.filepath["textvariable"] = self.filename
        self.filepath["bg"] = 'green'
        self.filepath["fg"] = 'white'
        self.filepath.grid(row = 0, column = 1,sticky = tk.W)
        self.speechrec = tk.Button(self.frame_speechRec)
        self.speechrec["text"] = "开始"
        self.speechrec["command"] = self.speech_rec
        self.speechrec["bg"] = "green"
        self.speechrec["fg"] = "white"
        self.speechrec.grid(row = 2, column = 0,sticky = tk.W)
        self.label1 = tk.Label(self.frame_speechRec)
        self.label1["textvariable"] = self.rate
        self.label1["bg"] = 'green'
        self.label1["fg"] = 'white'
        self.label1.grid(row = 1,column = 1,sticky = tk.W)
        self.samplerate = tk.Listbox(self.frame_speechRec)
        self.samplerate["height"] = 2
        self.samplerate["width"] = 6
        self.samplerate.insert(1,8000)
        self.samplerate.insert(2,16000)
        self.samplerate['bg'] = 'green'
        self.samplerate['fg'] = 'white'

        self.samplerate.bind('<ButtonRelease-1>',self.settextlabel1)
        self.samplerate.grid(row = 1,column = 0,sticky = tk.W)
        self.label2 = tk.Label(self.frame_speechRec)
        self.label2["textvariable"] = self.result
        self.label2['bg'] = 'green'
        self.label2['fg'] = 'white'
        self.label2.grid(row = 2,column = 1,sticky = tk.W)

        # self.samplerate["command"] = self.getsample


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(row = 3)

    # def say_hi(self):
    #     print("hi there, everyone!")
    def settextlabel1(self,event):
        self.rate.set("采样率："+str(self.samplerate.get(self.samplerate.curselection())))
    def open_file(self):
        self.filename.set(tkinter.filedialog.askopenfilename())






    def speech_rec(self):
        # 识别本地文件
        self.result.set("State:"+"正忙")
        APP_ID = '11388941'
        API_KEY = '0ZYGXXiNUMXDalelafeEL0GW'
        SECRET_KEY = 'VmTREEGWKm4V0DPAyQLfuEwhwISZoXx6 '
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        temp1 = client.asr(get_file_content(self.filename), format='wav', rate=self.samplerate.get(self.samplerate.curselection()), options={
            'dev_pid': 1737,
        })
        # temp2 = client.asr(get_file_content('2.amr'), format='amr', rate=8000,options= {
        #     'lan': 'en',
        # })
        self.result.set('State:'+temp1['err_msg'])
        # print(temp1['result'])
        # print(temp2['result'])
        #
        with open("res.txt", 'w') as file:
            file.write(temp1['result'][0])
        #     file.write(temp2['result'][0])


root = tk.Tk()
root.title("Baidu API")
root.geometry("550x550")
root.iconbitmap('bitbug_favicon.ico')
app = Application(master=root)
app.mainloop()