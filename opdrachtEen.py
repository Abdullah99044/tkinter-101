import tkinter
import random
from typing import Text

window = tkinter.Tk()

window.title("“My First Window”")
window.geometry("50x50")

colors = ["black" , "yellow" , "pink" , "blue" , "green" , "gray"]
window.config(bg="white") 

color = random.choice(colors)



def func1():  
    global colors
    x = 50
    y = 50
    for i in range(6):
        color = random.choice(colors)
        
        x+=50
        y+=50
        print(i)
        for i in range(1):
            window.update()
            window.after(2000 , window.config(bg=color) , window.geometry("{}x{}".format(x , y )) )
            window.update()
            print(x , y)
        

         
 
     
    
 
        


window.after(200 ,func1)    
   
 
 


for i in range(3):
    window.mainloop()