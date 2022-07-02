from tkinter import *

window = Tk()
window.geometry("600x600")
window.maxsize(800,800)
window.minsize(400,400)
window.title("Instagram Profile Downloader")

label = Label(window,text="Hello Instagram!")
label.pack()

button = Button(window,text="Click here to download",fg="white",bg="black")
button.pack()

window.mainloop()
