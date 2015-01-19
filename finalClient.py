import socket
import threading
import time
import thread
from Tkinter import *


tLock = threading.Lock()
shutdown = False

username = ""

host = '127.0.0.1'
port = 0
server = ('127.0.0.1',5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
#s.setblocking(0)
    


def receiving(name,s):
     
    #while not shutdown:
    print "thread called"
    while not shutdown:
            print "inside while"
            try:
                data,addr = s.recvfrom(1024)
                print data, "client data"
                printotherText(data)
                print data
            except:
                print "passing"
                pass
               
              
             

     
#def Main():
 #   setServer()
  #  Login()
   # SendMessage()
    #shudown = True
    #s.close()
    
def Login(uid,fid):
    #print "Enter the userid - should be 6 characters"
    #global uid
    #uid = raw_input()
    #s.sendto("lOgiNu" + uid,server)
    #print "Chat with a friend?"
    #ans = raw_input()
    #global fid
   
    #if ans == 'y':
     #   print "enter your friend's id (6 chars)"
        #fid = raw_input()
    #else:
     #   fid = ""
    print "iam here" ,uid ,fid
    s.sendto("lOgiNu" + uid + fid,server)
    print "lOgiNu" + uid + fid
    
        

def sendMessage(message):
    #message = raw_input(uid + "-> ")
    #while message != 'Quit':
     #   if message != '':
        global username
        s.sendto(username + message, server)
            
        #rT = threading.Thread(target=receving, args=("RecvThread",s))
        #rT.start()
        #time.sleep(0.2)
        #tLock.acquire()
        #message = raw_input(uid + "-> ")
        #tLock.release()


## Graphics

 #Create a Main window for the application
app = Tk()
app.title("Chat Application")
app.geometry("400x600")
app.resizable(width=FALSE, height=FALSE)

#Define functions for click events
def btnsendClicked():
    EntryText = Msgwin.get("0.0",END)
    printuserText(EntryText)
    sendMessage(EntryText)

def printuserText(EntryText):
    if EntryText != '':
        Chatwin.config(state=NORMAL)
        if Chatwin.index('end') != None:
            LineNumber = float(Chatwin.index('end'))-1.0
            Chatwin.insert(END, "You: " + EntryText)
            Chatwin.tag_add("You", LineNumber, LineNumber+0.4)
            Chatwin.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            Chatwin.config(state=DISABLED)
            Chatwin.yview(END)
            Msgwin.delete("0.0",END)

def printotherText(EntryText):
    if EntryText != '':
        Chatwin.config(state=NORMAL)
        if Chatwin.index('end') != None:
            try:
                LineNumber = float(Chatwin.index('end'))-1.0
            except:
                pass
            Chatwin.insert(END, "Other: " + EntryText)
            Chatwin.tag_add("Other", LineNumber, LineNumber+0.6)
            Chatwin.tag_config("Other", foreground="#04B404", font=("Arial", 12, "bold"))
            Chatwin.config(state=DISABLED)
            Chatwin.yview(END)

def btnresetClicked():
    Msgwin.delete("0.0",END)

def btnLoginClicked():
    global username
    
    username = txtusername.get("0.0",END)
    print username
    friend = txtconnect.get("0.0",END)
    username = username.strip('\n')
    friend = friend.strip('\n')
    Login(username,friend)
    print username,friend
    #Check if login is success. Then Disable the controls.
    txtusername.config(state=DISABLED)
    txtconnect.config(state=DISABLED)

def FilterText(EntryText):
    EndFiltered = ''
    for i in range(len(EntryText)-1,-1,-1):
        if EntryText[i]!='\n':
            EndFiltered = EntryText[0:i+1]
            break
    for i in range(0,len(EndFiltered), 1):
            if EndFiltered[i] != "\n":
                    return EndFiltered[i:]+'\n'
    return ''

#Create controls and place them in the window    
menubar = Menu(app)
Loginmenu = Menu(menubar,tearoff=0)
Loginmenu.add_command(label="Exit", command=app.destroy)
Loginmenu.add_separator()
menubar.add_cascade(label="Quit",menu=Loginmenu)
app.config(menu=menubar)

lblname = Label(app,bd=0,font = "Arial",text = "Username",pady=16)
lblname.place(x=6,y=0,height=47,width=100)

txtusername = Text(app,bd=5,bg="white",font = "Arial",relief ="groove")
txtusername.place(x=112,y=12,height=27,width=100)


lblname = Label(app,bd=0,font = "Arial",text = "Connect to",pady=16)
lblname.place(x=6,y=40,height=47,width=100)

txtconnect = Text(app,bd=5,bg="white",font = "Arial",relief ="groove")
txtconnect.place(x=112,y=52,height=27,width=100)

btnLogin = Button(app, font=16, text="Login", width="35", height=40,
                    bd=5, bg="#CCCCB2", activebackground="#CCCCB2",relief = "raised",command = btnLoginClicked)
btnLogin.place(x=240,y=30,height = 27,width = 75)

Chatwin = Text(app,bd=5,bg="white",height ="10",width = "50", font = "Arial",relief ="groove")
Chatwin.config(state=DISABLED)
Chatwin.place(x=6,y=91, height=385, width=388)

Msgwin = Text(app,bd=5,bg="white",height ="10",width = "50", font = "Arial",relief = "ridge")
Msgwin.place(x=6,y=497,height=97,width = 304)

btnsend = Button(app, font=16, text="Send", width="35", height=40,
                    bd=5, bg="#33D633", activebackground="#00A300",relief = "raised", command = btnsendClicked)
btnsend.place(x=322,y=497,height = 46,width = 78)

btnreset = Button(app, font=16, text="Clear\n Text", width="35", height=40,
                    bd=5, bg="#FF1919", activebackground="#FF4D4D",relief = "raised", command = btnresetClicked)
btnreset.place(x=322,y=549,height = 45,width = 78)

scrollbar1 = Scrollbar(app, command=Chatwin.yview, cursor="heart", relief = "groove")
Chatwin['yscrollcommand'] = scrollbar1.set
scrollbar1.place(x=378,y=92, height=381)

scrollbar2 = Scrollbar(app, command=Msgwin.yview, cursor="heart", relief = "ridge")
Msgwin['yscrollcommand'] = scrollbar2.set
scrollbar2.place(x=302,y=500, height=94)

rT = threading.Thread(target=receiving, args=("RecvThread",s))
rT.start()

#thread.start_new_thread(receiving,())
#Starts the application's mainloop,waiting for mouse and keyboard events
app.mainloop()

shutdown = True


