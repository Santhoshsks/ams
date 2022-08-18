from tkinter import *
from datetime import datetime
from PIL import ImageTk,Image
from tkinter import messagebox
import options
import ast

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))
DATA_LIST=[['A001', '1798', '17103'], ['A002', '1798', '17103'], ['A003', '1388', '13659'], ['A004', '1388', '13659'], ['A005', '1110', '11324'], ['A006', '1110', '11324'], ['A007', '1388', '13659'], ['A008', '1388', '13659'], ['A101', '2010', '18884'], ['A102', '2010', '18884'], ['A103', '1480', '14432'], ['A104', '1480', '14432'], ['A105', '1150', '11660'], ['A106', '1150', '11660'], ['A107', '1480', '14432'], ['A108', '1480', '14432'], ['A201', '2010', '18884'], ['A202', '2010', '18884'], ['A203', '1480', '14432'], ['A204', '1480', '14432'], ['A205', '1150', '11660'], ['A206', '1150', '11660'], ['A207', '1480', '14432'], ['A208', '1480', '14432'], ['A301', '2010', '18884'], ['A302', '2010', '18884'], ['A303', '1480', '14432'], ['A304', '1480', '14432'], ['A305', '1150', '11660'], ['A306', '1150', '11660'], ['A307', '1480', '14432'], ['A308', '1480', '14432'], ['A401', '2010', '18884'], ['A402', '2010', '18884'], ['A403', '1480', '14432'], ['A404', '1480', '14432'], ['A405', '1150', '11660'], ['A406', '1150', '11660'], ['A407', '1480', '14432'], ['A408', '1480', '14432'], ['A501', '2010', '18884'], ['A502', '2010', '18884'], ['A503', '1480', '14432'], ['A504', '1480', '14432'], ['A505', '1150', '11660'], ['A506', '1150', '11660'], ['A507', '1480', '14432'], ['A508', '1480', '14432'], ['A601', '2010', '18884'], ['A602', '2010', '18884'], ['A603', '1480', '14432'], ['A604', '1480', '14432'], ['A605', '1150', '11660'], ['A606', '1150', '11660'], ['A607', '1480', '14432'], ['A608', '1480', '14432'], ['A701', '2010', '18884'], ['A702', '2010', '18884'], ['A703', '1480', '14432'], ['A704', '1480', '14432'], ['A705', '1150', '11660'], ['A706', '1150', '11660'], ['A707', '1480', '14432'], ['A708', '1480', '14432'], ['A801', '2010', '18884'], ['A802', '2010', '18884'], ['A803', '1480', '14432'], ['A804', '1480', '14432'], ['A805', '1150', '11660'], ['A806', '1150', '11660'], ['A807', '1480', '14432'], ['A808', '1480', '14432']]
DATA_DICT={} #How it looks --->{'A001':['1798','17103'],'B001':['1798','17103'],...}
for i in DATA_LIST:
    DATA_DICT[i[0]]=[i[1],i[2]]
    str1=i[0][1:]
    str2="B"+str1#To Replace A with B
    DATA_DICT[str2]=[i[1],i[2]]
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def pay(k):
    file=open('base.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    if k in r.keys():
        if r[k][7] == "PAID":
            return True
        else:
            return False
    else:
        return "No"

def outgoing(k):
    file=open('base.txt','r+')
    d=file.read()
    file.close()
    r=ast.literal_eval(d)
    if pay(k) == False:
        messagebox.showwarning('Due','Cant Close Account With Due To Pay') 
    elif pay(k) == True:
        sure = messagebox.askyesno("Confirm", "Are you sure you want to delete Account?")
        if sure == True:
            del r[k]
            file=open('base.txt','w')
            file.truncate(0)
            file.close()
            file=open('base.txt','w')
            file.write(str(r))
            file.close()
            messagebox.showinfo("Success!!", "Account deleted from database.")
        else:
            pass
    else:
        messagebox.showwarning("Wrong","Apartment is Not Registered,Request Admin!")

def in_outf(k):
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Home')
    w.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_pkel = Label(w, image=photo)
    bg_pkel.image = photo
    bg_pkel.place(width=1366,height=768)
    
    def outf():
        outgoing(k)  

    def maintf():
        w.destroy()
        maintenance_fee(k)

    def back():
        w.destroy()
        options.optionsf(k)

    user = Button(w, text='Vacate', font=("gotham",15,"bold"), width=15, bd=0,bg='white', cursor="hand2", fg='black',command=outf)
    user.place(relx=0.32,rely=0.554)

    user = Button(w, text='Maintenance', font=("gotham",15,"bold"), width=15, bd=0,bg='white', cursor="hand2", fg='black',command=maintf)
    user.place(relx=0.53,rely=0.554)
    
    back = Button(w, text='Back', font=("gotham",10,"bold"), width=10, bd=0,bg='white', cursor="hand2", fg='black',command=back)
    back.place(relx=0.70,rely=0.85)
    w.mainloop()        

def maintenance_fee(k):
    w1=Toplevel()
    w1.geometry('1366x768')
    w1.title('Home')
    w1.resizable(0, 0)
    bg_frame = Image.open('./images/plainbg1.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_pkel = Label(w1, image=photo)
    bg_pkel.image = photo
    bg_pkel.place(width=1366,height=768)

    Label(w1,text="Name:",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.26)
    file=open('base.txt','r+')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    e1 =Entry(w1,width=20,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',16))
    e1.place(relx=0.41,rely=0.26)
    e1.insert(0,r[k][1])
    e1.config(state="disabled")

    def showduef(k):
        Label(w1,text="Due :",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.31)
        e1 =Entry(w1,width=20,fg='black',border=0,bg='white')
        e1.config(font=('Microsoft YaHei UI Light',16))
        e1.place(relx=0.41,rely=0.31)
        e1.insert(0,r[k][6])
        e1.config(state="disabled")

        def cal(k):
            file=open('base.txt','r+')
            d=file.read()
            Dct=ast.literal_eval(d)
            doy = datetime.now().timetuple().tm_yday
            file.close()
            Label(w1,text="Date:",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.36)
            e1 =Entry(w1,width=20,fg='black',border=0,bg='white')
            e1.config(font=('Microsoft YaHei UI Light',16))
            e1.place(relx=0.41,rely=0.36)
            e1.insert(0,doy)
            e1.config(state="disabled")


            def quarterly(k):    
                r=0 #Running date quarterly
                prp=0 #Present pending dues
                pap=Dct[k][6] #Past pending dues
                ma=int(DATA_DICT[k][1]) #Maintenance charge variable requires standard input from the database for the given flat number variables
                if(doy>0 and doy<=90):
                    q=1
                    r=doy
                elif(doy>90 and doy<=181):
                    q=2
                    r=doy-90
                elif(doy>181 and doy<=273):
                    q=3
                    r=doy-181
                elif(doy>274 and doy<=366):
                    q=4
                    r=doy-274
                if(r<=25):
                    ttl=ma
                elif(r>25 and r<=40):
                    ttl=ma+250
                elif(r>40 and r<=90):
                    ttl=ma+250+(10*(r-40))
                
                prp=ttl
                Label(w1,text="Quarter:",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.41)
                e1 =Entry(w1,width=20,fg='black',border=0,bg='white')
                e1.config(font=('Microsoft YaHei UI Light',16))
                e1.place(relx=0.41,rely=0.41)
                e1.insert(0,q)
                e1.config(state="disabled")

                Label(w1,text="Fee:",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.46)
                e1 =Entry(w1,width=20,fg='black',border=0,bg='white')
                e1.config(font=('Microsoft YaHei UI Light',16))
                e1.place(relx=0.41,rely=0.46)
                e1.insert(0,prp)
                e1.config(state="disabled")
                
                Label(w1,text="Paid[y/n]:",font=('Microsoft YaHei UI Light',13)).place(relx=0.35,rely=0.51)
                e5 =Entry(w1,width=20,fg='black',border=0,bg='white')
                e5.config(font=('Microsoft YaHei UI Light',16))
                e5.place(relx=0.41,rely=0.51)

                def fin():
                    c=e5.get()
                    if c=='n':
                        Dct[k][6]+=prp
                        file=open('base.txt','w')
                        file.truncate(0)
                        file.close()
                        file=open('base.txt','w')
                        file.write(str(Dct)) 
                        file.close()
                        messagebox.showinfo('success','Fee Added To Base')
                        w1.destroy()
                        in_outf(k)
            
                def qf1():
                    fin()
                     
                Button(w1, text='Add To Base', font=("gotham",13,"bold"), width=20, bd=0,
                                    bg='white', cursor='hand2', fg='black',command=qf1).place(relx=0.41,rely=0.56)

            def qf():
                if k in r.keys():
                    quarterly(k)
                else:
                    messagebox.showwarning("Wrong","Apartment is Not Registered,Request Admin!")

            Button(w1, text='Quarterly', font=("gotham",13,"bold"), width=20, bd=0,
                                bg='white', cursor='hand2', fg='black',command=qf).place(relx=0.63,rely=0.70)


        def calf():
            if k in r.keys():
                cal(k)
            else:
                messagebox.showwarning("Wrong","Apartment is Not Registered,Request Admin!")

        Button(w1, text='Date', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=calf).place(relx=0.43,rely=0.70)

    def duef():
        if k in r.keys():
            showduef(k)
        else:
            messagebox.showwarning("Wrong","Apartment is Not Registered,Request Admin!")

    Button(w1, text='Due', font=("gotham",13,"bold"), width=20, bd=0,
                            bg='white', cursor='hand2', fg='black',command=duef).place(relx=0.23,rely=0.70)

    def back():
        w1.destroy()
        in_outf(k)

    Button(w1, text='Back', font=("gotham",10,"bold"), width=10, bd=0,
                            bg='white', cursor='hand2', fg='black',command=back).place(relx=0.60,rely=0.80)
    w1.mainloop()


if __name__ == '__main__':
    in_outf("A201")