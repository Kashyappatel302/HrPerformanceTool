from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Employee Details")
        self.root.geometry("1440x680+50+50")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ==== Title ====
        title = Label(self.root, text="Manage Employee Details",compound=LEFT,padx=50,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=15,width=1440,height=35)
        # ==== Variables ====
        self.var_employeeID = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_project = StringVar()
        self.var_j_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()


        # ==== Widgets ====
        lbl_employeeID = Label(self.root, text="Employee ID", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=120)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=240)
        lbl_state = Label(self.root, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=300)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=300, y=300)
        lbl_pin = Label(self.root, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=520, y=300)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=360)
        
        lbl_dob = Label(self.root, text="Date of Birth", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=120)
        lbl_j_date = Label(self.root, text="Joining date", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)
        lbl_project = Label(self.root, text="Project", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=240)
        
        
        
        
        # ===== Entry Fields =====
        self.txt_employeeID = Entry(self.root, textvariable=self.var_employeeID, font=("goudy old style", 15, "bold"), bg="lightgrey")
        self.txt_employeeID.place(x=140, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=140, y=120, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=140, y=180, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"), font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_gender.place(x=140, y=240, width=200)
        self.txt_gender.current(0)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=140, y=300, width=120)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=355, y=300, width=120)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=570, y=300, width=120)
       
        self.project_list=["Select"]
        self.fetch_project()
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=490, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=490, y=120, width=200)
        txt_j_date = Entry(self.root, textvariable=self.var_j_date, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=490, y=180, width=200)
        self.txt_project = ttk.Combobox(self.root, textvariable=self.var_project,values=self.project_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_project.place(x=490, y=240, width=200)
        self.txt_project.current(0)
       
        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightgrey")
        self.txt_address.place(x=140, y=360, width=550, height=200)
        
        # ===== Buttons =====
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=570, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=570, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=570, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#000000", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=570, width=110, height=40)

        # ===== Search Project Name =====
        self.var_search=StringVar()
        lbl_search_employeeID = Label(self.root, text="Search By Employee ID", font=("goudy old style", 15, "bold"), bg="white").place(x=750, y=70)
        txt_search_employeeID = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=980, y=70, width=200)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search).place(x=1200, y=70, width=110, height=28)
        
        # ===== Search Table Content =====
        self.P_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.P_Frame.place(x=750, y=110, width=650, height=340)

        scrolly=Scrollbar(self.P_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.P_Frame, orient=HORIZONTAL)
        
        self.EmployeeTable = ttk.Treeview(self.P_Frame, columns=("eid", "empID", "name", "email", "gender", "dob", "contact", "joining", "project", "state", "city", "pin", "address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid", text="Project-Employee ID")
        self.EmployeeTable.heading("empID", text="Employee ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("joining", text="Joining")
        self.EmployeeTable.heading("project", text="Project")
        self.EmployeeTable.heading("state", text="State")
        self.EmployeeTable.heading("city", text="City")
        self.EmployeeTable.heading("pin", text="PIN")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.column("eid", width=50)
        self.EmployeeTable.column("empID", width=100)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("joining", width=100)
        self.EmployeeTable.column("project", width=100)
        self.EmployeeTable.column("state", width=100)
        self.EmployeeTable.column("city", width=100)
        self.EmployeeTable.column("pin", width=100)
        self.EmployeeTable.column("address", width=200)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        
    # ======  ======
    def get_data(self, ev):
        self.txt_employeeID.config(state='readonly')
        r = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(r)
        row = content["values"]
        self.var_employeeID.set(row[1])
        self.var_name.set(row[2])
        self.var_email.set(row[3])
        self.var_gender.set(row[4])
        self.var_dob.set(row[5])
        self.var_contact.set(row[6])
        self.var_j_date.set(row[7])
        self.var_project.set(row[8])
        self.var_state.set(row[9])
        self.var_city.set(row[10])
        self.var_pin.set(row[11])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[12])

    def clear(self):
        self.show()
        self.var_employeeID.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_j_date.set("")
        self.var_project.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.txt_employeeID.config(state=NORMAL)
        self.var_search.set("")
    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_employeeID.get() == "":
                messagebox.showerror("Error", "Employee ID should be required", parent=self.root)
            else:
                cur.execute("select * from employee where empID=?", (self.var_employeeID.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select a Employee", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where empID=? and project=?", (self.var_employeeID.get(),self.var_project.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_employeeID.get() == "":
                messagebox.showerror("Error", "Employee ID should be required", parent=self.root)
            else:
                cur.execute("select * from employee where empID=? and project=?", (self.var_employeeID.get(),self.var_project.get()))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Employee ID already present in the particular project", parent=self.root)
                else:
                    cur.execute("insert into employee (empID, name, email, gender, dob, contact, joining, project, state, city, pin, address) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_employeeID.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_j_date.get(),
                        self.var_project.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
           
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_employeeID.get() == "":
                messagebox.showerror("Error", "Employee ID should be required", parent=self.root)
            else:
                cur.execute("select * from employee where empID=?", (self.var_employeeID.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Employee from List", parent=self.root)
                else:
                    cur.execute("update employee set name=?, email=?, gender=?, dob=?, contact=?, joining=?, project=?, state=?, city=?, pin=?, address=? where empID=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_j_date.get(),
                        self.var_project.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_employeeID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
 
    def fetch_project(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from project")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.project_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Employee ID is required to search", parent=self.root)
            else:
                cur.execute("SELECT rowid, * FROM employee WHERE empID=?", (self.var_search.get(),))
                rows = cur.fetchall()
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                if len(rows) != 0:
                    for row in rows:
                        # Rearranging data to match table columns
                        self.EmployeeTable.insert('', END, values=(row[0], row[1], row[2], row[3], row[4],
                                                                row[5], row[6], row[7], row[8], row[9],
                                                                row[10], row[11], row[12]))
                else:
                    messagebox.showinfo("Not Found", "No employee found with given ID", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    
    
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()