from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from project import ProjectClass
from employee import employeeClass
from performance import performanceClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("HR Performance Tool")
        self.root.geometry("1960x790+-10+0")
        self.root.config(bg="white")

        # ==== Icons ====
        self.logo_dash = ImageTk.PhotoImage(Image.open("Images/logo_p.png").resize((50, 50), Image.Resampling.LANCZOS))
        
        # ==== Title ====
        title = Label(self.root, text="HR Performance Tool",image=self.logo_dash,compound=LEFT,padx=50, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        # ==== Menu =====
        M_Frame = LabelFrame(self.root,text="Menus",font=("times new roman", 15),bg="white")
        M_Frame.place(x=10, y=70, width=1520, height=80)

        btn_project = Button(M_Frame,text="Project",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_project).place(x=20, y=5, width=230, height=40)
        btn_employee = Button(M_Frame,text="Employee",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_employee).place(x=270, y=5, width=230, height=40)
        btn_performance = Button(M_Frame,text="Performance",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_performance).place(x=520, y=5, width=230, height=40)
        btn_view = Button(M_Frame,text="View Performance",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_report).place(x=765, y=5, width=240, height=40)
        btn_logout = Button(M_Frame,text="Logout",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1020, y=5, width=230, height=40)
        btn_exit = Button(M_Frame,text="Exit",font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1270, y=5, width=230, height=40)
        
        # ====content_window====
        self.bg_img = Image.open("images/bg.jpeg")
        self.bg_img = self.bg_img.resize((1040, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=230, y=180, width=1040, height=350)

        # ==== Update Details ====
        self.lbl_project = Label(self.root, text="Total Projects\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_project.place(x=230, y=530, width=300, height=100)
        
        self.lbl_employee = Label(self.root, text="Total Employees\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_employee.place(x=600, y=530, width=300, height=100)
        
        self.lbl_performance = Label(self.root, text="Total Performances\n[ 0 ]", font=("goudy old style", 20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_performance.place(x=970, y=530, width=300, height=100)

        self.update_details()
        # ==== Footer ====
        footer = Label(self.root, text="HR Performance Tool\nContact Us for any Technical issue: 8980944344",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
 
    def add_project(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProjectClass(self.new_win)

    def add_employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def add_performance(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=performanceClass(self.new_win)
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
        
    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from project")
            cr = cur.fetchall()
            self.lbl_project.config(text=f"Total Projects\n[ {str(len(cr))} ]")

            cur.execute("SELECT COUNT(DISTINCT empID) FROM employee")
            unique_employees = cur.fetchone()[0]
            self.lbl_employee.config(text=f"Total Employees [{str(unique_employees)}]")

            cur.execute("select * from performance")
            cr2 = cur.fetchall()
            self.lbl_performance.config(text=f"Total Performances\n[ {str(len(cr2))} ]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        finally:
            con.close()

        # 🔁 Schedule the next update after 5 seconds (adjust as needed)
        self.root.after(5000, self.update_details)






if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()