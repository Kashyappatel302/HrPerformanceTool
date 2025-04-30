from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class ProjectClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Project Details")
        self.root.geometry("1440x680+50+50")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # ==== Title ====
        title = Label(self.root, text="Manage Project Details",compound=LEFT,padx=50,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=15,width=1440,height=35)
        # ==== Variables ====
        self.var_project = StringVar()
        self.var_duration = StringVar()
        self.var_budget = StringVar()

        # ==== Widgets ====
        lbl_projectName = Label(self.root, text="Project Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=70)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_budget = Label(self.root, text="Budget", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=210)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=280)
        
        # ===== Entry Fields =====
        self.txt_projectName = Entry(self.root, textvariable=self.var_project, font=("goudy old style", 15, "bold"), bg="lightgrey")
        self.txt_projectName.place(x=140, y=70, width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=140, y=140, width=200)
        txt_budget = Entry(self.root, textvariable=self.var_budget, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=140, y=210, width=200)
        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightgrey")
        self.txt_description.place(x=140, y=280, width=550, height=200)
        
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
        lbl_search_projectName = Label(self.root, text="Search By Project Name", font=("goudy old style", 15, "bold"), bg="white").place(x=750, y=70)
        txt_search_projectName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightgrey").place(x=980, y=70, width=200)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.search).place(x=1200, y=70, width=110, height=28)
        
        # ===== Search Table Content =====
        self.P_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.P_Frame.place(x=750, y=110, width=650, height=340)

        scrolly=Scrollbar(self.P_Frame, orient=VERTICAL)
        scrollx=Scrollbar(self.P_Frame, orient=HORIZONTAL)
        
        self.ProjectTable = ttk.Treeview(self.P_Frame, columns=("pid", "name", "duration", "budget", "description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProjectTable.xview)
        scrolly.config(command=self.ProjectTable.yview)
        
        self.ProjectTable.heading("pid", text="Project ID")
        self.ProjectTable.heading("name", text="Name")
        self.ProjectTable.heading("duration", text="Duration")
        self.ProjectTable.heading("budget", text="Budget")
        self.ProjectTable.heading("description", text="Description")
        self.ProjectTable["show"] = "headings"
        self.ProjectTable.column("pid", width=120)
        self.ProjectTable.column("name", width=120)
        self.ProjectTable.column("duration", width=120)
        self.ProjectTable.column("budget", width=120)
        self.ProjectTable.column("description", width=200)
        self.ProjectTable.pack(fill=BOTH,expand=1)
        self.ProjectTable.bind("<ButtonRelease-1>", self.get_data) 
        self.show()
        
    # ======  ======
    def get_data(self, ev):
        self.txt_projectName.config(state='readonly')
        r = self.ProjectTable.focus()
        content = self.ProjectTable.item(r)
        row = content["values"]
        self.var_project.set(row[1])
        self.var_duration.set(row[2])
        self.var_budget.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])

    def clear(self):
        self.show()
        self.var_project.set("")
        self.var_duration.set("")
        self.var_budget.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_projectName.config(state=NORMAL)
    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_project.get() == "":
                messagebox.showerror("Error", "Project Name should be required", parent=self.root)
            else:
                cur.execute("select * from project where name=?", (self.var_project.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select a Project", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from project where name=?", (self.var_project.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Project deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_project.get() == "":
                messagebox.showerror("Error", "Project Name should be required", parent=self.root)
            else:
                cur.execute("select * from project where name=?", (self.var_project.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Project Name already present", parent=self.root)
                else:
                    cur.execute("insert into project (name, duration, budget, description) values(?, ?, ?, ?)", (
                        self.var_project.get(),
                        self.var_duration.get(),
                        self.var_budget.get(),
                        self.txt_description.get("1.0",END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Project Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
           
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_project.get() == "":
                messagebox.showerror("Error", "Project Name should be required", parent=self.root)
            else:
                cur.execute("select * from project where name=?", (self.var_project.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Project from List", parent=self.root)
                else:
                    cur.execute("update project set duration=?, budget=?, description=? where name=?", (
                        self.var_duration.get(),
                        self.var_budget.get(),
                        self.txt_description.get("1.0",END),
                        self.var_project.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Project Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from project")
            rows=cur.fetchall()
            self.ProjectTable.delete(*self.ProjectTable.get_children())
            for row in rows:
                self.ProjectTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from project where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.ProjectTable.delete(*self.ProjectTable.get_children())
            for row in rows:
                self.ProjectTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    
if __name__ == "__main__":
    root = Tk()
    obj = ProjectClass(root)
    root.mainloop()