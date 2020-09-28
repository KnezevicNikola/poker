import random

cards_l = [ "ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
signs_l = [ "hearts", "clubs", "diamonds", "spades" ]

def two_cards_same_num(sample_size):
    N = sample_size
    valid_randomizations = 0
    hits = 0
    for i in range(0, N):
        first_c = random.randrange(1,14)
        first_s = random.randrange(1,5)
        second_c = random.randrange(1,14)
        second_s = random.randrange(1,5)
        if not ((first_c == second_c) and (first_s == second_s)):
            valid_randomizations += 1
            if(first_c == second_c):
                hits += 1

    return hits/valid_randomizations

def card_is_num(sample_size, card_num):
    N = sample_size
    valid_randomizations = 0
    hits = 0
    for i in range(0, N):
        first_c = random.randrange(1,14)
        first_s = random.randrange(1,5)
        second_c = random.randrange(1,14)
        second_s = random.randrange(1,5)
        if not ((first_c == second_c) and (first_s == second_s)):
            valid_randomizations += 1
            if((first_c == card_num) or (second_c == card_num)):
                hits += 1

    return hits/valid_randomizations
    
    


phases = ["PRE_FLOP", "FLOP", "TURN", "RIVER"]

class Card:
    number
    sign

    

class Hand:

    first_card
    second_card

    win_probability_current
    win_probability_end
    
    no_of_players

    __phase

    __init__(self, first_card, second_card, no_of_players):
        self.first_card = first_card
        self.second_card = second_card
        self.no_of_players = no_of_players
        self.__phase = "PRE_FLOP"

    
