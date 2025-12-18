

valid_rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
valid_suit = ["S","C","D","H"]
rank_value = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
cards = []
for i in range(1, 6):
    while True:
        card = input(f"Card {i}: ").strip()
        rank = card[:-1]
        suit = card[-1]

        error = False
        if rank not in valid_rank:
            print(f"Invalid rank {rank}. Must be 2-10, J, Q, K, or A.")
            error = True
        if suit not in valid_suit:
            print(f"Invalid suit {suit}. Must be H, D, C, or S.")
            error = True
        if not error:
            if card in cards:
                print(f"There can't be two {card} in the same hand. You're playing with a fake deck!")
                exit()
            cards.append(card)
            break

#display the best poker hand
# @param cards
# 1st function is flush - 5 same card, each card has unique value, so i will use set as well
def is_same_suit(cards):
    suits = [card[-1] for card in cards]
    return len(set(suits))==1
#make a decision:


#2nd function is straight - in order rank in differ suits:
# @param cards
def is_straight(cards):
    ranks = [card[:-1] for card in cards]
    values = sorted([rank_value[r] for r in ranks])
    for i in range(4):
        if values[i + 1] - values[i] != 1:
            return False
    return True





#3rd function is straight flush! we already wrote the function for each part :
# @param cards
def is_straight_flush(cards):
    return is_straight(cards) and is_same_suit(cards)

#4 @param cards
def is_royal_flush(cards):
    ranks = [card[:-1] for card in cards]
    return is_same_suit(cards) and set(ranks) == {"10","J","Q","K","A"}




#5th is about full house ! Which is 3 same ranks and 2 other same ranks at the same time!
# @param cards
def is_full_house(cards):
    ranks = [card[:-1] for card in cards]
    has_three = False
    has_two = False
    for r in ranks:
        if ranks.count(r) == 3:
            has_three = True
        elif ranks.count(r) == 2:
            has_two = True
    if has_three and has_two:
        return True
    return False

#6th and 6th I am going to write a function for four of a kind and three of a kind
# @param cards
def is_four_of_kind(cards):
    ranks = [card[:-1] for card in cards]
    for r in ranks:
        if ranks.count(r) == 4:
            return True
    return False



def is_three_of_kind(cards):
    ranks = [card[:-1] for card in cards]
    for r in ranks:
        if ranks.count(r)==3:
            return True
    return False

#7th and 8TH will be function for the two pair and one pair
def is_one_pair(cards):
    ranks = [card[:-1] for card in cards]
    for r in ranks:
        if ranks.count(r)==2:
            return True
    return False

def is_two_pair(cards):
    ranks = [card[:-1] for card in cards]
    has_2_similar_rank = False
    pair_of_rank = False
    hand = []
    for r in ranks:
        if r in hand:
            continue
        if ranks.count(r) == 2 and has_2_similar_rank == False:
            has_2_similar_rank = True
        elif ranks.count(r) == 2 and has_2_similar_rank == True:
            pair_of_rank = True
        hand.append(r)
    if has_2_similar_rank == True and pair_of_rank == True:
        return True
    else:
        return False




def is_high_card(cards):
    ranks = [card[:-1] for card in cards]
    suits = [card[-1] for card in cards]
    if len(set(ranks)) == 5 and not is_straight(cards) and not is_same_suit(cards):
        return True
    return False

def main():
    # @param cards
    if is_royal_flush(cards):
        print("Royal Flush")
    elif is_straight_flush(cards):
        print("Straight Flush")
    elif is_four_of_kind(cards):
        print("Four of a Kind")
    elif is_full_house(cards):
        print("Full House")
    elif is_same_suit(cards):
        print("Flush")
    elif is_straight(cards):
        print("Straight")
    elif is_three_of_kind(cards):
        print("Three of a Kind")
    elif is_two_pair(cards):
        print("Two Pair")
    elif is_one_pair(cards):
        print("One Pair")
    else:
        print("High Card")
main()
