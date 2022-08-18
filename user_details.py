from tkinter import *
from PIL import ImageTk,Image
import options
import ast

def user_detailsf(apt_no):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Home')
    w.resizable(0, 0)
    file=open('base.txt','r+')
    reade=file.read()
    dictionary=ast.literal_eval(reade)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(w, image=photo)
    bg_panel.image = photo
    bg_panel.place(width=1366,height=768)
    head=["Apt No:","Name:","Mobile","Gender","Block:","Sq Feet:","Amount:","Status:"]
    string=[]
    for i in dictionary.keys():
        if i == apt_no:
            for j in dictionary[i]:
                string.append(str(j))     
                                                         
    Label(w,text=head[0],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.30)
    Label(w,text=head[1],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.36)
    Label(w,text=head[2],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.42)
    Label(w,text=head[3],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.48)
    Label(w,text=head[4],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.54)
    Label(w,text=head[5],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.60)
    Label(w,text=head[6],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.66)
    Label(w,text=head[7],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.23,rely=0.72)

    Label(w,text=string[0],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.30)
    Label(w,text=string[1],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.36)
    Label(w,text=string[2],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.42)
    Label(w,text=string[3],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.48)
    Label(w,text=string[4],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.54)
    Label(w,text=string[5],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.60)
    Label(w,text=string[6],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.66)
    Label(w,text=string[7],height=2,width=38,font=("gotham",10,"bold"),fg='black').place(relx=0.53,rely=0.72)

    def back():
        w.destroy()
        options.optionsf(apt_no)

    user = Button(w, text='Back', font=("gotham",10,"bold"), width=10, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back)
    user.place(relx=0.6885,rely=0.85)
    
    w.mainloop()        
    
if __name__ == '__main__':
    user_detailsf("A201")
