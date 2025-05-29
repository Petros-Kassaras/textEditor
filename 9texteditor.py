from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename , asksaveasfilename

def openfile ():
    filepath=askopenfilename(filetypes = [("Text files",".txt"),("All files","*.*")])
    if not filepath:
        return
    txtEdit.delete(1.0, END)
    with open(filepath, "r")as input_file:
        text = input_file.read()
        txtEdit.insert(1.0,text)
        screen.title(F"Simple text editor - {filepath}")

def savefile ():
    filepath=asksaveasfilename(defaultextension = "docx",filetypes =[("Text files",".txt"),("All files","*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txtEdit.get(1.0,END)
        output_file.write(text)
        screen.title(F"Simple text editor - {filepath}")

def clearfile ():
    txtEdit.delete(1.0 , END)

def exitfile():
    screen.destroy()

def dark():
    dn= darkmode.get()
    if dn==1:
        txtEdit.config(bg='black',fg='white')
    elif dn==0 :
        txtEdit.config(bg='white', fg='black')
    else :
        messagebox.showerror()



def about():
   messagebox.showinfo("idk","I do not know what to write")

screen = Tk() #dimiourgia othonis
screen.title("Parathyro") #titlos
screen.rowconfigure(0,minsize=800,weight=1)
screen.columnconfigure(1,minsize=800,weight=1)
screen.geometry('1000x700')#parathyro meget

menubar = Menu(screen)

file = Menu(menubar)
file.add_command(label = "Open",command=openfile)
menubar.add_cascade(label="File",menu=file)
file.add_command(label = "Save As",command=savefile)
file.add_command(label = "Exit",command=exitfile)
file.add_command(label = "Clear",command=clearfile)

darkmode= BooleanVar()
darkmode.set(False)
view = Menu(menubar)
view.add_checkbutton(label = "Dark Mode",onvalue=1,offvalue=0,variable=darkmode,command=dark)
menubar.add_cascade(label="View",menu=view)

help = Menu(menubar)
help.add_command(label = "about",command=about)
menubar.add_cascade(label="Help",menu=help)

txtEdit = Text(screen)
txtEdit.grid(row=0,column=1,sticky="nsew")




screen.config(menu=menubar)
screen.mainloop() #kleinei programma