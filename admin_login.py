from tkinter import *
from PIL import ImageTk,Image
import ast
import home
from tkinter import messagebox
import admin_options

def admin_loginf():
    file=open('adminp.txt','r+')
    d=file.read()
    database_dict1=ast.literal_eval(d)

    
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Home')
    w.resizable(0, 0)
     
    bg_frame = Image.open('./images/adminpage.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)    
    
#------------------------------------------------------------------------------------------------------------
    def signin():        
        
        def on_enter(e):
            e1.delete(0,'end')    
        def on_leave(e):
            if e1.get()=='':   
                e1.insert(0,'Username')

        Frame(w,width=295,height=2,bg='black').place(relx=0.510,rely=0.407)
        e1 =Entry(w,width=30,fg='black',border=0,bg='white')
        e1.config(font=('Microsoft YaHei UI Light',16))
        e1.bind("<FocusIn>", on_enter)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0,'Username')
        e1.place(relx=0.510,rely=0.396)
            
        def on_enter(e):  
            e2.delete(0,'end')   
            e2.configure(fg='black',show='*')
             
        
        Frame(w,width=295,height=2,bg='black').place(relx=0.510,rely=0.5780)
        e2 =Entry(w,width=30,fg='black',border=0,bg='white')
        e2.config(font=('Microsoft YaHei UI Light',16))
        e2.bind("<FocusIn>", on_enter)
        e2.insert(0,'Password')
        e2.place(relx=0.510,rely=0.559)

        
        def back():
            w.destroy()
            home.home()

        
        b2=Button(w,width=6,text='<Back',border=0,bg='white',fg='black',command=back)
        b2.place(relx=0.810,rely=0.780)
#------------------------------------------------------------------------------------------------------------
        def signin_cmd():  
            r=database_dict1
           
                
            key=e1.get()
            value=e2.get()
                
            if key in r.keys() and value==r[key]:           
                messagebox.showinfo("","   successfully logged in   ")
                w.destroy()
                admin_options.admin_optionsf()
            else:
                messagebox.showwarning('try again', 'invalid username or password')


        Button(w, text='Login', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=signin_cmd).place(relx=0.610,rely=0.680)

    signin()

    w.mainloop()


if __name__ == '__main__':
    admin_loginf()

