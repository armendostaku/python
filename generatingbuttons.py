from tkinter import * 
import random
root = Tk()

def changing():
    colorsfg = ["red","green","black","blue","yellow"]
    colorsbg = ["black","white","blue","purple","brown"]
    btn = Button(root,text="You clicked",fg=random.choice(colorsfg),bg=random.choice(colorsbg))
    btn.pack()
     

btn = Button(root,text="Generate Buttons",width="10",fg="red",bg="black",command=changing)
btn.pack()

root.mainloop()
