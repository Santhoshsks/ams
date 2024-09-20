from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
import admin_options

def admin_loginf(w, wi, he):
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor()

    bg_frame = Image.open('./images/adminpage.png')
    bg_frame = bg_frame.resize((wi, he), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=wi, height=he)

    def signin():
        e1 = Entry(w, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 16))
        e1.insert(0, 'Username')
        e1.place(relx=0.510, rely=0.344)

        e2 = Entry(w, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 16))
        e2.insert(0, 'Password')
        e2.place(relx=0.510, rely=0.505)

        def clear_entry(event):
            event.widget.delete(0, 'end')

        e1.bind("<FocusIn>", clear_entry)
        e2.bind("<FocusIn>", clear_entry)

        def signin_cmd():
            username = e1.get()
            password = e2.get()

            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if result and result[0] == password:
                messagebox.showinfo("", "Successfully logged in")
                w.destroy()
                admin_options.admin_optionsf()
            else:
                messagebox.showwarning("Try Again", "Invalid username or password")

        Button(w, text='Login', font=("gotham", 12, "bold"), width=10, bd=0, bg='white', cursor='hand2', fg='black', command=signin_cmd).place(relx=0.600, rely=0.773)

    signin()
    w.mainloop()
    conn.close()

if __name__ == "__main__":
    root = Tk()
    wi, he = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f'{wi}x{he}')
    admin_loginf(root, wi, he)
