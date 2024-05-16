from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(Screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error")
                Screen.update()    
        scvalue.set(value)
        Screen.update()    
    elif text == "C":
        scvalue.set("")
        Screen.upadate()
    else:
        scvalue.set(scvalue.get()+ text)
        Screen.update()
root=Tk()

root.geometry("644x9700")
root.title("My Calculator")

scvalue=StringVar()
scvalue.set("")
Screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
Screen.pack(fill=X, ipadx=8,pady=10, padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=24, pady=18, font="lucida 34 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=24, pady=18, font="lucida 34 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="5",padx=24, pady=18, font="lucida 34 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=24, pady=18, font="lucida 34 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="1",padx=24, pady=18, font="lucida 36 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=24, pady=18, font="lucida 40 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=24, pady=18, font="lucida 40 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=24, pady=18, font="lucida 35 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="C",padx=24, pady=18, font="lucida 34 bold")
b.pack(side=LEFT,padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()


f.pack()

root.mainloop()