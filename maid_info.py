from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import options
import ast

def maid_infof(List,k):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Maid')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)

    frame = Frame(w, bg='#F2B33D')

    rows = []
    for i in range(len(List)):
        cols = []
        for j in range(4):
            e = Entry(frame,relief=GROOVE)
            e.grid(row=i, column=j, sticky=NSEW,ipadx=12,ipady=20)
            e.insert(END,(str(List[i][j])))
            e.config(state= "disabled")
            cols.append(e)
        rows.append(cols)
    frame.pack(expand=True) 

    def back():
        w.destroy()
        run(k)
    Button(w, text='Back', font=("gotham",13,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.80)
    w.mainloop()        

def maid_list(k):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Maid')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    global r1
    file=open('maids.txt','r+')
    d=file.read()
    r1=ast.literal_eval(d)
    file.close()
    L=[]
    L.append(["Maid ID","Name","Work","Mobile"])
    for i,j in r1.items():
        L.append([i,j[0],j[1],j[2]])

    frame = Frame(w, bg='#F2B33D')
    rows = []
    for i in range(len(L)):
        cols = []
        for j in range(4):
            e = Entry(frame,relief=GROOVE)
            e.grid(row=i, column=j, sticky=NSEW,ipadx=12,ipady=20)
            e.insert(END,(str(L[i][j])))
            e.config(state= "disabled")
            cols.append(e)
        rows.append(cols)
    frame.pack(expand=True)


    def back():
        w.destroy()
        run(k)

    Button(w, text='Back', font=("gotham",13,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.58,rely=0.80)
    w.mainloop()    

def addf(k,a):
        file=open('maids.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        r[a.lower()].append(k)
        file.truncate(0)
        file.close()
        file=open('maids.txt','w')
        file.write(str(r))
    
def delf(k,a):
        file=open('maids.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        r[a.lower()].remove(k)
        file.truncate(0)
        file.close()
        file=open('maids.txt','w')
        file.write(str(r))
    
def maid_lister(k):
    file=open('maids.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    L=[]
    L.append(["Maid ID","Name","Work","Mobile"])
    for i,j in r.items():
        if k in r[i]:
            L.append([i,j[0],j[1],j[2]])
    if len(L) > 1:
        maid_infof(L,k)
    else:
        messagebox.showinfo("No Maid Assigned")
        run(k)

def run(k):
    w1=Toplevel()
    w1.geometry('1366x768')
    w1.title('Maid')
    w1.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w1, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    Label(w1,text="Maid Id:",font=('Microsoft YaHei UI Light',13)).place(relx=0.325,rely=0.26)
    file=open('maids.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    e1 =Entry(w1,width=30,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',16))
    e1.place(relx=0.38,rely=0.26)

    def add2(k,a):
        if a != "" and a[0] == "m":
            if a in r.keys():
                if k not in r[a]:
                    addf(k,a)
                    messagebox.showinfo('Success','Maid Booked')
                else:
                    messagebox.showinfo('Try again','Already Booked')
            else:
                messagebox.showwarning('try again',"Maid Id Is Incorrect")
        elif a == "":
            messagebox.showwarning('try again',"Entry is Empty")
        else:
            messagebox.showwarning('try again',"Maid Id Is Incorrect")
        
    Button(w1, text='Book Maid', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=lambda:add2(k,a=e1.get())).place(relx=0.42,rely=0.40)

    def display():
        w1.destroy()
        maid_lister(k)
    Button(w1, text='Booked Maid', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=display).place(relx=0.42,rely=0.50)
    def add1():
        w1.destroy()
        maid_list(k)
    Button(w1, text='Maids List', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=add1).place(relx=0.42,rely=0.60)

    def del2(k,a):
        if a != "" and a[0] == "m":
            if a in r.keys():
                if k in r[a]:
                    delf(k,a)
                    messagebox.showinfo('Success','Maid Canceled')
                else:
                    messagebox.showinfo('Try Again','Book First To Cancel')
            else:
                messagebox.showwarning('Try Again','Maid Id Is Incorrect')
        elif a == "":
            messagebox.showwarning('Try Again',"Entry is Empty")
        else:
            messagebox.showwarning('Try Again',"Maid Id Is Incorrect")

    Button(w1, text='Cancel', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=lambda:del2(k,a=e1.get())).place(relx=0.42,rely=0.70)

    def back():
        w1.destroy()
        options.optionsf(k)

    Button(w1, text='Back', font=("gotham",10,"bold"), width=10, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.80)
    w1.mainloop()

if __name__ == '__main__':
    run("A201")