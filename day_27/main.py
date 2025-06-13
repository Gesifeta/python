import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.geometry('300x600')

my_label = tk.Label(text="My first GUI", font=("Arial", 20, "bold"))
my_label.pack(side="left")

window.mainloop()