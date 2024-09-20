from tkinter import *
from PIL import ImageTk, Image
import user_login
import admin_login

def home(w, wi, he):
    bg_frame = Image.open('./images/home1.png')
    bg_frame = bg_frame.resize((wi, he), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(bg_frame)
    w.photo = photo  
    bg_panel = Label(w, image=photo)
    bg_panel.place(width=wi, height=he)

    def Admin():
        w.withdraw()
        admin_window = Toplevel(w)
        admin_window.geometry(f"{wi}x{he}")
        admin_login.admin_loginf(admin_window, wi, he)

    def User():
        w.withdraw()
        user_window = Toplevel(w)
        user_window.geometry(f"{wi}x{he}")
        user_login.user_loginf(user_window, wi, he)

    admin = Button(w, text='ADMIN', font=("gotham", 15, "bold"), width=15, bd=0,
                   bg='white', cursor='hand2', fg='black', command=Admin)
    admin.place(relx=0.31, rely=0.57)

    user = Button(w, text='USER', font=("gotham", 15, "bold"), width=15, bd=0,
                  bg='white', cursor='hand2', fg='black', command=User)
    user.place(relx=0.56, rely=0.57)

    w.mainloop()

if __name__ == '__main__':
    root = Tk()
    wi, he = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f'{wi}x{he}')
    root.title('Home')

    top_window = Toplevel(root)
    top_window.geometry(f"{wi}x{he}+0+0")
    top_window.title('Home')

    root.withdraw()

    home(top_window, wi, he)
