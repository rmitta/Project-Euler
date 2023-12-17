#Poker Hands
#How many of the following poker hands does player 1 win?

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
        self.cards = sorted([pokerCard(card) for card in cards])

    def bestHand(self) -> (str,list,list):
        """Calculate the best poker hand and store the result"""
        #Check for flush (have to repeat later)
        if all((self.cards[0].suit == self.cards[i].suit for i in range(1,5))):
            #Check for straight flush
            if all((self.cards[0].num + i == self.cards[i].num for i in range(1,5))):
                #Check for royal flush
                if self.cards[4].num == 14:
                    return ("Royal Flush", self.cards, [])
            return ("Straight Flush", self.cards, [])
        #Check for 4 of a kind
        for i in range(2): #Only need to check twice because only 1 can be outside the 4kind
            sameCards = [self.cards[j] for j in range(5) if self.cards[j].num == self.cards[i].num]
            if len(sameCards) == 4:
                return ("Four of a Kind", sameCards, [self.cards[i] for i in range(5) if self.cards[i].num != sameCards[0].num])
        #Check for 3 of a kind
        for i in range(3): #Only need to check thrice because only 2 can be outside the 3kind
            sameCards = [self.cards[j] for j in range(5) if self.cards[j].num == self.cards[i].num]
            if len(sameCards) == 3:
                #Check for full house
                otherCards = list(set(self.cards) - set(sameCards))
                if otherCards[0].num == otherCards[1].num:
                    return ("Full House", sameCards, otherCards)
        #Check for flush
        if all((self.cards[0].suit == self.cards[i].suit for i in range(1,5))):
            return ("Flush", self.cards, [])
        #Check for straight
        if all((self.cards[0].num + i == self.cards[i].num for i in range(1,5))):
            return("Straight", self.cards, [])
        #Check for 3 of a kind
        for i in range(3): #Only need to check thrice because only 2 can be outside the 3kind
            sameCards = [self.cards[j] for j in range(5) if self.cards[j].num == self.cards[i].num]
            if len(sameCards) == 3:
                return ("Three of a Kind",sameCards,list(set(self.cards) - set(sameCards)))
        #Check for two pair
        for i in range(2): #Only need to check twice because only 1 can be outside the two pair
            sameCards = [self.cards[j] for j in range(5) if self.cards[j].num == self.cards[i].num]
            if len(sameCards) == 2:
                otherCards = list(set(self.cards) - set(sameCards))
                for k in range(2): #Only need to check twice because only 1 can be outside the pair
                    secondPair = [otherCards[j] for j in range(3) if otherCards[j].num == otherCards[k].num]
                    if len(secondPair) == 2:
                        return ("Two Pairs", cardsInHand := sameCards + secondPair, list(set(self.cards) - set(cardsInHand)))
        #Check for one pair
        for i in range(4):
            sameCards = [self.cards[j] for j in range(5) if self.cards[j].num == self.cards[i].num]
            if len(sameCards) == 2:
                return("One Pair", sameCards, list(set(self.cards) - set(sameCards)))
        #Else return high cards
        return("High Card", self.cards,[])

    def __lt__(self, other) -> bool:
        """Compare two hands. Note that this changes the cards stored in handCards and otherCards"""
        h1name, cards1, ocards1 = self.bestHand()
        h2name, cards2, ocards2 = other.bestHand()
        if (h1 := handOrder[h1name]) < (h2 := handOrder[h2name]):
            return True
        if h1 > h2:
            return False
        while cards1:
            if (c1 := cards1.pop()) < (c2 := cards2.pop()):
                return True
            if c1 > c2:
                return False
        while ocards1:
            if (c1 := ocards1.pop()) < (c2 := ocards2.pop()):
                return True
            if c1 > c2:
                return False
        return False
        
hand1Wins = 0
for line in lines:
    cards = line.split()
    hand1 = cards[0:5]
    hand2 = cards[5:10]
    if pokerHand(hand2) < (pokerHand(hand1)):
        hand1Wins += 1
print(hand1Wins)
