import tkinter as tk
from tkinter import font
from tkinter.constants import CENTER

window = tk.Tk()

window.title("Hello")
window.geometry("200x200")
window.config(bg="black")

box = tk.Label(
    window,
    text="Hello tkinter",
    bg="white",
    fg="green"
)

box.pack(
    ipadx=50,
    ipady=50,
    expand=True,
)

window.mainloop()