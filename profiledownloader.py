import instaloader
from PIL import Image, ImageTk
import os
# Create instance
loader = instaloader.Instaloader()
# get username 
user = input("Enter Username: ")
# download profie
loader.download_profile(user, profile_pic_only = True)
# get list of image from folder
img = [x for x in os.listdir(f'{os.getcwd()}/{user}') if x.endswith('jpg')]
# read image from list
img = Image.open(f'{os.getcwd()}/{user}/{img[0]}')
# Display image
img.show()