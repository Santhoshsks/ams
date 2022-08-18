from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import admin_login
import ast

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def base_update(k,v):
        key=k
        value=v
        file=open('base.txt','r+')
        d=file.read()
        global r
        r=ast.literal_eval(d)
        dict2={key:value}
        r.update(dict2)
        file.truncate(0)
        file.close()
        file=open('base.txt','w')
        w=file.write(str(r))

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def valid_phone(phn):
    if phn.isdigit() and len(phn)==10:
        return True
    return False

def valid_pwd(pwd):
    if len(pwd)>5:
        return True
    return False
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
class Tenant:
    def __init__(self,w):
        global DATA_DICT
        DATA_LIST=[['A001', '1798', '17103'], ['A002', '1798', '17103'], ['A003', '1388', '13659'], ['A004', '1388', '13659'], ['A005', '1110', '11324'], ['A006', '1110', '11324'], ['A007', '1388', '13659'], ['A008', '1388', '13659'], ['A101', '2010', '18884'], ['A102', '2010', '18884'], ['A103', '1480', '14432'], ['A104', '1480', '14432'], ['A105', '1150', '11660'], ['A106', '1150', '11660'], ['A107', '1480', '14432'], ['A108', '1480', '14432'], ['A201', '2010', '18884'], ['A202', '2010', '18884'], ['A203', '1480', '14432'], ['A204', '1480', '14432'], ['A205', '1150', '11660'], ['A206', '1150', '11660'], ['A207', '1480', '14432'], ['A208', '1480', '14432'], ['A301', '2010', '18884'], ['A302', '2010', '18884'], ['A303', '1480', '14432'], ['A304', '1480', '14432'], ['A305', '1150', '11660'], ['A306', '1150', '11660'], ['A307', '1480', '14432'], ['A308', '1480', '14432'], ['A401', '2010', '18884'], ['A402', '2010', '18884'], ['A403', '1480', '14432'], ['A404', '1480', '14432'], ['A405', '1150', '11660'], ['A406', '1150', '11660'], ['A407', '1480', '14432'], ['A408', '1480', '14432'], ['A501', '2010', '18884'], ['A502', '2010', '18884'], ['A503', '1480', '14432'], ['A504', '1480', '14432'], ['A505', '1150', '11660'], ['A506', '1150', '11660'], ['A507', '1480', '14432'], ['A508', '1480', '14432'], ['A601', '2010', '18884'], ['A602', '2010', '18884'], ['A603', '1480', '14432'], ['A604', '1480', '14432'], ['A605', '1150', '11660'], ['A606', '1150', '11660'], ['A607', '1480', '14432'], ['A608', '1480', '14432'], ['A701', '2010', '18884'], ['A702', '2010', '18884'], ['A703', '1480', '14432'], ['A704', '1480', '14432'], ['A705', '1150', '11660'], ['A706', '1150', '11660'], ['A707', '1480', '14432'], ['A708', '1480', '14432'], ['A801', '2010', '18884'], ['A802', '2010', '18884'], ['A803', '1480', '14432'], ['A804', '1480', '14432'], ['A805', '1150', '11660'], ['A806', '1150', '11660'], ['A807', '1480', '14432'], ['A808', '1480', '14432']]
        DATA_DICT={} #How it looks --->{'A001':['1798','17103'],'B001':['1798','17103'],...}
        for i in DATA_LIST:
            DATA_DICT[i[0]]=[i[1],i[2]]
            str1=i[0][1:]
            str2="B"+str1#To Replace A with B
            DATA_DICT[str2]=[i[1],i[2]]
        def logoutf():
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                self.sel.clear()
                self.w.destroy()
                admin_login.admin_loginf()

        def exitf():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=w)
            if sure == True:
                self.sel.clear()
                self.w.destroy()
                
        file=open('base.txt','r+')
        d=file.read()
        global Base_Dict
        Base_Dict=ast.literal_eval(d)

            
        self.w=w
        self.w.geometry("1366x768")
        self.w.resizable(0, 0)
        self.w.title("Tenant Management")

        
        self.label1 = Label(w)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/databasepng1.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(w)
        self.entry1.place(relx=0.680, rely=0.235, width=220, height=27)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(w)
        self.button1.place(relx=0.855, rely=0.236, width=76, height=26)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="Black")
        self.button1.configure(background="white")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_w)

        self.button2 = Button(w)
        self.button2.place(relx=0.076, rely=0.095, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#3047ff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="Black")
        self.button2.configure(background="white")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=logoutf)

        self.button3 = Button(w)
        self.button3.place(relx=0.070, rely=0.810, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#3047ff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="black")
        self.button3.configure(background="#37e42a")
        self.button3.configure(font="gotham")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD ACCOUNT""")
        self.button3.configure(command=self.add_w)

        self.button4 = Button(w)
        self.button4.place(relx=0.370, rely=0.810, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#3047ff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="Black")
        self.button4.configure(background="#f78520")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE ACCOUNT""")
        self.button4.configure(command=self.update_w)

        self.button5 = Button(w)
        self.button5.place(relx=0.670, rely=0.810, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#3047ff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="white")
        self.button5.configure(background="#fa2a0f")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE ACCOUNT""")
        self.button5.configure(command=self.delete_w)

        self.button6 = Button(w)
        self.button6.place(relx=0.861, rely=0.095, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#3047ff")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="Black")
        self.button6.configure(background="white")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(command=exitf)

        self.scrollbary = Scrollbar(w, orient=VERTICAL)
        self.tree = ttk.Treeview(w)
        self.tree.place(relx=0.06, rely=0.303, width=1168, height=350)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbary.place(relx=0.920, rely=0.303, width=22, height=350)
        
        self.tree.configure(
            columns=(
                "APT NO",
                "Name",
                "Mobile",
                "Gender",
                "Block",
                "Sq Feet",
                "Amount",
                "Pay"
                 ))

        self.tree.heading("APT NO", text="APT NO", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Mobile", text="Mobile", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)
        self.tree.heading("Block", text="Block", anchor=W)
        self.tree.heading("Sq Feet", text="Sq Feet", anchor=W)
        self.tree.heading("Amount", text="Amount", anchor=W)
        self.tree.heading("Pay", text="Pay", anchor=W)

        self.tree.column("#0", stretch=YES, minwidth=0, width=0)
        self.tree.column("#1", stretch=YES, minwidth=0, width=50)
        self.tree.column("#2", stretch=YES, minwidth=0, width=150)
        self.tree.column("#3", stretch=YES, minwidth=0, width=100)
        self.tree.column("#4", stretch=YES, minwidth=0, width=80)
        self.tree.column("#5", stretch=YES, minwidth=0, width=80)
        self.tree.column("#6", stretch=YES, minwidth=0, width=80)
        self.tree.column("#7", stretch=YES, minwidth=0, width=80)
        self.tree.column("#8", stretch=YES, minwidth=0, width=100)
        self.DisplayData()

    def DisplayData(self):
        acc = []
        for row in Base_Dict.values():
            acc.append(row)
        for data in acc:
            self.tree.insert("", "end", values=(data))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def search_w(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
            
        to_search = self.entry1.get()
        for search in val:
            if search==to_search.upper():
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Account with Name: {} found.".format(self.entry1.get()), parent=self.w)
                break
        else: 
            messagebox.showerror("Oops!!", "Account with Name: {} not found.".format(self.entry1.get()), parent=self.w)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def delete_w(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected Tenant?", parent=self.w)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
            
                
                for r in range(len(to_delete)):
                    for r2 in Base_Dict.keys():
                        if str(to_delete[r])==str(Base_Dict[r2][0]):
                            del Base_Dict[r2]
                            break
                
                file=open('base.txt','w')
                file.truncate(0)
                file.close()
                file=open('base.txt','w')
                file.write(str(Base_Dict))

                messagebox.showinfo("Success!!", "Account(s) deleted from database.", parent=self.w)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
                                  
        else:
            messagebox.showerror("Error!!","Please select an Tenant.", parent=self.w)
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def update_w(self):
        global vall
        vall = []
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        
        if len(self.sel)==1:
            self.w.destroy()
            global e_update
            e_update = Toplevel()
            page8 = Update_Tenant(e_update)   
            def on_leave(e):  
                page8.entry1.delete(0,'end') 
                page8.entry1.insert(0,vall[0])
            page8.entry1.bind("<FocusIn>", on_leave)
            page8.entry1.bind("<FocusOut>", on_leave)
            page8.entry1.insert(0,vall[0])
            page8.entry1.config(state= "disabled")
            page8.entry2.insert(0, vall[1])
            page8.entry3.insert(0, vall[2])
            page8.entry4.insert(0, vall[3])
            page8.entry5.insert(0, vall[6])
            e_update.mainloop()
          
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select an Tenant to update.")
        else:
            messagebox.showerror("Error","Can only update one Tenant at a time.")
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def add_w(self):
        self.w.destroy()
        global add_wind
        add_wind = Toplevel()
        add_Tenant(add_wind)
        
    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            w.destroy()
            admin_login.admin_loginf()
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
class add_Tenant:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Tenant")

        self.label1 = Label(add_wind)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_win.png")
        self.label1.configure(image=self.img)
        

        self.r1 = add_wind.register(self.testint)
        self.r2 = add_wind.register(self.testchar)

        self.entry1 = Entry(add_wind)
        self.entry1.place(relx=0.400, rely=0.246, width=453, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(add_wind)
        self.entry2.place(relx=0.400, rely=0.336, width=453, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry3 = Entry(add_wind)
        self.entry3.place(relx=0.400, rely=0.426, width=453, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(add_wind)
        self.entry4.place(relx=0.400, rely=0.516, width=453, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        

        self.entry5 = Entry(add_wind)
        self.entry5.place(relx=0.400, rely=0.606, width=453, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")
        self.entry5.configure(validate="key", validatecommand=(self.r1, "%P"))


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        
        self.button1 = Button(add_wind)
        self.button1.place(relx=0.408, rely=0.83, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="black")
        self.button1.configure(background="white")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(add_wind)
        self.button2.place(relx=0.526, rely=0.83, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#3047ff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="black")
        self.button2.configure(background="white")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

        def back():
            add_wind.destroy()
            run()

        Button(add_wind,width=6,text='<BACK',border=0,bg='white',fg='black',cursor="hand2",command=back).place(relx=0.880, rely=0.856)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
    
   
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def add(self):
        Apt_no = self.entry1.get()
        Name = self.entry2.get()
        Mobile = self.entry3.get()
        Gender = self.entry4.get()
        Amount = self.entry5.get()
        if Apt_no:
            if Apt_no.upper() not in Base_Dict.keys():
                if Apt_no.upper() in DATA_DICT.keys():
                    if self.testint(Mobile):
                        if valid_phone(Mobile):
                            if self.testchar(Name):
                                if  Gender.upper() =="M" or Gender.upper() =="F":
                                    if Amount:
                                        if int(Amount) == 0:
                                            data=[Apt_no.upper(),Name.title(),Mobile,Gender.upper(),Apt_no.upper()[0],DATA_DICT[Apt_no.upper()][0],int(Amount)+1600,"NOT PAID"]
                                            base_update(Apt_no.upper(),data)
                                            messagebox.showinfo("Success!!", "Account successfully added in database.", parent=add_wind)
                                            self.clearr()
                                        else:
                                            messagebox.showerror("Oops!", "Amount will be Zero for new account,Enter zero! ", parent=add_wind)
                                    else:
                                        messagebox.showerror("Oops!", "Please enter Amount.", parent=add_wind)
                                else:
                                    messagebox.showerror("Oops!", "Please enter Gender properly[m/f].", parent=add_wind)
                            else:
                                messagebox.showerror("Oops!", "Please enter name.", parent=add_wind)
                        else:
                            messagebox.showerror("Oops!", "Invalid phone number.", parent=add_wind)
                    else:
                        messagebox.showerror("Oops!", "Please enter Mobile Number.", parent=add_wind)
                else:
                    messagebox.showerror("Oops!", "Please enter Proper Apt No.", parent=add_wind)
            else:
                messagebox.showerror("Oops!", "User Already exist.", parent=add_wind)
        else:
            messagebox.showerror("Oops!", "Please enter Apt No.", parent=add_wind)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

class Update_Tenant:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Tenant")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_win.png")
        self.label1.configure(image=self.img)

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(relx=0.400, rely=0.246, width=453, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        
        self.entry2 = Entry(e_update)
        self.entry2.place(relx=0.400, rely=0.336, width=453, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry3 = Entry(e_update)
        self.entry3.place(relx=0.400, rely=0.426, width=453, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_update)
        self.entry4.place(relx=0.400, rely=0.516, width=453, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        
        self.entry5 = Entry(e_update)
        self.entry5.place(relx=0.400, rely=0.606, width=453, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")
        self.entry5.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.button1 = Button(e_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="black")
        self.button1.configure(background="white")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#3047ff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="black")
        self.button2.configure(background="white")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

        def back():
            e_update.destroy()
            run()

        Button(e_update,width=6,text='<BACK',border=0,bg='white',fg='black',cursor="hand2",command=back).place(relx=0.880, rely=0.856)

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    def update(self):
        Apt_no = self.entry1.get()
        Name = self.entry2.get()
        Mobile = self.entry3.get()
        Gender = self.entry4.get()
        Amount = self.entry5.get()

        if Apt_no :
            if self.testint(Mobile):
                if valid_phone(Mobile):
                    if self.testchar(Name):
                        if  Gender.upper() =="M" or Gender.upper() =="F":
                            if Amount:
                                if int(Amount)== 0:
                                    data=[Apt_no.upper(),Name.title(),Mobile,Gender.upper(),Apt_no.upper()[0],DATA_DICT[Apt_no.upper()][0],int(Amount),"PAID"]
                                    base_update(Apt_no.upper(),data)
                                    messagebox.showinfo("Success!!", "Account successfully Updated in database.", parent=e_update)
                                    self.clearr()
                                else:
                                    data=[Apt_no.upper(),Name.title(),Mobile,Gender.upper(),Apt_no.upper()[0],DATA_DICT[Apt_no.upper()][0],int(Amount),"NOT PAID"]
                                    base_update(Apt_no.upper(),data)
                                    messagebox.showinfo("Success!!", "Account successfully Updated in database.", parent=e_update)
                                    self.clearr()
                            else:
                                    messagebox.showerror("Oops!", "Please enter Amount.", parent=e_update)
                        else:
                            messagebox.showerror("Oops!", "Enter Gender properly m/f.", parent=e_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter name.", parent=e_update)
                else:
                    messagebox.showerror("Oops!", "Invalid phone number.", parent=e_update)
            else:
                messagebox.showerror("Oops!", "Please enter Mobile Number.", parent=e_update)
        else:
            messagebox.showerror("Oops!", "Please enter Apt No.", parent=e_update)

                
    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def run():
    global w
    w=Toplevel()
    w.geometry('1366x768')
    w.title('Data Base')
    w.resizable(0, 0)
    Tenant(w)
    w.mainloop()

if __name__ == '__main__':
    run()