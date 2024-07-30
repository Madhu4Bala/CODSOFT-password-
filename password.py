from tkinter import*
import random,string


root = Tk()
root.geometry("400x280")
root.title("Password Generator")

#intro text
title = StringVar()
label = Label(root,textvariable=title).pack()
title.set("The Strength of password")

def selection():
    selection=choice.get()

choice=IntVar()
R1 = Radiobutton(root,text="POOR",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root,text="ADVANCED",variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice=Label(root)
labelchoice.pack()

lenlable=StringVar()
lenlable.set("Password length")
lentitle=Label(root,textvariable=lenlable).pack()


val=IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()

def calback():
    lsum.configtext=passgen()

passgenButton=Button(root,text="Generate password",bd=5,height=2,command=calback,pady=3)
passgenButton.pack()
password=str(calback)

lsum=Label(root,text="")
lsum.pack(side=BOTTOM)

    #logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="""'!@#$%^&*()_+-=|{}[]<>?/.,;"""
advance=poor+average+symbols

def passgen():

    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))
        
root.mainloop()



