import tkinter
from tkinter import font

window = tkinter.Tk()

window.title("Clock")
window.geometry("1500x300")
window.config(bg="black")

time_display = tkinter.Label(
    window ,
    bg="black",
    fg="white",
    text="{} : {} : {}".format(0 , 0 , 0),
    font=("Arial" , 60)

    
)
time_display.pack(
    ipadx=100,
    ipady=50,
    expand=True,
)

 

def time_func():
    global time_display
    x = 00
    y = 00
    z = 00
    while x != 13:
        z = z + 1
        time = "{} : {} : {}".format(x , y , z)
        if z == 60:
            z = 0
            y = y + 1
        if y == 60:
            y = 0
            x = x + 1
        window.update()
        window.after(1000    )
        time_display.config(text=time , font=("Arial" , 60))
        print(time)
        
time_func()

window.mainloop()