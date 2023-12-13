with open("Problem54_hands.txt") as file:
    lines = [line.rstrip() for line in file]

cardOrder = {'1' : 1,
             '2' : 2,
             '3' : 3,
             '4' : 4,
             '5' : 5,
             '6' : 6,
             '7' : 7,
             '8' : 8,
             '9' : 9,
             'T' : 10,
             'J' : 11,
             'Q' : 12,
             'K' : 13,
             'A' : 14,
             }

handOrder = {"High Card" : 1,
             "One Pair" : 2,
             "Two Pairs" : 3,
             "Three of a Kind" : 4,
             "Straight" : 5,
             "Flush" : 6,
             "Full House" : 7,
             "Four of a Kind" : 8,
             "Straight Flush": 9,
             "Royal Flush" : 10
            }

class pokerCard():
    def __init__(self, card : str) -> None:
        self.num = cardOrder[card[0]]
        self.suit = card[1]

    def __lt__(self, other):
        return self.num < other.num

class pokerHand():
    def __init__(self, cards : list) -> None:
        """Store as an ordered list of pokerCards, ordered by number."""
        self.cards = [pokerCard(card) for card in cards].sort()

    def bestHand(self) -> None:
        """Calculate the best poker hand and store the result"""
        if all((self.cards[0].suit == self.cards[i].suit for i in range(1,5))):
            if 
        self.hand = ""
        self.handCards = [].sort()
        self.otherCards = [].sort()


    def __lt__(self, other) -> bool:
        """Compare two hands. Note that this changes the cards stored in handCards and otherCards"""
        if (h1 := handOrder[self.hand]) < (h2 := handOrder[other.hand]):
            return True
        if h1 > h2:
            return False
        if self.hand == "Full House":
            if (c1 := self.triple[0]) < (c2 := other.triple[0]):
                return True
            if c1 > c2:
                return False
            if (c1 := self.double[0]) < (c2 := other.double[0]):
                return True
            if c1 > c2:
                return False
        while self.handCards:
            if c1 := self.handCards.pop() < (c2 := other.handCards.pop()):
                return True
            if c1 > c2:
                return False
        while self.otherCards:
            if c1 := self.otherCards.pop() < (c2 := other.otherCards.pop()):
                return True
            if c1 > c2:
                return False
        return False
        

#Logic: sequentially check for each poker hand type to get self.hand
#For <, when two hands have the same type, we have to check the highest card in each rank (and for full house the 3), then each hand 


hand1Wins = 0
for line in lines:
    cards = line.split()
    hand1 = cards[0:5]
    hand2 = cards[5:10]
    if pokerHand(hand2) < (pokerHand(hand1)):
        hand1Wins += 1
print(hand1Wins)

