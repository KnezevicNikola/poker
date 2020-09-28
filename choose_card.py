from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

from my_types import *

images_path = "C:\\Users\\User\\Documents\\python\\all_cards\\"

def chosen_card_action(sign, num, frame, card_idx):
    hand.change_card(card_idx, num, sign)
    frame.destroy()

photos = []
def place_card_images(frame, card_num):
    for sign in range(0, 4):
        for num in range(0, 13):
            image = Image.open("" + images_path + card_numbers[num] + "_" + card_signs[sign] + ".png")
            image = image.resize((80, 120), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            photos.append(photo)
            pick_card_btn = ttk.Button(frame, image=photos[-1] )
            pick_card_btn.configure(command = lambda i=sign, j=num : chosen_card_action(i, j, frame, card_num))
            pick_card_btn.grid(row = sign, column = num, padx=(10, 10), pady=(10, 10))
    
