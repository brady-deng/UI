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
        self.filename = ''
        self.rate = 16000
        self.result = 'State:'+'等待'
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.openfile = tk.Button(self)
        self.openfile["text"] = "打开..."
        self.openfile["command"] = self.open_file
        self.openfile.bind('<ButtonRelease-1>', self.setstateopen)
        self.openfile.pack(side="top")
        self.filepath = tk.Label(self)
        self.filepath["text"] = "文件路径:"+self.filename
        self.filepath.pack()
        self.speechrec = tk.Button(self)
        self.speechrec["text"] = "开始"
        self.speechrec["command"] = self.speech_rec
        self.speechrec.bind('<ButtonRelease-1>',self.setstatestart)
        self.speechrec.pack()
        self.label1 = tk.Label(self)
        self.label1["text"] = "Sample Rate:"
        # self.label1["bg"] = 'green'
        self.label1.pack()
        self.samplerate = tk.Listbox(self)
        self.samplerate["height"] = 4
        self.samplerate["width"] = 6
        self.samplerate.insert(1,8000)
        self.samplerate.insert(2,16000)
        self.samplerate.bind('<ButtonRelease-1>',self.settextlabel1)
        self.samplerate.pack()
        self.label2 = tk.Label(self)
        self.label2["text"] = self.result
        self.label2.pack()

        # self.samplerate["command"] = self.getsample


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    # def say_hi(self):
    #     print("hi there, everyone!")
    def open_file(self):
        self.filename = tkinter.filedialog.askopenfilename()
        self.filepath["text"] = "文件路径:"+self.filename

    def settextlabel1(self,event):
        self.label1["text"] = "Sample Rate:"+str(self.samplerate.get(self.samplerate.curselection()))
    def setstateopen(self,event):
        self.label2["text"] = 'State:'+'选择文件'
    def setstatestart(self,event):
        self.label2["text"] = 'State:'+'正忙'



    def speech_rec(self):
        # 识别本地文件

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
        self.label2["text"] =  'State:'+temp1['err_msg']
        # print(temp1['result'])
        # print(temp2['result'])
        #
        with open("res.txt", 'w') as file:
            file.write(temp1['result'][0])
        #     file.write(temp2['result'][0])


root = tk.Tk()
root.title("Baidu API")
root.geometry("550x550")
app = Application(master=root)
app.mainloop()