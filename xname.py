from tkinter import *
from tkinter import messagebox
#from main import x_name

tk=Tk()
x_name=""
tk.title("player X Name")

def submit():
    global x_name
    try:
        x_name = tbox.get("1.0",'end-1c')
        if x_name=="":
            messagebox.showerror("Name Error","Enter valid name")
    
        else:
            tk.destroy()
            import Tic_client
    except:
        messagebox.showerror("Error", "First start the Server")
        
        

tbox = Text(tk,font=('Times 15 bold'), height=2, width=30)
tbox.pack()

button1=Button(tk,text="Submit",font=('Times 15 bold'),height=1,width=6,command=lambda:submit())
button1.pack()


#tk.mainloop()