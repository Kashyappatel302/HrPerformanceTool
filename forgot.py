from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class Forgotp_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Recover Password")
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
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=30)
        lbl_dob = Label(self.root, text="Username", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=100)
        lbl_security_q = Label(self.root, text="Security Question", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=170)
        lbl_security_ans = Label(self.root, text="Security Answer", font=("goudy old style", 20, "bold"), bg="white").place(x=480, y=170)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=220, y=30, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=30, width=200)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=220, y=100, width=200)
        txt_security_ans = Entry(self.root, textvariable=self.var_s_a, font=("goudy old style", 20, "bold"), bg="lightgrey").place(x=700, y=170, width=200)
        self.txt_security_q = ttk.Combobox(self.root, textvariable=self.var_s_q,values=("Select","What is your favourite Movie?","What is your favourite Colour?","What was your first pet?","What is your best friend's name?","What is your favourite car?"), font=("goudy old style", 11, "bold"), state="readonly", justify=CENTER)
        self.txt_security_q.place(x=220, y=170, width=200,height=36)
        self.txt_security_q.current(0)
        
        
        btn_find_password = Button(self.root, text="Find Password", font=("goudy old style", 20, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.find).place(x=380, y=310, width=200, height=36)

        
        
    def find(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if (
                self.var_name.get() == "" or self.var_email.get() == "" or self.var_dob.get() == ""
                or self.var_s_q.get() == "Select" or self.var_s_a.get() == ""
            ):
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            cur.execute(
                "SELECT password FROM signup WHERE name=? AND dob=? AND email=? AND secq=? AND secp=?",
                (self.var_name.get(), self.var_dob.get(), self.var_email.get(), self.var_s_q.get(), self.var_s_a.get())
            )
            row = cur.fetchone()
            if row:
                messagebox.showinfo("Recovered Password", f"Your password is: {row[0]}", parent=self.root)
            else:
                messagebox.showerror("Error", "No matching user found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

        


if __name__ == "__main__":
    root = Tk()
    obj = Forgotp_System(root)
    root.mainloop()