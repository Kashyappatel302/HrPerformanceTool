from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import re


class Signup_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("960x400+300+200")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_name=StringVar()
        self.var_lname=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_s_q=StringVar()
        self.var_s_a=StringVar()
        
        
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=30)
        lbl_last_name = Label(self.root, text="Last Name", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=30)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=100)
        lbl_dob = Label(self.root, text="Username", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=100)
        lbl_security_q = Label(self.root, text="Security Question", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=170)
        lbl_security_ans = Label(self.root, text="Security Answer", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=170)
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=240)
        lbl_confirm_password = Label(self.root, text="Confrim Password", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=240)
        
        
        
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=220, y=30, width=200)
        txt_lastname = Entry(self.root, textvariable=self.var_lname, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=30, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=100, width=200)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=220, y=100, width=200)
        txt_security_ans = Entry(self.root, textvariable=self.var_s_a, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=170, width=200)
        self.txt_security_q = ttk.Combobox(self.root, textvariable=self.var_s_q,values=("Select","What is your favourite Movie?","What is your favourite Colour?","What was your first pet?","What is your best friend's name?","What is your favourite car?"), font=("goudy old style", 11, "bold"), state="readonly", justify=CENTER)
        self.txt_security_q.place(x=220, y=170, width=200,height=36)
        self.txt_security_q.current(0)
        txt_password = Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=220, y=240, width=200)
        txt_confirm_password = Entry(self.root, textvariable=self.var_cpass, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=240, width=200)
        
        
        btn_signup = Button(self.root, text="Sign Up", font=("goudy old style", 20, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add).place(x=380, y=310, width=200, height=36)
        


    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_dob.get() == "" or self.var_s_q.get() == "" or self.var_s_a.get() == "" or self.var_pass.get() == "" or self.var_cpass.get() == "" or self.var_s_q.get() == "Select":
                messagebox.showerror("Error", "All fields are required", parent=self.root)

            elif self.var_pass.get() != self.var_cpass.get():
                messagebox.showerror("Error", "Password and Confirm Password do not match", parent=self.root)

            elif len(self.var_pass.get()) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long", parent=self.root)

            elif not re.search(r"[A-Z]", self.var_pass.get()):
                messagebox.showerror("Error", "Password must include at least one uppercase letter", parent=self.root)

            elif not re.search(r"[a-z]", self.var_pass.get()):
                messagebox.showerror("Error", "Password must include at least one lowercase letter", parent=self.root)

            elif not re.search(r"[0-9]", self.var_pass.get()):
                messagebox.showerror("Error", "Password must include at least one digit", parent=self.root)

            else:
                
                cur.execute("SELECT * FROM signup WHERE email=?", (self.var_email.get(),))
                row_email = cur.fetchone()
                if row_email is not None:
                    messagebox.showerror("Error", "Email already exists", parent=self.root)
                    return

                
                cur.execute("SELECT * FROM signup WHERE dob=?", (self.var_dob.get(),))
                row_username = cur.fetchone()
                if row_username is not None:
                    messagebox.showerror("Error", "Username already taken", parent=self.root)
                    return

                else:
                    cur.execute("INSERT INTO signup (name, lastname, email, dob, secq, secp, password) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                        self.var_name.get(),
                        self.var_lname.get(),
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_s_q.get(),
                        self.var_s_a.get(),
                        self.var_pass.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Account added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)




        
if __name__ == "__main__":
    root = Tk()
    obj = Signup_System(root)
    root.mainloop()