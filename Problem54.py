with open("Problem54_hands.txt") as file:
    lines = [line.rstrip() for line in file]

class pokerHand():
    def __init__(self, cards : list) -> None:
    #Store as an ordered list of tuples of int, char. Order by int. (char doesn't matter)
        pass

    def beats(self, hand) -> bool:
        pass

hand1Wins = 0
for line in lines:
    cards = line.split()
    hand1 = cards[0:5]
    hand2 = cards[5:10]
    if pokerHand(hand1).beats(pokerHand(hand2)):
        hand1Wins

#Now we need to define handValues and an ordering on them (beats). 
#Method: look for hand type stating from the highest scoring one. This finds the hand -> remove it from leftover cards. Then if they both have the same hand, take highest leftover card. Repeat.


#Define bestHand and leftovers during init. 

#Again how do we define binary operations on classes?
