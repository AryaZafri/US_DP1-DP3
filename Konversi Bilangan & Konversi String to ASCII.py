from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Aplikasi Konversi Bilangan & String to ASCII')
root.geometry('1250x710')

#====================variable====================
num=IntVar()
lblbinary=StringVar()
lbldecimal=StringVar()
lblhexa=StringVar()
lbloctal=StringVar()
lblstring=StringVar()
lblhasilascii=StringVar()

#===================functions=====================
def convert():
    if num.get()==0:
        messagebox.showerror('Error','Anda harus memasukkan angka untuk mengonversi')
    else:
        lblbinary.set(str(bin(num.get()))[2:])
        lbldecimal.set(str(num.get()))
        lblhexa.set(str(hex(num.get()))[2:])
        lbloctal.set(str(oct(num.get()))[2:])

def konversi_ascii():
    input_str = lblstring.get()
    ascii_list = []
    for char in input_str.split():
        for c in char:
            ascii_list.append(str(ord(c)))
    lblhasilascii.set(', '.join(ascii_list))


def clear():
    num.set(0)
    lblhexa.set('')
    lblbinary.set('')
    lbldecimal.set('')
    lbloctal.set('')
    lblstring.set('')
    lblhasilascii.set('')


def exit():
    if messagebox.askyesno('Exit','Apakah benar kamu ingin keluar?'):
        root.destroy()


Label(root,text='Aplikasi Konversi Bilangan & String to ASCII',font=('Nunito',30,'bold'),fg='blue').pack(pady=10)

n=Label(root,text='Masukan Angka',font='Nunito 20 bold')
n.place(x=300,y=150)
n_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=num)
n_txt.place(x=650,y=150)

b=Label(root,text='Biner',font='Nunito 20 bold')
b.place(x=300,y=200)
b_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lblbinary)
b_txt.place(x=650,y=200)

d=Label(root,text='Desimal',font='Nunito 20 bold')
d.place(x=300,y=250)
d_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lbldecimal)
d_txt.place(x=650,y=250)

h=Label(root,text='Hexadesimal',font='Nunito 20 bold')
h.place(x=300,y=300)
h_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lblhexa)
h_txt.place(x=650,y=300)

o=Label(root,text='Oktal',font='Nunito 20 bold')
o.place(x=300,y=350)
o_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lbloctal)
o_txt.place(x=650,y=350)

s=Label(root,text='Masukan Huruf',font='Nunito 20 bold')
s.place(x=300,y=400)
s_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lblstring)
s_txt.place(x=650,y=400)

sh=Label(root,text='ASCII',font='Nunito 20 bold')
sh.place(x=300,y=450)
sh_txt=Entry(root,font=('Nunito',20,'bold'),fg='black',justify=CENTER,relief=GROOVE,textvariable=lblhasilascii)
sh_txt.place(x=650,y=450)

btn1=Button(root,text='Convert',font='Nunito 20 bold',fg='WHITE',bg='blue',width=10,command=convert)
btn1.place(x=380,y=550)

btn2=Button(root,text='Hapus',font='Nunito 20 bold',fg='WHITE',bg='blue',width=10,command=clear)
btn2.place(x=680,y=550)

btn3=Button(root,text='Keluar',font='Nunito 20 bold',fg='WHITE',bg='blue',width=10,command=exit)
btn3.place(x=980,y=550)

btn4=Button(root,text='ASCII',font='Nunito 20 bold',fg='WHITE',bg='blue',width=10,command=konversi_ascii)
btn4.place(x=80,y=550)

root.mainloop()