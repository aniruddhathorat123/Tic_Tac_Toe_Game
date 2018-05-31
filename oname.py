from tkinter import *
from tkinter import messagebox
#from main import o_name

o_name=""
tk=Tk()
tk.title("player O Name")

def submit():
    global o_name
    o_name = tbox.get("1.0",'end-1c')
    if o_name=="":
        messagebox.showerror("Name Error","Enter valid name")

    else:
        tk.destroy()
        import Tic_server
        
        

tbox = Text(tk,font=('Times 15 bold'), height=2, width=30)
tbox.pack()

button1=Button(tk,text="Submit",font=('Times 15 bold'),height=1,width=6,command=lambda:submit())
button1.pack()


#tk.mainloop()