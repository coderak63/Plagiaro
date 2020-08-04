from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from difflib import SequenceMatcher



def OpenFile1():
    global file1
    file1 = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")),title = "Choose a file.")
    inp1.delete(0,END)
    inp1.insert(0,file1)
    
def OpenFile2():
    global file2
    file2 = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")),title = "Choose a file.")
    inp2.delete(0,END)
    inp2.insert(0,file2)

def check():
    try:
        with open(inp1.get(),'r') as file_1,open(inp2.get(),'r') as file_2:
            file1_data = file_1.read()
            file2_data = file_2.read()
            similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
            lb1.config(text="Plagiarism Percentage: {} %".format(round(similarity_ratio*100,2)))
            if(similarity_ratio>=0.5):
                lb2.config(text="...Plagiarism Detected...",fg="red")
            else:
                lb2.config(text="Plagiarism not found.",fg="green")
    except:
        lb2.config(text="CHOOSE VALID FILES",fg="purple")

window = Tk()
window.geometry('400x400')

window.title("Plagiaro - A plagiarism checker app")

labelFrame1 = ttk.LabelFrame(window, text = "Select files")
labelFrame1.pack(fill="both",expand="yes")

inp1=Entry(labelFrame1,width=30)
inp1.pack(fill=X)

bt1=Button(labelFrame1,command=OpenFile1,text="Choose File 1",bg="grey",fg="white")
bt1.pack(pady=10)



inp2=Entry(labelFrame1,width=30)
inp2.pack(fill=X)

bt2=Button(labelFrame1,command=OpenFile2,text="Choose File 2",bg="grey",fg="white")
bt2.pack(pady=10)


check=Button(labelFrame1,command=check,text="Check Plagiarism",bg="green",fg="white")
check.pack(side=BOTTOM)

labelFrame2 = ttk.LabelFrame(window, text = "Results: ")
labelFrame2.pack(fill="both",expand="yes")


lb2=Label(labelFrame2,font=("times",12,"bold"))
lb2.pack(side=TOP,pady=10)

lb1=Label(labelFrame2,text="Plagiarism Percentage: ",font=("times",10,"bold"))
lb1.pack(side=LEFT)

build=Label(labelFrame2,text="Build by: coderak63",bg="cyan")
build.pack(side=BOTTOM,anchor=SE)


window.mainloop()