from tkinter import *
from tkinter import ttk
import qrcode,random

def generate(*args):
    try:
        Data = str(data.get())
        Location = str(save_location.get())
        FName = str(random.randint(10000,99999))+'.png'
        img = qrcode.make(Data)
        type(img)
        img.save(Location+'/'+FName)

    except ValueError:
        pass

root = Tk()
root.geometry("500x300")
root.title("QR Code Generator")

pframe = ttk.Frame(root,height=450,width=600)
pframe.grid(column=0,row=0)

data = StringVar()
data_input = ttk.Entry(pframe,width=40,textvariable=data)
data_input.place(x=200,y=60)
Label(pframe,text="Input Data").place(x=60,y=60)

save_location = StringVar()
save_input = ttk.Entry(pframe,width=40,textvariable=save_location)
save_input.place(x=200,y=100)
ttk.Label(pframe,text="Save Location").place(x=60,y=100)

ttk.Button(pframe,text="Generate",command=generate,width=20).place(x=200,y=150)

root.mainloop()


