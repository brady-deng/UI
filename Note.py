import pymongo
import tkinter as tk
from urllib.parse import quote_plus

class application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.initvars()
        self.initwidgetlogin()
    def initvars(self):
        self.username = ''
        self.password = ''
        self.labelcache = []
        self.labelind = []
        self.contentind = []
        self.barind = []
        self.flagcache = []
        self.finditem = 8012
        self.state = tk.StringVar()
        self.rowcount = 3
        self.itemcount = 1
        self.labelcount = 0
        self.contentcount = 0
        self.state.set('Wait...')
        self.collection = tk.StringVar()
    def initwidgetlogin(self):
        self.login = tk.Frame()
        self.labelname = tk.Label(self.login,text = 'User:')
        self.labelname.grid(row = 0,column = 0,sticky = tk.W)
        self.entryname = tk.Entry(self.login)
        self.entryname.grid(row = 0,column = 1,sticky = tk.W)
        self.labelpas = tk.Label(self.login,text = 'PassWord:')
        self.labelpas.grid(row = 1,column = 0,sticky = tk.W)
        self.entrypas = tk.Entry(self.login,show = '*')
        self.entrypas.grid(row = 1, column = 1, sticky = tk.W)
        self.entryip = tk.Entry(self.login)
        self.entryip.grid(row = 2,column = 1,sticky = tk.W)
        self.labelstate = tk.Label(self.login,text = 'State:')
        self.labelstate.grid(row = 1,column = 2,sticky = tk.W)
        self.labelstate2 = tk.Label(self.login,textvariable = self.state)
        self.labelstate2.grid(row = 1,column = 3,sticky = tk.W)
        self.buttonlog = tk.Button(self.login,text = 'Connect',command = self.connectmongo)
        self.buttonlog.grid(row = 0,column = 2,sticky = tk.W)
        self.buttonsign = tk.Button(self.login,text = 'Sign up',command = self.sign)
        self.buttonsign.grid(row = 0,column = 3,sticky = tk.W)
        self.labelip = tk.Label(self.login,text = 'IP')
        self.labelip.grid(row = 2,column = 0,sticky = tk.W)

        self.login.grid(row = 0,sticky = tk.S)
    def sign(self):
        self.signup = tk.Toplevel()
        # self.signup.geometry('400x200')
        # dia.geometry('800x800')
        self.labelsignuser = tk.Label(self.signup,text = 'username')
        self.labelsignuser.grid(row = 0,column = 0,sticky = tk.W)
        self.entrysignuser = tk.Entry(self.signup)
        self.entrysignuser.grid(row = 0,column = 1,sticky = tk.W)
        self.labelsignpsd = tk.Label(self.signup,text = 'password')
        self.labelsignpsd.grid(row = 1,column = 0, sticky = tk.W)
        self.entrysignpsd = tk.Entry(self.signup)
        self.entrysignpsd.grid(row = 1,column = 1, sticky = tk.W)
        self.buttonsignup = tk.Button(self.signup,text = 'register',command = self.registeruser)
        self.buttonsignup.grid(row=0, column=2, sticky=tk.W)
        self.labelseip = tk.Label(self.signup,text = 'IP')
        self.labelseip.grid(row = 2, column = 0, sticky = tk.W)
        self.entryseip = tk.Entry(self.signup)
        self.entryseip.grid(row = 2, column = 1, sticky = tk.W)
        self.labelsignstate = tk.Label(self.signup,text = 'State:')
        self.labelsignstate.grid(row = 1,column = 2, sticky = tk.W)
        self.labelsignstate2 = tk.Label(self.signup,textvariable = self.state)
        self.labelsignstate2.grid(row = 2,column = 2,sticky = tk.W)

    def registeruser(self):
        self.signuser = self.entrysignuser.get()
        self.signpsd = self.entrysignpsd.get()
        self.seip = self.entryseip.get()
        self.client = pymongo.MongoClient(self.seip,27017)

        try:
            # self.dbadmin = self.client['admin']
            # self.dbadmin.authenticate("admin","2672411561")
            self.db = self.client['admin']
            self.db.authenticate('root','2672411561')
            self.db = self.client[self.signuser]
            self.db.command("createUser",self.signuser,pwd = self.signpsd,roles = ['readWrite'])
            self.state.set('Success!')
        except:
            self.state.set('Fail')


    def initwidgetfunction(self):
        self.login.destroy()
        dia.geometry("800x1100")
        self.function = tk.Frame()
        self.collention = self.db.list_collection_names()
        self.collection.set(self.collention)
        self.labeldate = tk.Label(self.function,text = 'Date:(example20180914)',width = 20)
        self.labeldate.grid(row = 0,column = 0,sticky = tk.W)
        self.entrydate = tk.Entry(self.function,width = 20)
        self.entrydate.grid(row = 0,column = 1,sticky = tk.W)
        self.labelcol = tk.Label(self.function,text = 'Collections:')
        self.labelcol.grid(row = 2,column = 0,sticky = tk.W)


        self.listscroll = tk.Scrollbar(self.function)
        self.listscroll.grid(row = 2,column = 2,sticky = tk.W)
        self.listboxcol = tk.Listbox(self.function,width = 20,height = 2,listvariable = self.collection,yscrollcommand = self.listscroll.set)
        self.listscroll.config(command  = self.listboxcol.yview)
        self.listboxcol.grid(row = 2,column = 1,sticky = tk.W)


        self.buttonlabelin = tk.Button(self.function,text = 'Insert Label',command = self.insertlabel,width = 12)
        self.buttonlabelin.grid(row = 0,column = 2,sticky = tk.W)
        self.buttoncontentin = tk.Button(self.function,text = 'Insert Content',command = self.insertcontent,width = 12)
        self.buttoncontentin.grid(row = 0, column = 3, sticky = tk.W)
        self.buttondate = tk.Button(self.function, text='Insert',command = self.insert,width = 20)
        self.buttondate.grid(row=1, column=0, sticky=tk.W)
        self.buttonback = tk.Button(self.function, text='Back', command= self.back, width=20)
        self.buttonback.grid(row=1, column=1, sticky=tk.W)
        self.labelstatef = tk.Label(self.function,text = 'State:')
        self.labelstatef.grid(row = 0, column = 4,sticky = tk.W)
        self.labelstatef2 = tk.Label(self.function,textvariable = self.state)
        self.labelstatef2.grid(row = 0, column = 5,sticky =tk.W)
        self.function.grid(row=1, sticky=tk.S)
        # self.entryfind = tk.Entry(self.function,width = 10)
        # self.entryfind.grid(row = 1,column = 2,sticky = tk.W)
        self.buttonfind = tk.Button(self.function,text = 'Find by date:',command = self.find,width = 12)
        self.buttonfind.grid(row = 1, column = 2, sticky = tk.W)

        self.buttonexport = tk.Button(self.function,text = 'Export',command = self.export,width = 12)
        self.buttonexport.grid(row = 1,column = 3,sticky = tk.W)
        self.buttonfile = tk.Button(self.function,text = 'New file', command = self.createfile)
        self.buttonfile.grid(row = 1,column = 4,sticky = tk.W)
        self.entryfile = tk.Entry(self.function)
        self.entryfile.grid(row = 1,column = 5,sticky = tk.W)
    def createfile(self):

        filename = self.entryfile.get()
        self.file = self.db[filename]
        self.collention = self.db.list_collection_names()
        if filename in self.collention:
            self.state.set('the file already exists')
        else:
            self.collention.append(filename)
            self.collection.set(self.collention)
            count = len(self.collention)
            self.listboxcol.selection_anchor(count-1)
            self.state.set('Success')

        # self.state.set('something went wrong!')

    def find(self):
        tempdate = int(self.entrydate.get())
        temp = list(self.collection.find())
        tempflag = 0
        for i in range(len(temp)):
            if tempdate == temp[i]['Date']:
                tempflag = 1
                tempind = i
                break
        if tempflag == 1:
            self.state.set("The item is at location: " + str(tempind))
            self.finditem = tempind
        else:
            self.state.set("Not found")

    def export(self):
        temp = list(self.collection.find())
        header = []
        cache = []
        if self.finditem == 8012:
            for item in temp:
                del(item["_id"])
                cache.append(item)
        else:
            del(temp[self.finditem]["_id"])
            cache.append(temp[self.finditem])
        # for item in list(cache[0].keys()):
        #     header.append(item)
        file = open("res.txt", "w")
        for i in range(len(cache)):
            for item in list(cache[i].keys()):
                file.write(item+':')
                if item == 'Date':
                    if type(cache[i][item]) != str:
                        file.write(str(cache[i][item]))
                    else:
                        file.write(cache[i][item])
                else:
                    file.write('\r\n')
                    if type(cache[i][item]) != str:
                        file.write(str(cache[i][item]))
                    else:
                        file.write(cache[i][item])
                file.write('\r\n')
        # for item in header:
        #     file.write(item)
        #     file.write('\t\t\t')
        # file.write('\r\n')
        # for item in cache:
        #     for head in header:
        #         file.write(str(item[head]))
        #         file.write('\t\t\t')
        #     file.write('\r\n')
    def connectmongo(self):
        self.username = self.entryname.get()
        self.password = self.entrypas.get()
        self.host = self.entryip.get()
        # ipnum = 1
        # uri = "mongodb://%s:%s@%s" % (quote_plus(self.username),quote_plus(self.password),self.host)
        if len(self.username)<1 or len(self.password)<1:
            self.state.set("The username or password can't be blank")
        else:

            try:
                # self.host = self.host+str(ipnum)
                self.client = pymongo.MongoClient(self.host,27017)
                if self.username == 'tingo':
                    self.db = self.client['test']

                else:
                    self.db = self.client[self.username]
                self.db.authenticate(self.username,self.password)
                # self.collection = self.db[str(self.data["Date"])]
                # self.collection = self.db['noteex']
                # self.collection.find().count()

                self.state.set("Connected")
                self.initwidgetfunction()
            except:
                self.state.set("Wrong user or password!")



    def insert(self):
        filename = self.listboxcol.selection_get()
        self.file = self.db[filename]
        self.predata()
        # self.db = self.client['test']
        # # self.collection = self.db[str(self.data["Date"])]
        # self.collection = self.db['noteex']
        temp = self.file.find()
        tempflag = 0
        for item in temp:
            # tempcount = 1
            # tempname2 = "Content"+str(tempcount)
            # tempcount+=1
            if self.data['Date'] == item['Date']:
                tempflag = 1
                break
        if tempflag == 0:
            try:
                self.file.insert_one(self.data)
                self.state.set("Inserted")
            except:
                self.state.set('Something went wrong!')
        else:
            self.state.set('The Date already exists, only the content will be input into the dbs')
            tempdate = self.data['Date']
            del(self.data['Date'])
            # del(tempdata['Date'])
            try:
                self.file.update_one({"Date":tempdate},{'$addToSet':self.data},True,False)
                self.state.set('Updated')
            except:
                self.state.set('Something went wrong!')

    def predata(self):
        self.data = {}
        temp = list(self.file.find())
        self.itemcount = len(temp) + 1
        # tempname = "Content"+str(self.itemcount)
        # self.data.setdefault(tempname,{})
        self.data.setdefault("Date",int(self.entrydate.get()))
        # self.data.setdefault("SubContent",[])
        tempdic = {}
        for i in range(self.labelcount):
            self.data.setdefault(self.labelind[i].get(),[self.contentind[i].get("0.0","end")])
            # tempdic.setdefault(self.labelind[i].get(),self.contentind[i].get("0.0","end"))
        # self.data.setdefault("Content",tempdic)
        # self.data[tempname].setdefault("SubContent",[])
        # self.data[tempname]["SubContent"].append([tempdic])
        # temparg = tempname+".Date"
        # return tempname
        # self.db = self.client['test']
        # self.collection = self.db[self.data["Date"]]

    def insertlabel(self):
        self.labelcount += 1
        labelname = 'Label'+str(self.rowcount)
        self.labelcache.append(tk.Label(self.function,text = labelname))
        self.labelcache[self.rowcount - 3].grid(row = self.rowcount,column = 0,sticky = tk.W)
        self.labelind.append(tk.Entry(self.function))
        self.labelind[self.labelcount-1].grid(row = self.rowcount,column = 1,sticky = tk.W)
        self.rowcount = self.rowcount+1
        self.flagcache.append(0)


        # self.buttondate.grid(row=self.rowcount, column=0, sticky=tk.W)
        # self.labelstatef.grid(row=self.rowcount, column=1, sticky=tk.W)
        # self.labelstatef2.grid(row=self.rowcount, column=2, sticky=tk.W)
    def insertcontent(self):
        self.contentcount+=1
        labelname = 'Content' + str(self.rowcount)
        self.labelcache.append(tk.Label(self.function, text=labelname))
        self.labelcache[self.rowcount-3].grid(row=self.rowcount, column=0, sticky=tk.W)
        self.barind.append(tk.Scrollbar(self.function))
        self.barind[self.contentcount-1].grid(row = self.rowcount,column = 2,sticky = tk.W)
        self.contentind.append(tk.Text(self.function,width = 20,height = 10,yscrollcommand = \
                                       self.barind[self.contentcount-1].set))
        self.barind[self.contentcount-1].config(command = self.contentind[self.contentcount-1].yview)
        self.contentind[self.contentcount - 1].grid(row=self.rowcount, column=1, sticky=tk.W)
        self.rowcount = self.rowcount + 1
        self.flagcache.append(1)

        # self.buttondate.grid(row=self.rowcount, column=0, sticky=tk.W)
        # self.labelstatef.grid(row=self.rowcount, column=1, sticky=tk.W)
        # self.labelstatef2.grid(row=self.rowcount, column=2, sticky=tk.W)
    def back(self):
        if self.rowcount>3:
            if self.flagcache[-1] == 0:
                self.rowcount-=1
                self.labelcount-=1
                self.labelind[-1].destroy()
                del(self.labelind[-1])
                del(self.flagcache[-1])

            else:
                self.rowcount -= 1
                self.contentcount -= 1
                self.contentind[-1].destroy()
                self.barind[-1].destroy()
                del (self.contentind[-1])
                del (self.flagcache[-1])
                del (self.barind[-1])
            self.labelcache[-1].destroy()
            del(self.labelcache[-1])
        else:
            return 0





if __name__ == "__main__":
    dia = tk.Tk()
    dia.geometry("500x400")
    application(dia)
    dia.mainloop()
