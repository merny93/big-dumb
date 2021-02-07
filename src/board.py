from src.player import Player
from src.deck import Deck
class Board:
    def __init__(self, players):
        #players is a list with names and if they are controlled or not 
        self.deck = Deck()
        print("the strong suit", self.deck.strong)
        self.players = [Player(pl[0], self.deck.get_cards(6),controlled = pl[1]) for pl in players]
        self.turn = 0

    def play_turn(self):
        attack = self.turn
        deffend = (self.turn +1)%len(self.players)
        bystanders = list(range(len(self.players)))
        bystanders.remove(attack)
        bystanders.remove(deffend)
        #start with the 1 on 1

        ##attack
        attack_cards = self.players[attack].play()
        if not self.deck.check_legal(attack_cards):
            print("whell fulk")
        if len(attack_cards) == 0:
            print("certified bruh moment play a card")
        print("cards played against u")
        print(attack_cards)
        deffend_cards = self.players[deffend].play()
        ##check if win
        if not self.deck.check_defense(attack_cards, deffend_cards):
            self.players[deffend] += attack_cards + deffend_cards
            self.turn = (self.turn +2)%len(self.players)
            return
        
        ##ok so keep going
        total_cards = attack_cards + deffend_cards
        played_numbers = set([x.value for x in attack_cards + deffend_cards])
        while True:
            attack_cards = self.players[attack].play()
            if len(attack_cards) == 0:
                break
            
            if not self.deck.check_legal(attack_cards, played_cards=played_numbers):
                print("not legal")
            
            print("cards played against u")
            print(attack_cards)
            deffend_cards = self.players[deffend].play()
            if not self.deck.check_defense(attack_cards, deffend_cards):
                self.players[deffend] += total_cards +  attack_cards + deffend_cards
                self.turn = (self.turn +2)%len(self.players)
                return
            total_cards += attack_cards + deffend_cards
            played_numbers.update(set([x.value for x in attack_cards + deffend_cards]))
        #now bistanders turn
        while True:
            attack_cards = []
            for pl in bystanders:
                added = self.players[pl].play()
                if len(added) == 0:
                    pass
                elif not self.deck.check_legal(added, played_cards=played_numbers):
                    print("reee")
                attack_cards += added        
            if len(attack_cards) == 0:
                break
            print("cards played against u")
            print(attack_cards)
            deffend_cards = self.players[deffend].play()
            if not self.deck.check_defense(attack_cards, deffend_cards):
                self.players[deffend] += total_cards +  attack_cards + deffend_cards
                self.turn = (self.turn +2)%len(self.players)
                return
            total_cards += attack_cards + deffend_cards
            played_numbers.update(set([x.value for x in attack_cards + deffend_cards]))