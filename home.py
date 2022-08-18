from tkinter import *
from PIL import ImageTk,Image
import user_login
import admin_login

def home():
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Home')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/home1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)

    def Admin():
        w.destroy()
        admin_login.admin_loginf() 

    def User():
        w.destroy()
        user_login.user_loginf()
    
    admin = Button(w, text='ADMIN', font=("gotham",15,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=Admin)
    admin.place(relx=0.30,rely=0.553)

    user = Button(w, text='USER', font=("gotham",15,"bold"), width=15, bd=0,
                            bg='white', cursor='hand2', fg='black',command=User)
    user.place(relx=0.550,rely=0.554)

    if __name__ == '__main__':
        w1=Toplevel()
        wi, he = w1.winfo_screenwidth(), w1.winfo_screenheight()
        w1.geometry("%dx%d+0+0" % (wi, he))
        w1.title('Home')
        w1.mainloop()
    w.mainloop()        
    
if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    home()
    
