import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class TenantManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Tenant Management System")
        self.master.geometry("1000x600")

        self.create_widgets()
        self.load_tenants()

    def create_widgets(self):
        # Create Treeview
        self.tree = ttk.Treeview(self.master, columns=("APT NO", "Name", "Mobile", "Gender", "Block", "Sq Feet", "Amount", "Pay"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Define headings
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        # Add buttons
        tk.Button(self.master, text="Add Tenant", command=self.add_tenant).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.master, text="Update Tenant", command=self.update_tenant).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.master, text="Delete Tenant", command=self.delete_tenant).pack(side=tk.LEFT, padx=10, pady=10)

    def load_tenants(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT user_details.apt_no, name, mobile, gender, block, sq_feet, amount, 
                   CASE WHEN pay_status = 1 THEN 'PAID' ELSE 'NOT PAID' END as pay_status
            FROM user_details
            JOIN apartments ON user_details.apt_no = apartments.apt_no
        ''')
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def add_tenant(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Tenant")

        labels = ["APT NO", "Name", "Mobile", "Gender", "Amount"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        def save():
            apt_no, name, mobile, gender, amount = [e.get() for e in entries]
            try:
                amount = float(amount)
                pay_status = False if amount > 0 else True
                
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                
                # Check if apartment exists
                cursor.execute("SELECT block, sq_feet FROM apartments WHERE apt_no = ?", (apt_no,))
                apartment = cursor.fetchone()
                if not apartment:
                    messagebox.showerror("Error", "Apartment does not exist!")
                    return
                
                block, sq_feet = apartment

                cursor.execute('''
                    INSERT INTO user_details (apt_no, name, mobile, gender, amount, pay_status)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (apt_no, name, mobile, gender, amount, pay_status))
                
                conn.commit()
                conn.close()
                
                self.load_tenants()
                add_window.destroy()
                messagebox.showinfo("Success", "Tenant added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Apartment already occupied!")

        tk.Button(add_window, text="Save", command=save).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def update_tenant(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a tenant to update!")
            return

        values = self.tree.item(selected[0])['values']
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Tenant")

        labels = ["APT NO", "Name", "Mobile", "Gender", "Amount"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(update_window, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(update_window)
            entry.insert(0, values[i])
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        def save():
            apt_no, name, mobile, gender, amount = [e.get() for e in entries]
            try:
                amount = float(amount)
                pay_status = False if amount > 0 else True
                
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE user_details 
                    SET name = ?, mobile = ?, gender = ?, amount = ?, pay_status = ?
                    WHERE apt_no = ?
                ''', (name, mobile, gender, amount, pay_status, apt_no))
                
                conn.commit()
                conn.close()
                
                self.load_tenants()
                update_window.destroy()
                messagebox.showinfo("Success", "Tenant updated successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount!")

        tk.Button(update_window, text="Save", command=save).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def delete_tenant(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a tenant to delete!")
            return

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this tenant?"):
            apt_no = self.tree.item(selected[0])['values'][0]
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_details WHERE apt_no = ?", (apt_no,))
            conn.commit()
            conn.close()
            self.load_tenants()
            messagebox.showinfo("Success", "Tenant deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TenantManagement(root)
    root.mainloop()