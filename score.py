import csv
from tkinter import *


tk=Tk()

x_count=0
o_count=0
d_count=0


with open('winner.csv', 'r') as csvfile:
     spamreader = csv.reader(csvfile)
     for row in spamreader:
        if row=='X':
            x_count=x_count+1
        elif row=='O':
            o_count=o_count+1
        else:
            d_count=d_count+1


x = Label(tk, text=x_count)
x.pack()

o = Label(tk, text=o_count)
o.pack()

d = Label(tk, text=d_count)
d.pack()        


tk.mainloop()

