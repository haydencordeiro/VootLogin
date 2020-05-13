import tkinter as tk
import os

def k():
  os.system("/home/hayden/try2.py")

price=['1','2','3']
root=tk.Tk()
root.minsize(600, 600)
root.configure(bg='#feeaeb')

button = tk.Button(root, 
                   text="Submit", 
                   fg="white",
                   command=k,bg='#2e3d80'
                   ).place(x=10,y=400,width=80,height=50)
root.mainloop()