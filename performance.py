from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class performanceClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Performance Details")
        self.root.geometry("1440x680+50+50")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ==== Title ====
        title = Label(self.root, text="Add Employee Performance Details",compound=LEFT,padx=50,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=15,width=1440,height=35)
        
        # ==== Variables ====
        self.var_project=StringVar()
        self.var_employeeID=StringVar()
        self.var_name=StringVar()
        self.var_communication=StringVar()
        self.var_productivity=StringVar()
        self.var_creativity=StringVar()
        self.var_integrity=StringVar()
        self.var_punctuality=StringVar()
        self.var_attendance=StringVar()
        self.var_search=StringVar()
        
        
        
        # ===== widget ======
        lbl_project = Label(self.root, text="Project", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_employeeID = Label(self.root, text="Employee ID", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        lbl_communication = Label(self.root, text="Communication", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=120)
        lbl_productivity = Label(self.root, text="Productivity", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)
        lbl_creativity = Label(self.root, text="Creativity", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=240)        
        lbl_integrity = Label(self.root, text="Integrity", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=300)
        lbl_punctuality = Label(self.root, text="Punctuality", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=360)
        lbl_attendance = Label(self.root, text="Attendance", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=420)
        
        
        self.project_list=["Select"]
        self.fetch_project()
        self.txt_project = ttk.Combobox(self.root, textvariable=self.var_project,values=self.project_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_project.place(x=140, y=60, width=200)
        self.txt_project.current(0)
        btn_search1 = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search1).place(x=10, y=120, width=110, height=28)
       
        self.employee_list=["Select"]
        #function
        self.txt_employeeID = ttk.Combobox(self.root, textvariable=self.var_employeeID,values=self.employee_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_employeeID.place(x=140, y=180, width=200)
        self.txt_employeeID.current(0)
        btn_search2 = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search2).place(x=10, y=240, width=110, height=28)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightgrey",state="readonly").place(x=500, y=60, width=200)
        self.score_list=["Select","0","1","2","3","4","5"]
        self.txt_communication = ttk.Combobox(self.root, textvariable=self.var_communication,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_communication.place(x=500, y=120, width=200)
        self.txt_communication.current(0)
        self.txt_productivity = ttk.Combobox(self.root, textvariable=self.var_productivity,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_productivity.place(x=500, y=180, width=200)
        self.txt_productivity.current(0)
        self.txt_creativity = ttk.Combobox(self.root, textvariable=self.var_creativity,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_creativity.place(x=500, y=240, width=200)
        self.txt_creativity.current(0)
        self.txt_integrity = ttk.Combobox(self.root, textvariable=self.var_integrity,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_integrity.place(x=500, y=300, width=200)
        self.txt_integrity.current(0)
        self.txt_punctuality = ttk.Combobox(self.root, textvariable=self.var_punctuality,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_punctuality.place(x=500, y=360, width=200)
        self.txt_punctuality.current(0)
        self.txt_attendance = ttk.Combobox(self.root, textvariable=self.var_attendance,values=self.score_list, font=("goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_attendance.place(x=500, y=420, width=200)
        self.txt_attendance.current(0)
        
        
        btn_submit = Button(self.root, text="Submit", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2",command=self.add).place(x=360, y=480, width=120, height=35)
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2",command=self.clear).place(x=490, y=480, width=120, height=35)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=620, y=480, width=120, height=35)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=750, y=480, width=120, height=35)

        
        # ===== Search Table Content =====
        self.P_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.P_Frame.place(x=750, y=110, width=650, height=340)

        scrolly=Scrollbar(self.P_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.P_Frame, orient=HORIZONTAL)
        
        self.PerformanceTable = ttk.Treeview(self.P_Frame, columns=( "eid", "pname", "name", "communication", "productivity", "creativity", "integrity", "punctuality", "attendance"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.PerformanceTable.xview)
        scrolly.config(command=self.PerformanceTable.yview)
        
        self.PerformanceTable.heading("eid", text="Employee ID")
        self.PerformanceTable.heading("pname", text="Project Name")
        self.PerformanceTable.heading("name", text="Name")
        self.PerformanceTable.heading("communication", text="Communication")
        self.PerformanceTable.heading("productivity", text="Productivity")
        self.PerformanceTable.heading("creativity", text="Creativity")
        self.PerformanceTable.heading("integrity", text="Integrity")
        self.PerformanceTable.heading("punctuality", text="Punctuality")
        self.PerformanceTable.heading("attendance", text="Attendnace")
        self.PerformanceTable["show"] = "headings"
        self.PerformanceTable.column("eid", width=100)
        self.PerformanceTable.column("pname", width=100)
        self.PerformanceTable.column("name", width=100)
        self.PerformanceTable.column("communication", width=100)
        self.PerformanceTable.column("productivity", width=100)
        self.PerformanceTable.column("creativity", width=100)
        self.PerformanceTable.column("integrity", width=100)
        self.PerformanceTable.column("punctuality", width=100)
        self.PerformanceTable.column("attendance", width=100)
        self.PerformanceTable.pack(fill=BOTH,expand=1)
        self.PerformanceTable.bind("<ButtonRelease-1>", self.get_data) 
        self.show()
        
        
        
    def get_data(self, ev):
        self.txt_employeeID.config(state='readonly')
        r = self.PerformanceTable.focus()
        content = self.PerformanceTable.item(r)
        row = content["values"]
        self.var_employeeID.set(row[0])
        self.var_project.set(row[1])
        self.var_name.set(row[2])
        self.var_communication.set(row[3])
        self.var_productivity.set(row[4])
        self.var_creativity.set(row[5])
        self.var_integrity.set(row[6])
        self.var_punctuality.set(row[7])
        self.var_attendance.set(row[8])
        self.show()
        
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select eid,pname,name,communication,productivity,creativity,integrity,punctuality,attendance from performance")
            rows=cur.fetchall()
            self.PerformanceTable.delete(*self.PerformanceTable.get_children())
            for row in rows:
                self.PerformanceTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
        


    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_employeeID.get() == "":
                messagebox.showerror("Error", "Employee ID should be required", parent=self.root)
            else:
                cur.execute("select * from performance where eid=?", (self.var_employeeID.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select a Employee", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from performance where eid=? and pname=?", (self.var_employeeID.get(),self.var_project.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()


    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_employeeID.get() == "":
                messagebox.showerror("Error", "Employee ID should be required", parent=self.root)
            else:
                cur.execute("select * from performance where eid=? and pname=?", (self.var_employeeID.get(),self.var_project.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Employee from List", parent=self.root)
                else:
                    cur.execute("update performance set  pname=?, name=?, communication=?, productivity=?, creativity=?, integrity=?, punctuality=?, attendance=? where eid=?", (
                        self.var_project.get(),
                        self.var_name.get(),
                        self.var_communication.get(),
                        self.var_productivity.get(),
                        self.var_creativity.get(),
                        self.var_integrity.get(),
                        self.var_punctuality.get(),
                        self.var_attendance.get(),
                        self.var_employeeID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Performance Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()


    def search1(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            selected_project = self.var_project.get()
            if selected_project == "Select":
                messagebox.showerror("Error", "Please select a project first")
                return

            cur.execute("SELECT empID FROM employee WHERE project=?", (selected_project,))
            rows = cur.fetchall()

            self.employee_list = ["Select"]  # Clear previous entries
            if rows:
                self.employee_list.extend([row[0] for row in rows])

            self.txt_employeeID["values"] = self.employee_list  # Update dropdown
            self.txt_employeeID.current(0)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()


    def search2(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from employee where empID=?", (self.var_employeeID.get(),))
            row=cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
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
            


    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_productivity.get() == "Select" or self.var_communication.get() == "Select" or self.var_creativity.get() == "Select" or self.var_integrity.get() == "Select" or self.var_punctuality.get() == "Select" or self.var_attendance.get() == "Select":
                messagebox.showerror("Error", "All performance fields should be required", parent=self.root)
            else:
                cur.execute("select * from performance where name=? and pname=?", (self.var_name.get(), self.var_project.get()))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Employee performace already present", parent=self.root)
                else:
                    cur.execute("insert into performance (eid, pname, name, communication, productivity, creativity, integrity, punctuality, attendance) values(?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_employeeID.get(),
                        self.var_project.get(),
                        self.var_name.get(),
                        self.var_communication.get(),
                        self.var_productivity.get(),
                        self.var_creativity.get(),
                        self.var_integrity.get(),
                        self.var_punctuality.get(),
                        self.var_attendance.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee performance Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.var_communication.set("Select")
        self.var_productivity.set("Select")
        self.var_creativity.set("Select")
        self.var_integrity.set("Select")
        self.var_punctuality.set("Select")
        self.var_attendance.set("Select")


        
if __name__ == "__main__":
    root = Tk()
    obj = performanceClass(root)
    root.mainloop()