SUITS = ["hearts", "spades", "diamonds", "clubs"]
VALUES = list(range(1,10))

class Card:
    def __init__(self, suit, number):
        self.value = number
        self.suit = suit
    def __str__(self):
        return str(self.value) + " of " +  self.suit
    def __repr__(self):
        return str(self)

class Deck:
    """
    the deck class which can be inited
    """
    def __init__(self):
        from itertools import product
        card_set = list(product(SUITS, VALUES))
        from random import shuffle, choice 
        shuffle(card_set)
        self.cards = [Card(*val_pair) for val_pair in card_set]
        self.strong = choice(SUITS)
        self.cards_left = len(self.cards)
    
    def get_card(self):
        if self.cards_left > 0:
            self.cards_left -= 1
            return self.cards.pop(-1)
        else:
            return False

    def get_cards(self, n):
        return [self.get_card() for _ in range(n)]

    def compare_cards(self, A, B):
        #equiv to check A>B?
        if A.suit == B.suit:
            return A.value>B.value
        elif A.suit == self.strong:
            return True
        else:
            return False

    def check_defense(self, attack_cards, deffend_cards):
        from itertools import permutations
        for order in permutations(attack_cards):
            if all([self.compare_cards(deffend_cards[i], order[i]) for i in range(len(deffend_cards))]):
                return True
        return False
        
    def check_legal(self, cards, played_cards = None):
        if played_cards is None:
            played_cards = set([cards[0].value])
        legality = [card.value in played_cards for card in cards]
        return all(legality)