from tkinter import *
from PIL import ImageTk,Image
import ast
import home
from tkinter import messagebox
import options

def user_loginf():
    
    global w
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Home')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/usersignin.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)    
    
#------------------------------------------------------------------------------------------------------------

    file=open('userp.txt','r+')
    d=file.read()
    database_dict=ast.literal_eval(d)
    
    file=open('base.txt','r+')
    d=file.read()
    base_dict=ast.literal_eval(d)

    def signin():        
        def on_enter(e):
            e1.delete(0,'end')    
        def on_leave(e):
            if e1.get()=='':   
                e1.insert(0,'Apt no')

        e1 =Entry(w,width=30,fg='black',border=0,bg='white')
        e1.config(font=('Microsoft YaHei UI Light',16))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0,'Apt No')
        e1.place(relx=0.510,rely=0.344)

        def on_enter(e):
            e2.delete(0,'end')    
        def on_leave(e):
            if e2.get()=='':   
                e2.insert(0,'Username')

        e2 =Entry(w,width=30,fg='black',border=0,bg='white')
        e2.config(font=('Microsoft YaHei UI Light',16))
        e2.bind("<FocusIn>", on_enter)
        e2.bind("<FocusOut>", on_leave)
        e2.insert(0,'Username')
        e2.place(relx=0.510,rely=0.505)

        def on_enter(e):  
            e3.delete(0,'end')   
            e3.configure(fg='black',show='*')

        e3 =Entry(w,width=30,fg='black',border=0,bg='white')
        e3.config(font=('Microsoft YaHei UI Light',16))
        e3.bind("<FocusIn>", on_enter)
        e3.insert(0,'Password')
        e3.place(relx=0.510,rely=0.666)

        def back():
            w.destroy()
            home.home()
        Button(w,width=6,text='<Back',border=0,bg='white',fg='black', cursor='hand2',command=back).place(relx=0.755,rely=0.780)

        def signin_cmd():
                
            r=database_dict
            key=e1.get()
            value=(e2.get(),e3.get())
            s=base_dict
            if key.upper() in s.keys():
                if key.upper() in r.keys() and value==(r[key.upper()][0],r[key.upper()][1]):           
                    messagebox.showinfo("","   successfully logged in   ")
                    w.destroy()
                    options.optionsf(key.upper())
                else:
                    messagebox.showwarning('try again', 'invalid username or password')
            else:
                messagebox.showwarning('Request admin','DataBase Is Not Created for this Apt No Yet')

        Button(w, text='Login', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=signin_cmd).place(relx=0.600,rely=0.773)

    signin()
    w.mainloop()


if __name__ == '__main__':
    user_loginf()

