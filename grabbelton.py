import random
from tkinter import font
import tkinter
from tkinter.constants import LEFT, ON, RIGHT
from tkinter.messagebox import showerror, showwarning, showinfo

window = tkinter.Tk()

wordsList = ["Money" , "Trip" , "Car" , "House" , "Job" , "Gold" , "Your dream!" , "Trip to the moon" , "Met your idol!" , "Become an actor in a movie"]

def wordChoice():
    global wordsList
    random_word = random.choice(wordsList)
    print("Congratulations, you grabbed an {}!".format(random_word))
    showinfo("Congratulations" , "Congratulations, you grabbed  {}!".format(random_word) )
    wordsList.remove(random_word)

window.title("Game")
window.geometry("500x500")
window.config(bg="yellow")

box = tkinter.Label(  
    text="Prees on the button and you will get an Item!",
    font=("Arial" , 15),
    fg="white",
    bg="Black"

)

box.pack(
    pady=10,
    padx=10,
    expand=True
     
)

btn = tkinter.Button(window)
btn.config(text="press hier", fg="white" , bg="black" , font=("Arial" , 14), command=wordChoice)
btn.pack(padx=9  , pady=10 , expand=True )




window.mainloop()