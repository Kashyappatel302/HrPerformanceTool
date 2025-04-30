from tkinter import *
from signup import Signup_System
from tkinter import messagebox
import sqlite3
from dashboard import RMS
from forgot import Forgotp_System
from unblock import Unblock_System

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("960x690+300+50")
        
        
        #===Login_Frame===
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=305, y=100, width=350, height=460)
        
        self.username=StringVar()
        self.password=StringVar()

        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_user = Label(login_frame, text="Username", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)
        txt_username = Entry(login_frame,textvariable=self.username, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=140, width=250)
        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=200)
        txt_password = Entry(login_frame,textvariable=self.password,show='*', font=("times new roman", 15), bg="#ECECEC").place(x=50, y=240, width=250)

        
        btn_login = Button(login_frame, text="Log In", font=("Arial Rounded MT Bold", 15),bg='#00B0F0',activebackground="#00B0F0", fg="white", activeforeground="white",cursor='hand2',command=self.login).place(x=50,y=300,width=250,height=35)
        hr = Label(login_frame, bg="lightgray").place(x=50, y=360, width=250, height=2)
        or_ = Label(login_frame,text='OR',bg='white', fg="lightgray",font=('times new roman',15,'bold')).place(x=150, y=347)
        
        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 13),bg='white', fg="#00759E",bd=0,activebackground='white',activeforeground='#00759E',command=self.add_forgot).place(x=110,y=390)

        btn_unblock = Button(login_frame, text="Unblock Account", font=("times new roman", 13), bg='white', fg="#00759E", bd=0,activebackground='white', activeforeground='#00759E', command=self.add_unblock)
        btn_unblock.place(x=110, y=420)

        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=305, y=565, width=350, height=60)
        
        lbl_reg = Label(register_frame, text="Don't have an account?", font=("times new roman", 13), bg="white").place(x=55,y=20)
        btn_signup = Button(register_frame, text="Sign Up", font=("times new roman", 13, "bold"),bg='white',fg='#00759E',activebackground='white',activeforeground='#00759E', bd=0,command=self.add_signup).place(x=215, y=17)


    def login(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.password.get() == "" or self.username.get() == "":
                messagebox.showerror("Error", "Username and Password both are required", parent=self.root)
                return

            cur.execute("SELECT password, failed_attempts, blocked FROM signup WHERE dob=?", (self.username.get(),))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Username not found", parent=self.root)
            elif row[2] == 1:
                messagebox.showerror("Blocked", "Account is blocked due to multiple failed attempts.\nClick 'Unblock Account' to recover.", parent=self.root)
            elif row[0] == self.password.get():
                cur.execute("UPDATE signup SET failed_attempts=0 WHERE dob=?", (self.username.get(),))
                con.commit()
                messagebox.showinfo("Success", "Login Successful", parent=self.root)
                self.add_dashboard()
            else:
                failed = row[1] + 1
                if failed >= 3:
                    cur.execute("UPDATE signup SET blocked=1 WHERE dob=?", (self.username.get(),))
                    messagebox.showerror("Blocked", "Account blocked after 3 failed attempts", parent=self.root)
                else:
                    cur.execute("UPDATE signup SET failed_attempts=? WHERE dob=?", (failed, self.username.get()))
                    messagebox.showerror("Error", f"Incorrect password. {3 - failed} attempts left.", parent=self.root)
                con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)





    def add_signup(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Signup_System(self.new_win)
        

    def add_dashboard(self):
        self.root.destroy()
        root = Tk()
        login = RMS(root)
        root.mainloop()


    def add_forgot(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Forgotp_System(self.new_win)
        
    
    def add_unblock(self):
        self.new_win = Toplevel(self.root)
        from unblock import Unblock_System
        self.new_obj = Unblock_System(self.new_win)
        


if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
