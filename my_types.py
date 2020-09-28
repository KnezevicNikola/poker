phases = ["SETUP", "PRE_FLOP", "FLOP", "TURN", "RIVER"]

card_numbers = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "none"]
card_signs = ["spades", "hearts", "diamonds", "clubs", "none"]


class Card:
    def __init__(self, sgn = -1, num = -1):
        self.set_fields(num, sgn)

    def __repr__(self):
        if(self.number == -1):
            return "not picked"
        elif((self.number > -1) and (self.sign > -1)):
            return "<%s of %s>" % (self.number_str, self.sign_str)

    def __str__(self):
        if(self.number == -1):
            return "not picked"
        elif((self.number > -1) and (self.sign > -1)):
            return "%s of %s" % (self.number_str, self.sign_str)

    def set_fields(self, num, sgn):
        self.number_str = card_numbers[num]
        self.sign_str = card_signs[sgn]
        self.number = num
        self.sign = sgn

    def is_chosen(self):
        return (self.number > -1) and (self.sign > -1)


class Hand:
    __phase = 0
    __num_of_players = 0

    def __init__(self, card1, card2):
        self.set_cards(card1, card2)
        self.__phase = 0

    def __repr__(self):
        return "<Card 1 is %s \nCard 2 is %s>" % (self.card1, self.card2)

    def __str__(self):
        return "Card 1 is %s \nCard 2 is %s" % (self.card1, self.card2)

    def set_cards(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.cards_chosen = False

    def change_card(self, card_idx, num, sgn):
        if(card_idx == 1):
            self.card1.set_fields(num, sgn)
        elif(card_idx == 2):
            self.card2.set_fields(num, sgn)

        self.cards_chosen = self.card1.is_chosen() and self.card2.is_chosen()

    def get_current_hase(self):
        return phases[__phase]
            
    def advance_phase(self):
        if(self.__phase < 4):
            self.__phase += 1

    def restart_hand(self):
        self.set_cards(Card(), Card())
        self.__phase = 0
        self.__num_of_players = 0

    def set_num_of_players(self, num):
        assert(num in range(1,9))
        self.__num_of_players = num

    def get_num_of_players(self):
        return self.__num_of_players
            
        
hand = Hand(Card(), Card())
