class Player:
    def __init__(self, name, cards, controlled= False):
        self.controlled = controlled
        self.hand = cards
        self.name = name
    
    def play(self):
        if self.controlled:
            #human playing
            print(self.name, "turn")
            print("your cards are: ")
            print(self.hand)
            to_play = input("Chose the card or cards split by commas")
            if len(to_play) == 0:
                return False
            to_play = to_play.split(",")
            to_play = [int(x) for x in to_play]
            to_play.sort(reverse= True)
            return [self.hand.pop(x) for x in to_play]
        else:
            print("not done")
            exit()