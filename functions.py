import random

def hand_evaluation(hand):
    card_copy = hand.copy()

    # Replace J, Q, K with value of 10
    for i in range(0, len(card_copy)):
        if card_copy[i] == 'J':
            card_copy[i] = '10'
        elif card_copy[i] == 'Q':
            card_copy[i] = '10'
        elif card_copy[i] == 'K':
            card_copy[i] = '10'

    # Check occurence of A
    if 'A' in card_copy:
        aces_count = card_copy.count('A')

        for i in range(0, aces_count):
            card_copy.remove('A')

        card_copy = [int(i) for i in card_copy]
        total_value = sum(card_copy)

        for i in range(0, aces_count):
            if total_value < 11:
                total_value += 11
            else:
                total_value += 1

    else:
        card_copy = [int(i) for i in card_copy]
        total_value = sum(card_copy)
        
    return total_value

def double_down():
    players_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    if hand_evaluation(players_card) > 21:
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}")
        print("")
        print("Busted ! You have lost this round.")

    elif hand_evaluation(players_card) <= 21:
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        if hand_evaluation(dealers_card) > 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}")
            print("")
            print("Dealer busted ! You have won this round.")
        elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}")
            print("")
            print("Push ! You have not won or lost this round.")
        elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}")
            print("")
            print("Nice ! You have won this round.")
        elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}")
            print("")
            print("Too low ! You have lost this round.")

def stand():
    while hand_evaluation(dealers_card) < 17:
        dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    if hand_evaluation(dealers_card) > 21:
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Dealer busted ! You have won this round.")    
    elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Push ! You have not won or lost this round.")
    elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Nice ! You have won this round.")
    elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Too low ! You have lost this round.")

def fold():
    print("You folded ! You have lost this round.")
    
def hit():
    decision_2 = '1'
    while decision_2 == '1':
        players_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))

        if hand_evaluation(players_card) > 21:
            decision_2 = '0'
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Busted ! You have lost this round.")
        
        elif hand_evaluation(players_card) == 21:
            decision_2 = '0'
            while hand_evaluation(dealers_card) < 17:
                dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
                
            if hand_evaluation(dealers_card) > 21:
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Dealer busted ! You have won this round.") 
                
            elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Push ! You have not won or lost this round.")
            
            elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Nice ! You have won this round.")
            
            elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Too low ! You have lost this round.")

        elif hand_evaluation(players_card) < 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")

            print("Choice of Action:")
            print("1. Hit")
            print("2. Stand")
            print("3. Fold")

            decision_2 = input("Please input action: ")

    if decision_2 == '2':
        stand()
    elif decision_2 == '3':
        fold()
        
one_suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
one_deck = 4 * one_suit
one_deck_shuffled = random.sample(one_deck, len(one_deck))
no_deck = int(input('How many decks do you want to play ? '))
all_cards = no_deck * one_deck_shuffled

to_continue = True
while to_continue == True:
    cards_for_play = random.sample(all_cards, len(all_cards))

    players_card = []
    dealers_card = []

    players_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    players_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))

    print("")
    print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
    print("")

    if hand_evaluation(players_card) == 21 and hand_evaluation(dealers_card) != 11:
        print("BLACKJACK ! You have won this round.")

    elif hand_evaluation(players_card) == 21 and hand_evaluation(dealers_card) == 11:
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        if hand_evaluation(dealers_card) == 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Push ! You have not won or lost this round.")
        elif hand_evaluation(dealers_card) < 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Nice ! You have won this round.")
        elif hand_evaluation(dealers_card) > 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Dealer busted ! You have won this round.")

    elif hand_evaluation(players_card) < 21:

        print("Choice of Action:")
        print("1. Hit")
        print("2. Double Down")
        print("3. Stand")
        print("4. Fold")

        decision_1 = input("Please input action: ")

        if decision_1 == '2':
            double_down()

        elif decision_1 == '3':
            stand()

        elif decision_1 == '4':
            fold()

        elif decision_1 == '1':
            hit()

    to_continue_decision = input("Do you want to continue? (y/n)")
    if to_continue_decision == 'y':
        to_continue = True
    else:
        to_continue = False
print("")
print("Thank You for Playing This Blackjack Simulator !")