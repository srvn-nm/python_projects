from tkinter import *
import instaloader
import urllib
from urllib import urlopen
import Pillow

# instagram
insta = instaloader.Instaloader()

# window
window = Tk()
window.geometry("600x600")
window.maxsize(800,800)
window.minsize(400,400)
window.title("Instagram Profile Downloader")

label = Label(window,text="Type the username here: ")
label.pack()

label_pic = Label(window)

def buttonFunc():
    # print("You pressed the button! >-<")
    # button.config(text="Downloaded Already!")
    profile = instaloader.Profile.from_username(insta.context,input.get())
    # print(profile.followers)
    # label.config(text=input.get())
    username = profile.get_profile_pic_url()
    # print(username)

button = Button(window,text="Click here to download",fg="white",bg="black",command=buttonFunc)
button.pack()
# button.place(300,300)

input = Entry(window)
input.pack()


window.mainloop()