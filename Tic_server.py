from tkinter import *
from tkinter import messagebox
import csv
import socket

host = socket.gethostname() 
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port)) 
s.listen(1) 
conn, addr = s.accept()
choice=0


tk=Tk()
tk.title("Tic Tac Toe Server")
choice=0

def send():
    button11.config(state=NORMAL)
    global choice
    conn.send(bytes([choice]))
    checker()
    button10.config(state=DISABLED)
    
def disable_bt():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button11.config(state=DISABLED)
    

def enable_bt():
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)
        


def rec():
    button10.config(state=NORMAL)
    enable_bt()
    button11.config(state=DISABLED)
    recvi()
    

def recvi():
    global choice
    buttons = conn.recv(1024)
    buttons=int.from_bytes(buttons, byteorder='big')

    
    if buttons == 1:
        button1["text"]="X" 
        
    elif buttons == 2:
        button2["text"]="X"
            
    elif buttons == 3:
        button3["text"]="X"
        
    elif buttons == 4:
        button4["text"]="X"
        
    elif buttons == 5:
        button5["text"]="X"
        
    elif buttons == 6:
        button6["text"]="X"
        
    elif buttons == 7:
        button7["text"]="X"
        
    elif buttons == 8:
        button8["text"]="X"
        
    elif buttons == 9:
        button9["text"]="X" 
    
    checker()   

    

def OnButtonClick(buttons):    
    global click,choice
    if buttons["text"]=="1":
        button1["text"]="O"
        click=False 
        choice = 1
        disable_bt()
  
        
    elif buttons["text"]=="2":
        button2["text"]="O"
        click=False 
        choice = 2
        disable_bt()
        
            
    elif buttons["text"]=="3":
        button3["text"]="O"
        choice = 3
        disable_bt()
        
        
    elif buttons["text"]=="4":
        button4["text"]="O" 
        choice = 4
        disable_bt()
        
        
    elif buttons["text"]=="5":
        button5["text"]="O" 
        choice = 5
        disable_bt()
        
        
    elif buttons["text"]=="6":
        button6["text"]="O"
        choice = 6
        disable_bt()
        
        
    elif buttons["text"]=="7":
        button7["text"]="O"
        choice = 7
        disable_bt()
        
        
    elif buttons["text"]=="8":
        button8["text"]="O"
        choice = 8
        disable_bt()
        
        
    elif buttons["text"]=="9":
        button9["text"]="O"
        choice = 9
        disable_bt()
         
    else:
        messagebox.showerror("Oops.", "Move Alrady Played")      
    
        
def checker():
    
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
         button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
         button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
         button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
         button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
         button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
         button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or
         button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" ):
            messagebox.showinfo("Winner", "Player X Won")
            f=open('winner.csv','a')
            f.write('X\n')
            f.close()
            tk.destroy()
            
    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
         button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
         button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
         button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
         button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or
         button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" ):
            messagebox.showinfo("Winner is O","Player O won")
            f=open('winner.csv','a')
            f.write('O\n')
            f.close()
            tk.destroy()
                         
    elif(button1["text"]!="1" and button2["text"]!="2" and button3["text"]!="3" and button4["text"]!="4" and button5["text"]!="5"
          and button6["text"]!="6" and button7["text"]!="7" and button8["text"]!="8" and button9["text"]!="9" ):
            messagebox.showinfo("Draw","Match Draw...!!\nPlay Again") 
            f=open('winner.csv','a')
            f.write('Draw\n')
            f.close()
            tk.destroy()
            


button1=Button(tk,text="1",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button1))
button1.grid(row=1,column=0)
         
button2=Button(tk,text="2",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button2))
button2.grid(row=1,column=1)

button3=Button(tk,text="3",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button3))
button3.grid(row=1,column=2)

button4=Button(tk,text="4",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button4))
button4.grid(row=2,column=0)

button5=Button(tk,text="5",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button5))
button5.grid(row=2,column=1)

button6=Button(tk,text="6",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button6))
button6.grid(row=2,column=2)

button7=Button(tk,text="7",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button7))
button7.grid(row=3,column=0)

button8=Button(tk,text="8",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button8))
button8.grid(row=3,column=1)

button9=Button(tk,text="9",font=('Times 26 bold'),height=2,width=4,state=DISABLED,command=lambda:OnButtonClick(button9))
button9.grid(row=3,column=2)

button10=Button(tk,text="Send",font=('Times 15 bold'),height=1,width=6,state=DISABLED,command=lambda:send())
button10.grid(row=4,column=0)

button11=Button(tk,text="Received",font=('Times 15 bold'),height=1,width=6,command=lambda:rec())
button11.grid(row=4,column=2)




tk.mainloop()