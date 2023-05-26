import time
import tkinter as tk

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label['text'] = timer
        time.sleep(1)
        t -= 1
    time_label['text'] = 'Time is up!'

root = tk.Tk()
root.title('Focus Timer')
time_label = tk.Label(root, font=('Helvetica', 48), text='25:00')
time_label.pack(pady=20)
start_button = tk.Button(root, text='Start', command=lambda: countdown(1500))
start_button.pack(pady=10)
root.mainloop()
