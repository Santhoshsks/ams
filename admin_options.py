from tkinter import *
from PIL import ImageTk,Image
import home
import database_code
from tkinter import messagebox
import ast

def admin_optionsf():
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Options')
    w.resizable(0, 0)
    
    bg_frame = Image.open('./images/adminselection.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    
    def admin_detail():
        w.destroy()
        database_code.run()

    Button(w, text='Details', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=admin_detail).place(relx=0.310,rely=0.560)

    
    def add_user_id():
        w.destroy()
        global add_wind
        add_wind = Toplevel()
        add_Tenant(add_wind)

    Button(w, text='Add User', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=add_user_id).place(relx=0.580,rely=0.560)


    def back():
            w.destroy()
            home.home()

    b2=Button(w,width=6,text='<Back',border=0,bg='white',fg='black',command=back).place(relx=0.810,rely=0.780)

    w.mainloop()        
    
def base_update(k,v):
        key=k
        value=v
        file=open('userp.txt','r+')
        d=file.read()
        global r
        r=ast.literal_eval(d)
        dict2={key:value}
        r.update(dict2)
        file.truncate(0)
        file.close()
        file=open('userp.txt','w')
        w=file.write(str(r))

class add_Tenant:
    def __init__(self, top=None):
        self.top=top
        self.top.geometry("1366x768")
        self.top.resizable(0, 0)
        self.top.title("Add ID")

        self.label1 = Label(self.top)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/id_creater.png")
        self.label1.configure(image=self.img)
        
        file=open('userp.txt','r+')
        d=file.read()
        global userpass
        userpass=ast.literal_eval(d)


        def on_enter(e):
            self.e1.delete(0,'end')    
        def on_leave(e):
            if self.e1.get()=='':   
                self.e1.insert(0,'Apt no')

        
        self.e1 =Entry(self.top,width=30,fg='black',border=0,bg='white')
        self.e1.config(font=('Microsoft YaHei UI Light',16))
        self.e1.bind("<FocusIn>", on_enter)
        self.e1.bind("<FocusOut>", on_leave)
        self.e1.insert(0,'Apt no')
        self.e1.place(relx=0.510,rely=0.349)
            

        def on_enter(e):
            self.e2.delete(0,'end')    
        def on_leave(e):
            if self.e2.get()=='':   
                self.e2.insert(0,'Username')

        self.e2 =Entry(self.top,width=30,fg='black',border=0,bg='white')
        self.e2.config(font=('Microsoft YaHei UI Light',16))
        self.e2.bind("<FocusIn>", on_enter)
        self.e2.bind("<FocusOut>", on_leave)
        self.e2.insert(0,'Username')
        self.e2.place(relx=0.510,rely=0.510)

        def on_enter(e):
            self.e3.delete(0,'end')    
        def on_leave(e):
            if self.e3.get()=='':   
                self.e3.insert(0,'Password')

        self.e3 =Entry(self.top,width=30,fg='black',border=0,bg='white')
        self.e3.config(font=('Microsoft YaHei UI Light',16))
        self.e3.bind("<FocusIn>", on_enter)
        self.e3.bind("<FocusOut>", on_leave)
        self.e3.insert(0,'Password')
        self.e3.place(relx=0.510,rely=0.666)


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        def add():
            Apt_no = self.e1.get()
            Name = self.e2.get()
            Password = self.e3.get()

            if Apt_no.upper() not in userpass.keys():
                if Apt_no and Apt_no != "Apt no":
                    if  Name and Name != "Username":
                        if Password and Password != "Password":
                            data=(Name,Password)
                            base_update(Apt_no.upper(),data)
                            messagebox.showinfo("Success!!", "Account successfully added in database.", parent=add_wind)
                            clearr()
        
                        else:
                            messagebox.showerror("Oops!", "Please enter Password", parent=add_wind)
                    else:
                        messagebox.showerror("Oops!", "Please enter Name", parent=add_wind)
                else:
                    messagebox.showerror("Oops!", "Please enter Apt No", parent=add_wind)
            else:
                messagebox.showerror("Oops!", "User already exist", parent=add_wind)

        def clearr():
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)


        def back():
            add_wind.destroy()
            admin_optionsf()

        Button(self.top,width=6,text='<BACK',border=0,bg='white',fg='black',command=back).place(relx=0.795, rely=0.785)
        Button(self.top,text='ADD', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=add).place(relx=0.600,rely=0.773)


        
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))       

if __name__ == '__main__':
    admin_optionsf()
    
    
