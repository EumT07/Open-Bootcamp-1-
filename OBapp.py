"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.

Position with Anchor
N   /S     /W   /E
top/bottom/left/right alignment.
"""
from tkinter import *

#Function show imagens
def showOption():
    lang = ""
    value = opcion.get()
    if(value == 1):
        lang += "javascript"
    elif(value == 2):
        lang += "java"
    elif(value == 3):
        lang += "php"
    elif(value == 4):
        lang += "c+"
    elif(value == 5):
        lang += "python"

    if(len(lang) == 0):
        showLangProgramming.config(text=f"Upss You need to choose first",font=("Arial bold", 10))
    else:
        showLangProgramming.config(text=f"Great {lang.upper()} is a good Programming Language",font=("Arial bold", 10))
    showImg1.destroy()
    showImg2.destroy()
   
def reset():
    opcion.set(None)
    showLangProgramming.config(text="")
    
#Root 
root = Tk()
#settings window
root.title("OpenBootcamp")
#image-ico
root.iconbitmap("OpenBootcamp.ico")
#Size
root.geometry("820x590")
#Background Color
root.config(bg="#2c2c2c", )
root.resizable(0,0)

# 1
# Frame --> Main question
frameCenter = Frame(root, bg="#2c2c2c")
frameCenter.grid(row=0,column=0,columnspan=3,sticky=N+S+W+E, padx=245, pady=20)

#Main Question: Label
qtlabel = Label(frameCenter, text="¿Cual es el Mejor Curso de OpenBootcamp?")
qtlabel.pack(anchor="center", padx=10, pady=4)
qtlabel.config(bg="#2c2c2c", fg="white", font=("Comic bold",12))

# 2
#RadioButton Options Frame
rbFrameLeft = Frame(root,bg="#2c2c2c")
rbFrameLeft.grid(row=1,column=0, padx=25, pady=10)

#Radiobuttoms
opcion = IntVar()
langCategories = LabelFrame(rbFrameLeft,text="Select Language",padx=60,pady=40)
langCategories.pack()
langCategories.config(bg="#2c2c2c",fg="White")

#radioButton Options:
# Javascript Icon 
img1r1 = PhotoImage(file="./img/javascript.png")
r1 = Radiobutton(langCategories,image=img1r1,text="Javascript",variable=opcion,value=1)
r1.pack(side="top")
r1.config(bg="#2c2c2c",fg="green")

# Java Icon 
img2r2 = PhotoImage(file="./img/java.png")
r2 = Radiobutton(langCategories,image=img2r2,text="Java",variable=opcion,value=2)
r2.pack(side="top")
r2.config(bg="#2c2c2c",fg="green")

# PHP Icon 
img3r3 = PhotoImage(file="./img/php.png")
r3 = Radiobutton(langCategories,image=img3r3,text="PHP",variable=opcion,value=3)
r3.pack(side="top")
r3.config(bg="#2c2c2c",fg="green")

# C+ Icon 
img4r4 = PhotoImage(file="./img/c+.png")
r4 = Radiobutton(langCategories,image = img4r4,text="C",variable=opcion,value=4)
r4.pack(side="top")
r4.config(bg="#2c2c2c",fg="green")

# Python Icon 
img5r5 = PhotoImage(file="./img/python.png")
r5 = Radiobutton(langCategories,image = img5r5,text="Python",variable=opcion,value=5)
r5.pack(anchor=W)
r5.config(bg="#2c2c2c",fg="green")

# 3
#Answer Place
answerframeRigth = Frame(root, bg="#2c2c2c")
answerframeRigth.grid(row=1,column=1,columnspan=3,padx=40, pady=20)

#Image ¿ : Question Mark
img1 = PhotoImage(file="./img/question1.png")
showImg1 = Label(answerframeRigth, image = img1)
showImg1.pack(side="left")
showImg1.config(bg="#2c2c2c")

#Image ? : Question Mark
img2 = PhotoImage(file="./img/question2.png")
showImg2 = Label(answerframeRigth, image = img2)
showImg2.pack(side="right")
showImg2.config(bg="#2c2c2c")

# Answer --> Place to show the Answer text about Programming languages
showLangProgramming = Label(answerframeRigth, width=40)
showLangProgramming.pack(side="top")
showLangProgramming.pack(side="right")
showLangProgramming.pack(side="bottom")
showLangProgramming.pack(side="left")
showLangProgramming.config(bg="#2c2c2c",fg="yellow")

# 4
#Button options Frame
frameBottom = Frame(root,bg="#2c2c2c")
frameBottom.grid(row=2,column=0, columnspan=3, sticky=N+S+W+E, padx=245, pady=30)

#Button to Choose
buttonChoose = Button(frameBottom, text="Choose", command=showOption)
buttonChoose.pack(side="left",padx=8)
buttonChoose.config(width=12, height=2,bg="#006400")

#Button to reset
buttonReset = Button(frameBottom, text="Reset", command=reset)
buttonReset.pack(side="right",padx=8)
buttonReset.config(width=12, height=2, bg="#FFD700")

#mainloop
root.mainloop()