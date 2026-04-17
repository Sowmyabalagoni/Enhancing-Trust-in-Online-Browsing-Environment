import tkinter as tk
from tkinter import ttk
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

running = True

root = tk.Tk()
root.title("Browsing Hijack Detection System")
root.geometry("1200x650")

# STATUS
status = tk.Label(root,text="Status: Monitoring...",fg="green")
status.pack()

# BUTTONS
button_frame = tk.Frame(root)
button_frame.pack()

def start_monitor():
    global running
    running = True
    status.config(text="Status: Monitoring...",fg="green")

def stop_monitor():
    global running
    running = False
    status.config(text="Status: Stopped",fg="red")

start_btn = tk.Button(button_frame,text="Start Monitoring",command=start_monitor)
start_btn.pack(side=tk.LEFT,padx=10)

stop_btn = tk.Button(button_frame,text="Stop Monitoring",command=stop_monitor)
stop_btn.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(fill="both",expand=True)

# TABLE
columns=("Timestamp","Click","Scroll","Redirect","Prediction","Confidence")

tree = ttk.Treeview(frame,columns=columns,show="headings")

for col in columns:
    tree.heading(col,text=col)
    tree.column(col,width=120)

tree.pack(side="left",fill="both",expand=True)

# GRAPH
graph_frame = tk.Frame(frame)
graph_frame.pack(side="right")

fig,ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig,master=graph_frame)
canvas.get_tk_widget().pack()

counter = tk.Label(root,text="Normal:0  Hijacked:0")
counter.pack()

normal_history=[]
hijack_history=[]
time_step=[]
t=0

# MULTIPLE ALERT FUNCTION
def show_alert():

    alert=tk.Toplevel(root)
    alert.title("Hijacking Alert")
    alert.geometry("300x120")

    label=tk.Label(
        alert,
        text="⚠ WARNING!\nBrowsing Hijacking Detected!",
        fg="red",
        font=("Arial",12,"bold")
    )

    label.pack(pady=20)

    btn=tk.Button(alert,text="OK",command=alert.destroy)
    btn.pack()


def update():

    global t

    if running==False:
        root.after(2000,update)
        return

    try:

        res=requests.get("http://127.0.0.1:5000/logs")

        data=res.json()

        tree.delete(*tree.get_children())

        normal=0
        hijacked=0

        for row in data:

            tree.insert("",0,values=(
                row["timestamp"],
                row["click"],
                row["scroll"],
                row["redirect"],
                row["prediction"],
                row["confidence"]
            ))

            if row["prediction"]=="Normal":
                normal+=1
            else:
                hijacked+=1
                show_alert()

        counter.config(text=f"Normal:{normal}  Hijacked:{hijacked}")

        normal_history.append(normal)
        hijack_history.append(hijacked)
        time_step.append(t)

        t+=1

        ax.clear()

        ax.plot(time_step,normal_history,label="Normal",marker="o")
        ax.plot(time_step,hijack_history,label="Hijacked",marker="o")

        ax.set_title("Detections Over Time")
        ax.set_xlabel("Events")
        ax.set_ylabel("Count")

        ax.legend()

        canvas.draw()

    except:
        pass

    root.after(2000,update)

update()

root.mainloop()
