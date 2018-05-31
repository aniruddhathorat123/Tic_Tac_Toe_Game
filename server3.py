from tkinter import *
from tkinter import messagebox
import socket
from _overlapped import NULL

tk=Tk()
tk.title("Tic tac Toe Server")
click=True
cycle=False
choice=0
s=NULL
conn=NULL
addr=NULL
host = socket.gethostname() 
port = 4000


def create():
    global s,conn,addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    s.listen(9) 
    conn, addr = s.accept()

def recvi():
    global click,s,conn,addr
    create()
    data = conn.recv(1024)
    data1=int.from_bytes(data, byteorder='big')
    click=True
    print("data=",data1)
    s.close()
    conn.close()
    recv_click(data1)    


def OnButtonClick(buttons):    
    global click,s,conn,addr
    if buttons["text"]=="1" and click==True:
        button1["text"]="O"
        click=False 
        choice = 1
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()    
        
    elif buttons["text"]=="2" and click==True:
        button2["text"]="O"
        click=False 
        choice = 2
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
            
    elif buttons["text"]=="3" and click==True:
        button3["text"]="O"
        click=False 
        choice = 3
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="4" and click==True:
        button4["text"]="O"
        click=False 
        choice = 4
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="5" and click==True:
        button5["text"]="O"
        click=False 
        choice = 5
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="6" and click==True:
        button6["text"]="O"
        click=False 
        choice = 6
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="7" and click==True:
        button7["text"]="O"
        click=False 
        choice = 7
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="8" and click==True:
        button8["text"]="O"
        click=False 
        choice = 8
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    elif buttons["text"]=="9" and click==True:
        button9["text"]="O"
        click=False 
        choice = 9
        create()
        conn.send(bytes([choice]))
        checker()
        conn.close()
        s.close()
        recvi()
        
    

def recv_click(buttons):    
    
    if buttons == 1 and button1["text"]=="1":
        button1["text"]="X" 
        
    elif buttons == 2 and button2["text"]=="2":
        button2["text"]="X"
            
    elif buttons == 3 and button3["text"]=="3":
        button3["text"]="X"
        
    elif buttons == 4 and button4["text"]=="4":
        button4["text"]="X"
        
    elif buttons == 5 and button5["text"]=="5":
        button5["text"]="X"
        
    elif buttons == 6 and button6["text"]=="6":
        button6["text"]="X"
        
    elif buttons == 7 and button7["text"]=="7":
        button7["text"]="X"
        
    elif buttons == 8 and button8["text"]=="8":
        button8["text"]="X"
        
    elif buttons == 9 and button9["text"]=="9":
        button9["text"]="X"
        


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
            button1["text"]="1" 
            button2["text"]="2" 
            button3["text"]="3" 
            button4["text"]="4" 
            button5["text"]="5" 
            button6["text"]="6" 
            button7["text"]="7" 
            button8["text"]="8" 
            button9["text"]="9"
            s.close() 
            
    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
         button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
         button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
         button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
         button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or
         button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" ):
            messagebox.showinfo("Winner is O","Player O won")
            button1["text"]="1"  
            button2["text"]="2" 
            button3["text"]="3" 
            button4["text"]="4" 
            button5["text"]="5" 
            button6["text"]="6" 
            button7["text"]="7" 
            button8["text"]="8" 
            button9["text"]="9"
            s.close()
                         
    elif(button1["text"]!="1" and button2["text"]!="2" and button3["text"]!="3" and button4["text"]!="4" and button5["text"]!="5"
          and button6["text"]!="6" and button7["text"]!="7" and button8["text"]!="8" and button9["text"]!="9" ):
            messagebox.showinfo("Draw","Match Draw...!!\nPlay Again") 
            button1["text"]="1" 
            button2["text"]="2" 
            button3["text"]="3" 
            button4["text"]="4" 
            button5["text"]="5" 
            button6["text"]="6" 
            button7["text"]="7" 
            button8["text"]="8" 
            button9["text"]="9" 
            s.close()
        


buttons=StringVar()

button1=Button(tk,text="1",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button1))
button1.grid(row=1,column=0)
         
button2=Button(tk,text="2",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button2))
button2.grid(row=1,column=1)

button3=Button(tk,text="3",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button3))
button3.grid(row=1,column=2)

button4=Button(tk,text="4",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button4))
button4.grid(row=2,column=0)

button5=Button(tk,text="5",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button5))
button5.grid(row=2,column=1)

button6=Button(tk,text="6",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button6))
button6.grid(row=2,column=2)

button7=Button(tk,text="7",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button7))
button7.grid(row=3,column=0)

button8=Button(tk,text="8",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button8))
button8.grid(row=3,column=1)

button9=Button(tk,text="9",font=('Times 26 bold'),height=4,width=8,command=lambda:OnButtonClick(button9))
button9.grid(row=3,column=2)


recvi()


tk.mainloop()