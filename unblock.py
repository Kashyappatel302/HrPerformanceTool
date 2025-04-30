from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class Unblock_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Unblock Account")
        self.root.geometry("600x350+400+200")
        self.root.config(bg="white")

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_secq = StringVar()
        self.var_s_a = StringVar()

        Label(self.root, text="Unblock Account", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        Label(self.root, text="Username", bg="white", font=("Arial", 13)).place(x=50, y=60)
        Entry(self.root, textvariable=self.var_dob, font=("Arial", 13), bg="lightgray").place(x=200, y=60, width=300)

        Label(self.root, text="Name", bg="white", font=("Arial", 13)).place(x=50, y=100)
        Entry(self.root, textvariable=self.var_name, font=("Arial", 13), bg="lightgray").place(x=200, y=100, width=300)

        Label(self.root, text="Email", bg="white", font=("Arial", 13)).place(x=50, y=140)
        Entry(self.root, textvariable=self.var_email, font=("Arial", 13), bg="lightgray").place(x=200, y=140, width=300)

        Label(self.root, text="Security Question", bg="white", font=("Arial", 13)).place(x=50, y=180)
        self.txt_security_q = ttk.Combobox(self.root, textvariable=self.var_secq,
                                           values=("Select", "What is your favourite Movie?", "What is your favourite Colour?",
                                                   "What was your first pet?", "What is your best friend's name?", "What is your favourite car?"),
                                           font=("Arial", 11), state="readonly")
        self.txt_security_q.place(x=200, y=180, width=300)
        self.txt_security_q.current(0)

        Label(self.root, text="Answer", bg="white", font=("Arial", 13)).place(x=50, y=220)
        Entry(self.root, textvariable=self.var_s_a, font=("Arial", 13), bg="lightgray").place(x=200, y=220, width=300)

        Button(self.root, text="Unblock Now", font=("Arial", 15), bg="#4caf50", fg="white", cursor="hand2", command=self.unblock).place(x=220, y=270)

    def unblock(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM signup WHERE dob=? AND name=? AND email=? AND secq=? AND secp=?",
                        (self.var_dob.get(), self.var_name.get(), self.var_email.get(), self.var_secq.get(), self.var_s_a.get()))
            row = cur.fetchone()
            if row:
                cur.execute("UPDATE signup SET blocked=0, failed_attempts=0 WHERE dob=?", (self.var_dob.get(),))
                con.commit()
                messagebox.showinfo("Success", "Account has been unblocked", parent=self.root)
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Details do not match", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Unblock_System(root)
    root.mainloop()