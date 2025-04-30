from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AdvancedGraph:
    def __init__(self, root, eid):
        self.root = root
        self.root.title("Advanced Performance Graph")
        self.root.geometry("1200x600+200+75")
        self.root.config(bg="white")

        self.graph_frame = Frame(self.root, bg="white")
        self.graph_frame.pack(fill=BOTH, expand=True)

        self.draw_advanced_graph(eid)

    def draw_advanced_graph(self, eid):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT pname, communication, productivity, creativity, integrity, punctuality, attendance FROM performance WHERE eid=?", (eid,))
            rows = cur.fetchall()

            if not rows:
                return

            projects = [row[0] for row in rows]
            metrics = {
                "Communication": [],
                "Productivity": [],
                "Creativity": [],
                "Integrity": [],
                "Punctuality": [],
                "Attendance": [],
            }

            for row in rows:
                try:
                    metrics["Communication"].append(float(row[1]))
                    metrics["Productivity"].append(float(row[2]))
                    metrics["Creativity"].append(float(row[3]))
                    metrics["Integrity"].append(float(row[4]))
                    metrics["Punctuality"].append(float(row[5]))
                    metrics["Attendance"].append(float(row[6]))
                except:
                    continue

            fig, ax = plt.subplots(figsize=(10, 4), dpi=100)
            for key, values in metrics.items():
                ax.plot(projects, values, label=key, marker='o')

            ax.set_title("Performance Breakdown per Project")
            ax.set_xlabel("Project Name")
            ax.set_ylabel("Score")
            ax.set_ylim(0, 5)
            ax.legend(loc="upper right")

            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=1)
            plt.close(fig)

        except Exception as ex:
            print("Graph error:", str(ex))
        finally:
            con.close()
