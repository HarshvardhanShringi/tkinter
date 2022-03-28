import tkinter
from tkinter import IntVar
from tkinter import font
from tkinter import filedialog



# main window
m=tkinter.Tk()
m.geometry('1600x1000')
m.title('practise')


# buttons
but=tkinter.Button(m,activebackground='cyan',text='Start',command=isbutton_checked,width=14,height=1,font=15,bd=6,bg='white')
but.pack(side='bottom',pady=150)
but2=tkinter.Button(m,activebackground='cyan',command=openfile,text='select file',width=14,height=1,font=10,bd=2,bg='white')
but2.pack(side='top',pady=60,padx=30)

# entry
namvar=tkinter.StringVar()

entry=tkinter.Entry(m,width=30,textvariable=namvar)
entry.pack(side='bottom',pady=0)


# checkbutton
CheckVar1 = IntVar()
CheckVar2 = IntVar()
myFont = font.Font(size=12)
C1 = tkinter.Checkbutton(m, text = "Decryption", variable = CheckVar1,offvalue=0,onvalue=1, height=0,width = 20,font=myFont)
C2 = tkinter.Checkbutton(m, text = "Encryption", variable = CheckVar2,offvalue=0,onvalue=1, height=0,width = 20,font=myFont)
C1.pack(side='bottom',pady=60)
C2.pack(side='bottom',pady=0)




m.mainloop()
