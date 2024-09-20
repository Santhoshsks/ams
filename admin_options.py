from tkinter import *
from PIL import ImageTk, Image
import home
import database_code
from tkinter import messagebox
import sqlite3

def admin_optionsf():
    w = Toplevel()
    w.geometry('1366x768')
    w.title('Options')
    w.resizable(0, 0)

    bg_frame = Image.open('./images/adminselection.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366, height=768)

    def admin_detail():
        w.destroy()
        database_code.TenantManagement()

    Button(w, text='Details', font=("gotham", 12, "bold"), width=10, bd=0,
           bg='white', cursor='hand2', fg='black', command=admin_detail).place(relx=0.310, rely=0.560)

    def add_user_id():
        w.destroy()
        global add_wind
        add_wind = Toplevel()
        add_Tenant(add_wind)

    Button(w, text='Add User', font=("gotham", 12, "bold"), width=10, bd=0,
           bg='white', cursor='hand2', fg='black', command=add_user_id).place(relx=0.580, rely=0.560)

    def back():
        w.destroy()
        home.home()

    Button(w, width=6, text='<Back', border=0, bg='white', fg='black', command=back).place(relx=0.810, rely=0.780)

    w.mainloop()

class add_Tenant:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("1366x768")
        self.top.resizable(0, 0)
        self.top.title("Add ID")

        self.label1 = Label(self.top)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/id_creater.png")
        self.label1.configure(image=self.img)

        def on_enter(e, entry):
            entry.delete(0, 'end')

        def on_leave(e, entry, placeholder):
            if entry.get() == '':
                entry.insert(0, placeholder)

        self.e1 = Entry(self.top, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 16))
        self.e1.bind("<FocusIn>", lambda e: on_enter(e, self.e1))
        self.e1.bind("<FocusOut>", lambda e: on_leave(e, self.e1, 'Apt no'))
        self.e1.insert(0, 'Apt no')
        self.e1.place(relx=0.510, rely=0.349)

        self.e2 = Entry(self.top, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 16))
        self.e2.bind("<FocusIn>", lambda e: on_enter(e, self.e2))
        self.e2.bind("<FocusOut>", lambda e: on_leave(e, self.e2, 'Username'))
        self.e2.insert(0, 'Username')
        self.e2.place(relx=0.510, rely=0.510)

        self.e3 = Entry(self.top, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 16))
        self.e3.bind("<FocusIn>", lambda e: on_enter(e, self.e3))
        self.e3.bind("<FocusOut>", lambda e: on_leave(e, self.e3, 'Password'))
        self.e3.insert(0, 'Password')
        self.e3.place(relx=0.510, rely=0.666)

        def add():
            apt_no = self.e1.get().upper()
            username = self.e2.get()
            password = self.e3.get()

            if apt_no and apt_no != "Apt no" and username and username != "Username" and password and password != "Password":
                try:
                   
                    conn = sqlite3.connect('users.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()

                    cursor.execute("INSERT INTO user_details (apt_no, name, mobile, gender, amount, pay_status) VALUES (?, ?, ?, ?, ?, ?)",
                                   (apt_no, username, '', '', 0, False))
                    conn.commit()
                    messagebox.showinfo("Success!", "User successfully added.", parent=add_wind)
                    conn.close()
                    clear_entries()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error!", "Username must be unique or apartment does not exist.", parent=add_wind)
                    conn.close()
            else:
                messagebox.showerror("Oops!", "Please fill all fields correctly", parent=add_wind)

        def clear_entries():
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)

        def back():
            add_wind.destroy()
            admin_optionsf()

        Button(self.top, width=6, text='<BACK', border=0, bg='white', fg='black', command=back).place(relx=0.795, rely=0.785)
        Button(self.top, text='ADD', font=("gotham", 12, "bold"), width=10, bd=0,
               bg='white', cursor='hand2', fg='black', command=add).place(relx=0.600, rely=0.773)

if __name__ == '__main__':
    admin_optionsf()
