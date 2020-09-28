from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

from my_types import *
from choose_card import *


root = Tk()


####### Choosing cards frame #######

def _destroy_pick_card_win(event):
    if(str(event.widget) == ".card_picked1"):
        card_img_name = hand.card1.number_str + "_" + hand.card1.sign_str
        image = Image.open("" + images_path + card_img_name + ".png")
        image = image.resize((150, 220), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        photo1.clear()
        photo1.append(photo)
        card_one_l.configure(image = photo1[0])
        card_one_l.grid(row=0, column=0)
    elif(str(event.widget) == ".card_picked2"):
        card_img_name = hand.card2.number_str + "_" + hand.card2.sign_str
        image = Image.open("" + images_path + card_img_name + ".png")
        image = image.resize((150, 220), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        photo2.clear()
        photo2.append(photo)
        card_two_l.configure(image = photo2[0])
        card_two_l.grid(row=0, column=1)
        
    
def pick_card1():
    pick_card_win = Toplevel(root, name = "card_picked1")
    pick_card_win.bind("<Destroy>", _destroy_pick_card_win)
    place_card_images(pick_card_win, 1)

def pick_card2():
    pick_card_win = Toplevel(root, name = "card_picked2")
    pick_card_win.bind("<Destroy>", _destroy_pick_card_win)
    place_card_images(pick_card_win, 2)

def restart_card_pick():
    global card_one_l, card_two_l
    card_one_l.destroy()
    card_two_l.destroy()
    hand.restart_hand()
    photo1.clear()
    photo2.clear()
    card_one_l = ttk.Label(pick_cards_labels_f)
    card_two_l = ttk.Label(pick_cards_labels_f)

frame_cards_f = ttk.Frame(root, name="my_cards_frame")
frame_cards_f.grid(row = 0, column = 1)

pick_cards_labels_f = ttk.Frame(frame_cards_f, width=320, height=230)
pick_cards_labels_f.grid_propagate(0)
pick_cards_labels_f.grid(row = 1, column = 0, columnspan = 2)

card_one_l = ttk.Label(pick_cards_labels_f)
card_two_l = ttk.Label(pick_cards_labels_f)

photo1 = []
photo2 = []

pick_card1_b = ttk.Button(frame_cards_f, text="Pick card", command=pick_card1)
pick_card1_b.grid(row = 0, column = 0, padx=(10, 10), pady=(5, 5))
pick_card2_b = ttk.Button(frame_cards_f, text="Pick card", command=pick_card2)
pick_card2_b.grid(row = 0, column = 1, padx=(10, 10), pady=(5, 5))


########################################

#### Initial frame ####

def restart_game():
    restart_card_pick()
    num_of_players_e.configure(state=ACTIVE)
    remove_player_b.configure(state=ACTIVE)
    pick_card1_b.configure(state=ACTIVE)
    pick_card2_b.configure(state=ACTIVE)
    remove_player_b.grid_forget()
    restart_game_b.grid_forget()
    next_phase_b.grid_forget()
    prev_phase_b.grid_forget()
    for pl_l in other_players_l:
        pl_l.destroy()

    other_players_l.clear()
    start_game_b.grid(row = 1, column = 0, columnspan=2, pady=(10, 0))

def start_game():
    try:
        num_of_players = int(num_of_players_e.get())
        if num_of_players not in range(1,9):
            raise ValueError

        hand.set_num_of_players(num_of_players)
        if not hand.cards_chosen:
            raise Exception("Please chose cards before starting game.")
        
        num_of_players_e.configure(state=DISABLED)
        pick_card1_b.configure(state=DISABLED)
        pick_card2_b.configure(state=DISABLED)
        start_game_b.grid_forget()
        restart_game_b.grid(row = 1, column = 0, columnspan=2, pady=(10, 0))
        set_flop_frames()
        add_players()
            
    except ValueError:
        messagebox.showerror("Setup error", "Please insert number between 1 and 8 in 'Number of players' box.")
    except Exception as ex:
        messagebox.showerror("Setup error", str(ex))
    

start_game_f = ttk.Frame(root, name="setup_frame")

ttk.Label(start_game_f, text="Number of other players").grid(row = 0, column = 0)
num_of_players_e = ttk.Entry(start_game_f, width=5)
num_of_players_e.grid(row = 0, column = 1, padx=(10, 0))
start_game_b = ttk.Button(start_game_f, name="start_btn", text="Start", command=start_game)
start_game_b.grid(row = 1, column = 0, columnspan=2, pady=(10, 0))
restart_game_b = ttk.Button(start_game_f, name="restart_btn", text="Restart", command=restart_game)

start_game_f.grid(row = 0, column = 0, padx=(50, 50), pady=(25, 25))

#######################

###### Flop frame ######

def set_flop_frames():
    next_phase_b.grid(row = 0, column = 0, pady=(10, 10))
    prev_phase_b.grid(row = 1, column = 0, pady=(10, 10))

flop_f = ttk.Frame(root, name="flop_frame")
flop_f.grid(row = 1, column = 0, columnspan = 5, sticky = 'w')

flop_s = ttk.Style()
flop_s.configure('flop.TFrame', background='white')
flop_cards_f = ttk.Frame(flop_f, width = 500, height = 230, style = 'flop.TFrame')
flop_cards_f.grid_propagate(0)
flop_cards_f.grid(row = 0, column = 0, padx=(10, 10))

flop_btn_f = ttk.Frame(flop_f)
flop_btn_f.grid(row = 0, column = 1, padx=(0, 10))

next_phase_b = ttk.Button(flop_btn_f, text = "Next phase")

prev_phase_b = ttk.Button(flop_btn_f, text = "Previous phase")


########################

#### Other players frame #####

def remove_palyer():
    pl_num = hand.get_num_of_players()
    if(pl_num == 2):
        remove_player_b.configure(state=DISABLED)

    for i in range(0,2):
        other_players_l[-1].grid_forget()
        del other_players_l[-1]

    hand.set_num_of_players(pl_num - 1)
    
    
def add_players():
    pl_num = hand.get_num_of_players()
    for i in range(0, pl_num):
        for j in range(0,2):
            image = Image.open("" + images_path + "card_back.jpg")
            image = image.resize((90, 140), Image.ANTIALIAS)
            card_back_photos.append(ImageTk.PhotoImage(image))
            other_players_l.append(ttk.Label(card_back_f, image = card_back_photos[-1]))
            last_card_in_row = int((i+1)%4 == 0)*j
            other_players_l[-1].grid(row = int(i/4), column = (2*i+j)%8, padx=(15*((j+1)%2), 15*last_card_in_row), pady=(5,5))

    if(hand.get_num_of_players() == 1):
        remove_player_b.configure(state=DISABLED)
        
    remove_player_b.grid(row = 0, column = 0, pady=(10, 10))

other_players_f = ttk.Frame(root, name="other_players_frame")
other_players_f.grid(row = 2, column = 0, columnspan = 9)

card_back_s = ttk.Style()
card_back_s.configure('other_players.TFrame', background='white')
card_back_f = ttk.Frame(other_players_f, name="card_back_frame", width = 830, height = 310, style='other_players.TFrame')
card_back_f.grid_propagate(0)
card_back_f.grid(row = 0, column = 0, padx=(10, 10), pady=(10, 10))

fold_btn_f = ttk.Frame(other_players_f, width = 50)
fold_btn_f.grid(row = 0, column = 1, padx=(10, 20), sticky = "n")

card_back_photos = []

remove_player_b = ttk.Button(fold_btn_f, name="remove_player_btn", text="Fold", command=remove_palyer)

other_players_l = []

##############################

root.mainloop()

