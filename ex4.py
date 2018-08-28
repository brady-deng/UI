import tkinter.filedialog
import tkinter as tk
import facecv
from aip import AipSpeech,AipOcr
import function



# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # self.pack()
        self.create_speechrec_variable()
        self.create_frame()
        self.create_speechrec_widgets()
    def create_speechrec_variable(self):
        self.filename = tk.StringVar()
        self.rate = tk.StringVar()
        self.result = tk.StringVar()
        self.funcNum = tk.IntVar()
        self.state = 0
        self.filename.set('E://ex/UI/life.wav')
        self.rate.set("采样率："+'16000')
        self.result.set('State:'+'请选择文件...')
        self.funcNum.set(1)
    def create_frame(self):
        self.frame_speechRec = tk.Frame(width = 550,height = 200, bg = 'green')
        self.frame_speechRec.grid(row = 0,column = 0)
        self.frame_wordRec = tk.Frame(width = 550,height = 100,bg = 'white')
        self.frame_wordRec.grid(row = 1,column = 0)
        self.frame_speechRec.grid_propagate(0)
        self.frame_wordRec.grid_propagate(0)
    def create_speechrec_widgets(self):

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
        self.speechrec["command"] = self.rec
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
        self.func_speech = tk.Radiobutton(self.frame_speechRec)
        self.func_word = tk.Radiobutton(self.frame_speechRec)
        self.func_image = tk.Radiobutton(self.frame_speechRec)
        self.func_speech["text"] = "语音识别"
        self.func_speech["variable"] = self.funcNum
        self.func_speech['bg'] = 'green'
        # self.func_speech['fg'] = 'white'
        # self.func_speech['highlightbackground'] = 'green'
        # self.func_speech['highlightcolor'] = 'black'
        self.func_speech['value'] = 1
        self.func_speech['command'] = self.changeSpeechstate
        self.func_speech.grid(row = 0,column = 3,sticky = tk.W)
        self.func_word["text"] = "文字识别"
        self.func_word["variable"] = self.funcNum
        self.func_word['bg'] = 'green'
        # self.func_word['fg'] = 'white'
        # self.func_word['highlightbackground'] = 'green'
        # self.func_word['highlightcolor'] = 'black'
        self.func_word['value'] = 2
        self.func_word['command'] = self.changeWordstate
        self.func_word.grid(row=1,column = 3,sticky = tk.W)
        self.func_image["text"] = "人脸注册"
        self.func_image['variable'] = self.funcNum
        self.func_image['bg'] = 'green'
        self.func_image['value'] = 3
        self.func_image['command'] = self.changeImagestate
        self.func_image.grid(row=2,column = 3,sticky = tk.W)
        self.startvideo = tk.Button(self.frame_speechRec)
        self.startvideo['text'] = "打开摄像头"
        self.startvideo['bg'] = 'green'
        self.startvideo['fg'] = 'white'
        self.startvideo.grid(row = 3,column = 0,sticky = tk.W)
        self.startvideo['command'] = facecv.faceRegsearch
        self.labeluserid = tk.Label(self.frame_speechRec)
        self.labeluserid["text"] = "USER ID:"
        self.labeluserid['bg'] = 'green'
        self.labeluserid['fg'] = 'white'
        self.labeluserid.grid(row = 3,column = 1,sticky = tk.E)
        self.userid = tk.Entry(self.frame_speechRec)
        self.userid['bg'] = 'green'
        self.userid['fg'] = 'white'
        self.userid.grid(row = 3,column = 2,sticky = tk.W)
        self.labeluserinfo = tk.Label(self.frame_speechRec)
        self.labeluserinfo["text"] = "USER INFO:"
        self.labeluserinfo['bg'] = 'green'
        self.labeluserinfo['fg'] = 'white'
        self.labeluserinfo.grid(row=3, column=3, sticky=tk.E)
        self.userinfo = tk.Entry(self.frame_speechRec)
        self.userinfo['bg'] = 'green'
        self.userinfo['fg'] = 'white'
        self.userinfo.grid(row = 3,column = 4,sticky = tk.W)





        # self.samplerate["command"] = self.getsample


        self.quit = tk.Button(self.frame_speechRec, text="QUIT", bg = 'green',fg="red",
                              command=root.destroy)
        self.quit.grid(row = 4,column = 0,sticky = tk.W)

    # def say_hi(self):
    #     print("hi there, everyone!")
    def settextlabel1(self,event):
        self.rate.set("采样率："+str(self.samplerate.get(self.samplerate.curselection())))
    def open_file(self):
        self.filename.set(tkinter.filedialog.askopenfilename())
    def changeWordstate(self):
        self.state = 1
    def changeSpeechstate(self):
        self.state = 0
    def changeImagestate(self):
        self.state = 2
    def rec(self):
        if self.state == 0:
            self.speech_rec()
        elif self.state == 1:
            self.word_rec()
        elif self.state == 2:
            self.facereg()

    def word_rec(self):
        self.result.set("State:" + "正忙")
        APP_ID = '11702208'
        API_KEY = 'A2PICecu9tMyZcHb773oFqWf'
        SECRET_KEY = '1Pld9D8Ubbbvv7Xaxeg65iK91UAZUKwj '
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        """ 读取图片 """

        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        image = get_file_content(self.filename.get())

        """ 调用通用文字识别, 图片参数为本地图片 """

        """ 调用通用文字识别（含生僻字版）, 图片参数为本地图片 """
        client.enhancedGeneral(image)

        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        """ 带参数调用通用文字识别（含生僻字版）, 图片参数为本地图片 """
        temp1 = client.basicGeneral(image, options)
        if temp1["words_result_num"] > 1:
            self.result.set('State: success')
        else:
            self.result.set('State:' + '因为某种原因未能识别出文字')
        with open("res.txt", 'w') as file:
            for item in temp1['words_result']:
                file.write(item['words'])
                file.write('\t')
                file.write(str(item['probability']['average']))
                file.write('\r\n')


    def speech_rec(self):
        # 识别本地文件
        self.result.set("State:"+"正忙")
        APP_ID = '11388941'
        API_KEY = '0ZYGXXiNUMXDalelafeEL0GW'
        SECRET_KEY = 'VmTREEGWKm4V0DPAyQLfuEwhwISZoXx6 '
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        temp1 = client.asr(get_file_content(self.filename.get()), format='wav', rate=self.samplerate.get(self.samplerate.curselection()), options={
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
    def facereg(self):
        self.result.set("State:" + "正忙")
        client = function.faceinit()
        data = function.get_file_content(self.filename.get())
        imagetype = "BASE64"
        groupId = "group1"
        userId = self.userid.get()
        options = {}
        options["user_info"] = self.userinfo.get()
        options["quality_control"] = "NORMAL"
        options["liveness_control"] = "LOW"
        res = client.addUser(data,imagetype,groupId,userId,options)
        self.result.set("State:" + res['error_msg'])



root = tk.Tk()
root.title("Baidu API")
root.geometry("550x550")
root.iconbitmap('bitbug_favicon.ico')
app = Application(master=root)
app.mainloop()