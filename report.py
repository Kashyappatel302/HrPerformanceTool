from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from advanced_graph import AdvancedGraph  # Must be in same folder

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Reports")
        self.root.geometry("1440x680+50+50")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_employeeID = StringVar()
        self.var_name = StringVar()

        # ==== Title ====
        title = Label(self.root, text="Employee Performance Reports", compound=LEFT, padx=50,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=15, width=1440, height=35)

        lbl_search = Label(self.root, text="Select by Employee ID", font=("goudy old style", 20, "bold"),
                           bg="white").place(x=10, y=60)
        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="lightgray", command=self.clear).place(
            x=290, y=60, width=120, height=35)
        lbl_table = Label(self.root, text="Employee Reports", font=("goudy old style", 20, "bold"), bg="white").place(
            x=520, y=60)

        # ==== Table 1 ====
        self.P_Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        self.P_Frame1.place(x=10, y=110, width=400, height=500)

        scrolly1 = Scrollbar(self.P_Frame1, orient=VERTICAL)
        scrollx1 = Scrollbar(self.P_Frame1, orient=HORIZONTAL)
        self.ReportTable = ttk.Treeview(self.P_Frame1, columns=("eid", "name"), xscrollcommand=scrollx1.set,
                                        yscrollcommand=scrolly1.set)
        scrollx1.pack(side=BOTTOM, fill=X)
        scrolly1.pack(side=RIGHT, fill=Y)
        scrollx1.config(command=self.ReportTable.xview)
        scrolly1.config(command=self.ReportTable.yview)
        self.ReportTable.heading("eid", text="Employee ID")
        self.ReportTable.heading("name", text="Name")
        self.ReportTable["show"] = "headings"
        self.ReportTable.column("eid", width=100)
        self.ReportTable.column("name", width=100)
        self.ReportTable.pack(fill=BOTH, expand=1)
        self.ReportTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # ==== Table 2 ====
        self.P_Frame2 = Frame(self.root, bd=2, relief=RIDGE)
        self.P_Frame2.place(x=420, y=110, width=1000, height=250)

        scrolly2 = Scrollbar(self.P_Frame2, orient=VERTICAL)
        scrollx2 = Scrollbar(self.P_Frame2, orient=HORIZONTAL)

        self.ReportShowTable = ttk.Treeview(
            self.P_Frame2,
            columns=("eid", "name", "pname", "projectPerformance", "communication", "productivity", "creativity",
                     "integrity", "punctuality", "attendance"),
            xscrollcommand=scrollx2.set, yscrollcommand=scrolly2.set)

        scrollx2.pack(side=BOTTOM, fill=X)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrollx2.config(command=self.ReportShowTable.xview)
        scrolly2.config(command=self.ReportShowTable.yview)

        for col in self.ReportShowTable["columns"]:
            self.ReportShowTable.heading(col, text=col.replace("pname", "Project Name").title())
            self.ReportShowTable.column(col, width=100)

        self.ReportShowTable["show"] = "headings"
        self.ReportShowTable.pack(fill=BOTH, expand=1)
        self.ReportShowTable.bind("<ButtonRelease-1>", self.get_data2)
        self.show2()

        # ==== Graph Frame ====
        self.graph_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.graph_frame.place(x=420, y=370, width=1000, height=240)

        # ==== Button ====
        btn_advance = Button(self.root, text="Advanced Performance Details", font=("goudy old style", 15, "bold"),bg="#4caf50", fg="white", cursor="hand2", command=self.show_advanced_graph)
        btn_advance.place(x=1100, y=620, width=280, height=35)

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT DISTINCT empID, name FROM employee")
            rows = cur.fetchall()
            self.ReportTable.delete(*self.ReportTable.get_children())
            for row in rows:
                self.ReportTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show2(self, eid=None):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if eid:
                cur.execute(
                    "SELECT eid, name, pname, communication, productivity, creativity, integrity, punctuality, attendance FROM performance WHERE eid=?",
                    (eid,))
            else:
                cur.execute(
                    "SELECT eid, name, pname, communication, productivity, creativity, integrity, punctuality, attendance FROM performance")
            rows = cur.fetchall()
            self.ReportShowTable.delete(*self.ReportShowTable.get_children())
            for row in rows:
                try:
                    scores = list(map(float, row[3:]))
                    weights = [0.30, 0.25, 0.15, 0.15, 0.05, 0.10]
                    performance = round(sum([a * b for a, b in zip(scores, weights)]), 2)
                except:
                    performance = "N/A"
                new_row = row[:3] + (performance,) + row[3:]
                self.ReportShowTable.insert('', END, values=new_row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def get_data(self, ev):
        r = self.ReportTable.focus()
        content = self.ReportTable.item(r)
        row = content["values"]
        if row:
            self.var_employeeID.set(row[0])
            self.var_name.set(row[1])
            self.show2(row[0])
            self.draw_bar_graph(row[0])

    def get_data2(self, ev):
        r = self.ReportShowTable.focus()
        row = self.ReportShowTable.item(r)["values"]
        if row:
            self.var_employeeID.set(row[0])
            self.var_name.set(row[1])

    def draw_bar_graph(self, eid):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(
                "SELECT pname, communication, productivity, creativity, integrity, punctuality, attendance FROM performance WHERE eid=?",
                (eid,))
            rows = cur.fetchall()
            if not rows:
                return
            x = []
            y = []
            for row in rows:
                x.append(row[0])
                try:
                    scores = list(map(float, row[1:]))
                    weights = [0.30, 0.25, 0.15, 0.15, 0.05, 0.10]
                    performance = round(sum([a * b for a, b in zip(scores, weights)]), 2)
                except:
                    performance = 0
                y.append(performance)

            fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)
            ax.bar(x, y, color="#2196f3")
            ax.set_title("Project-wise Performance")
            ax.set_xlabel("Project Name")
            ax.set_ylabel("Performance Score")
            ax.set_ylim(0, 5)

            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=1)
        except Exception as ex:
            messagebox.showerror("Error", f"Graph error: {str(ex)}")
        finally:
            con.close()

    def show_advanced_graph(self):
        if not self.var_employeeID.get():
            messagebox.showwarning("Warning", "Please select an employee first", parent=self.root)
            return
        new_win = Toplevel(self.root)
        AdvancedGraph(new_win, self.var_employeeID.get())

    def clear(self):
        self.var_employeeID.set("")
        self.var_name.set("")
        self.ReportTable.selection_remove(self.ReportTable.selection())
        self.ReportShowTable.selection_remove(self.ReportShowTable.selection())
        self.show2()
        for widget in self.graph_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)

    def on_closing():
        root.quit()  # Stops the mainloop
        root.destroy()  # Destroys the window

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
