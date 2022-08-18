from tkinter import *
from PIL import ImageTk,Image
import user_login
import ast
import options
from tkinter import messagebox

#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def update(k,v,b):
        key=k
        value=v
        file=open('parking_base.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        dict2={key:value}
        if b=="A" and r["A"]>0:
            r.update(dict2)
            r['A']-=1
            file.truncate(0)
            file.close()
            messagebox.showinfo("Success","Parking Slot Booked in a Block")
            return r
        elif b=="A" and r["A"]<=0:
            messagebox.showinfo("Error","NO SLOTS TO PARK IN A BLOCK")
            return r
        elif b=="B" and r["B"]>0:
            r.update(dict2)
            r['B']-=1
            file.truncate(0)
            file.close()
            messagebox.showinfo("Succes","Parking Slot Booked in b Block")
            return r
        else:
            messagebox.showinfo("Error","NO SLOTS TO PARK IN B BLOCK")
            return r

def display(k):
    w1=Toplevel()
    w1.geometry('1366x768')
    w1.title('Parking Booking')
    w1.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w1, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    #(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    path='parking_base.txt'
    #(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

#'A': 0, 'B': 42, 'santhosh': ('a', 123796984, 12, 600)

    file=open('parking_base.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    Lst =[]
    Lst.append(["Name","Block","Number","Days","Cost"])
    for j in r.keys():
        if j !="A" and j != "B":
            Lst.append([j,r[j][0],r[j][1],str(r[j][2]),str(r[j][3])])
    frame = Frame(w1,bg='#F2B33D')
    rows = []
    for i in range(len(Lst)):
        cols = []
        for j in range(len(Lst[0])):
            e = Entry(frame,relief=GROOVE)
            e.grid(row=i, column=j, sticky=NSEW,ipadx=12,ipady=20)
            e.insert(END,(str(Lst[i][j])))
            e.config(state= "disabled")
            cols.append(e)
        rows.append(cols)
    frame.pack(expand=True) 

    def back():
        w1.destroy()
        parking_infof(k)
    Button(w1, text='Back', font=("gotham",10,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.88)
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def offline(k):
    w1=Toplevel()
    w1.geometry('1366x768')
    w1.title('Parking Booking')
    w1.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w1, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)

    def testint(val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    r1 = w1.register(testint)
    r2 = w1.register(testchar)

    Label(w1,text="Name:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.26)
    e1 =Entry(w1,width=14,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',15),validate="key", validatecommand=(r2, "%P"))
    e1.place(relx=0.50,rely=0.26)
    
    Label(w1,text="Number:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.33)
    e2 =Entry(w1,width=14,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',15),validate="key", validatecommand=(r1, "%P"))
    e2.place(relx=0.50,rely=0.33)
    
    Label(w1,text="Days:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.42)
    e3 =Entry(w1,width=14,fg='black',border=0,bg='white')
    e3.config(font=('Microsoft YaHei UI Light',15),validate="key", validatecommand=(r1, "%P"))
    e3.place(relx=0.50,rely=0.42)

    Label(w1,text="Block:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.51)
    e4 =Entry(w1,width=14,fg='black',border=0,bg='white')
    e4.config(font=('Microsoft YaHei UI Light',15))
    e4.place(relx=0.50,rely=0.51)

    def Bookf():
        name=e1.get().lower()
        ph=e2.get()
        days=e3.get()
        b=e4.get().upper()
        if name:
            if days:
                if b == "A" or b == "B":
                    if len(ph)==10:
                        cost=int(days)*50
                        up_dict = update(name,(b,ph,days,cost),b)
                        file=open('parking_base.txt','w')
                        file.write(str(up_dict))   
                        file.close()
                    else:
                        messagebox.showerror("Error","Enter Proper Mobile No") 
                else:
                    messagebox.showerror("Error","Enter a or b block") 
            else:
                messagebox.showerror("Error","Enter Days") 
        else:
            messagebox.showerror("Error","Enter Name") 
    Button(w1, text='Book', font=("gotham",13,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=Bookf).place(relx=0.430,rely=0.60)

    def back():
        w1.destroy()
        parking_infof(k)
    Button(w1, text='Back', font=("gotham",10,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.80)
    w1.mainloop()      

def parking_infof(k):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Parking')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)

    Label(w,text="Available in a block:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.26)
    file=open('parking_base.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    e1 =Entry(w,width=14,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',15))
    e1.place(relx=0.50,rely=0.26)
    e1.insert(0,r["A"])
    e1.config(state="disabled")

    Label(w,text="Available in b block:",font=('Microsoft YaHei UI Light',13)).place(relx=0.37,rely=0.33)
    e2 =Entry(w,width=14,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',15))
    e2.place(relx=0.50,rely=0.33)
    e2.insert(0,r["B"])
    e2.config(state="disabled")

    def offlinef():
        w.destroy()
        offline(k)
    Button(w, text='Book', font=("gotham",13,"bold"), width=15, bd=0,bg='white', cursor='hand2', fg='black',command=offlinef).place(relx=0.33,rely=0.45)
    
    def displayf():
        w.destroy()
        display(k)
    Button(w, text='Booked', font=("gotham",13,"bold"), width=15, bd=0,bg='white', cursor='hand2', fg='black',command=displayf).place(relx=0.54,rely=0.45)
    
    def back():
        w.destroy()
        options.optionsf(k)
    Button(w, text='Back', font=("gotham",10,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.80)
    w.mainloop()
    
if __name__ == '__main__':
    parking_infof("A201")