from tkinter import *
root=Tk()
nameofui = Label(root,text="first ui")
nameofui.pack()
btn=Button(root,text="stop",command=root.destroy)
btn.pack()
root.mainloop()