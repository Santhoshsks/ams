from tkinter import *
from PIL import ImageTk,Image
import user_login
import user_details
import in_out
import maid_info
import parking_info

def optionsf(k):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Options')
    w.resizable(0, 0)
    
    bg_frame = Image.open('./images/uselection.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    
    def user_detail():
        w.destroy()
        user_details.user_detailsf(k)

    Button(w, text='Details', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=user_detail).place(relx=0.217,rely=0.515)

    def inout():
        w.destroy()
        in_out.in_outf(k)

    Button(w, text='Amount', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=inout).place(relx=0.381,rely=0.510)

    def maid():
        w.destroy()
        maid_info.run(k)

    Button(w, text='Maids', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=maid).place(relx=0.542,rely=0.510)

    def park():
        w.destroy()
        parking_info.parking_infof(k)

    Button(w, text='parking', font=("gotham",12,"bold"), width=10, bd=0,
        bg='white', cursor='hand2', fg='black',command=park).place(relx=0.705,rely=0.510)


    def back():
            w.destroy()
            user_login.user_loginf()

    b2=Button(w,width=6,text='<Back',border=0,bg='white',fg='black', cursor='hand2',command=back).place(relx=0.810,rely=0.780)

    w.mainloop()        
    
if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    optionsf(0)

