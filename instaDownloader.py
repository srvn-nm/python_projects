from tkinter import *

window = Tk()
window.geometry("600x600")
window.maxsize(800,800)
window.minsize(400,400)
window.title("Instagram Profile Downloader")

label = Label(window,text="Hello Instagram!")
label.pack()

def buttonFunc():
    print("You pressed the button! >-<")
    button.config(text="Downloaded Already!")

button = Button(window,text="Click here to download",fg="white",bg="black",command=buttonFunc)
button.pack()
# button.place(300,300)

window.mainloop()
