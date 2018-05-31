from tkinter import *
#from tkinter import messagebox
#from tkinter.scrolledtext import ScrolledText

tk=Tk()
tk.title("TictacToe")
tk.minsize(500, 250)
x_name=""
o_name=""

tk.title("Tic Tac Toe Zone")

def choose1():
    import Tic_single
def choose3():
    import Tic_server
def choose4():
    import Tic_client
def choose5():
    import score
    


button1=Button(tk,text="Single PC",font=('Times 15 bold'),height=2,width=20,command=lambda:choose1())
button1.pack()

button2=Button(tk,text="Peer to Peer",font=('Times 15 bold'),height=2,width=20,state=DISABLED,command=False)
button2.pack()

button3=Button(tk,text="Start server",font=('Times 15 bold'),height=2,width=20,command=lambda:choose3())
button3.pack()

button4=Button(tk,text="Start client",font=('Times 15 bold'),height=2,width=20,command=lambda:choose4())
button4.pack()

button5=Button(tk,text="Show Score",font=('Times 15 bold'),height=2,width=20,command=lambda:choose5())
button5.pack()


tk.mainloop()