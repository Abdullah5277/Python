import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Alarm Clock")
alarm_time = ""

def time():
    current_time=strftime('%H:%M:%S')
    time_label.config(text=current_time)
    
    if current_time ==alarm_time:
         print("Wake up")
    root.after(1000,time)    
    
# Create a label to display the time
time_label=tk.Label(root,font=('calbiri',40,'bold'),background='purple',foreground='white')
time_label.pack(anchor='center')

def set_alarm():
    global alarm_time
    alarm_time = entry.get()
    print(f"Alarm set for {alarm_time}")

# Entry widget to input alarm time
entry = tk.Entry(root, font=('calibri', 20))
entry.pack(pady=20)

# Button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm, font=('calibri', 15))
set_button.pack()
   
# Start the time update
time()

root.mainloop()   