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

def local_evaluation(hand_1):
    global players_win, dealers_win, draws, wallet, local_win, local_loss, local_push
    if hand_evaluation(hand_1) > 21:
        local_loss += 1
    elif hand_evaluation(hand_1) <= 21 and hand_evaluation(dealers_card) > 21:
        local_win += 1
    elif hand_evaluation(hand_1) <= 21 and hand_evaluation(dealers_card) <= 21:
        if hand_evaluation(hand_1) > hand_evaluation(dealers_card):
            local_win += 1
        elif hand_evaluation(hand_1) == hand_evaluation(dealers_card):
            local_push += 1
        elif hand_evaluation(hand_1) < hand_evaluation(dealers_card):
            local_loss += 1

def double_down(players_card):
    global players_win, dealers_win, draws, wallet
    players_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    if hand_evaluation(players_card) > 21:
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}")
        print("")
        print("Busted ! You have lost this round.")
        dealers_win += 1
        wallet -= 2 * wage

    elif hand_evaluation(players_card) <= 21:
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        if hand_evaluation(dealers_card) > 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}")
            print("")
            print("Dealer busted ! You have won this round.")
            players_win += 1
            wallet += 2 * wage
        elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Push ! You have not won or lost this round.")
            draws += 1
        elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Nice ! You have won this round.")
            players_win += 1
            wallet += 2 * wage
        elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Too low ! You have lost this round.")
            dealers_win += 1
            wallet -= 2 * wage

def stand(players_card):
    global players_win, dealers_win, draws, wallet
    while hand_evaluation(dealers_card) < 17:
        dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
    if hand_evaluation(dealers_card) > 21:
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Dealer busted ! You have won this round.") 
        players_win += 1
        wallet += wage
    elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Push ! You have not won or lost this round.")
        draws += 1
    elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Nice ! You have won this round.")
        players_win += 1
        wallet += wage
    elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
        print("")
        print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        print("Too low ! You have lost this round.")
        dealers_win += 1
        wallet -= wage
    
def hit(players_card):
    global players_win, dealers_win, draws, wallet
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
            dealers_win += 1
            wallet -= wage
        
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
                players_win += 1
                wallet += wage
                
            elif hand_evaluation(players_card) == hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Push ! You have not won or lost this round.")
                draws += 1
            
            elif hand_evaluation(players_card) > hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Nice ! You have won this round.")
                players_win += 1
                wallet += wage
            
            elif hand_evaluation(players_card) < hand_evaluation(dealers_card):
                print("")
                print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Too low ! You have lost this round.")
                dealers_win += 1
                wallet -= wage

        elif hand_evaluation(players_card) < 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")

            print("Choice of Action:")
            print("1. Hit")
            print("2. Stand")

            decision_2 = input("Please input action: ")

    if decision_2 == '2':
        stand(players_card)
        
def split():
    global players_win, dealers_win, draws, wallet
    hand_1 = [players_card[0]]
    hand_2 = [players_card[1]]
    
    # For splitting A's, no further split and only addition of one card
    if hand_1[0] == 'A':
        hand_1.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        hand_2.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        
        # Blackjack Scenarios
        if hand_evaluation(hand_1) == 21 or hand_evaluation(hand_2) == 21 and hand_evaluation(dealers_card) != 21:
            if hand_evaluation(hand_1) == 21 and hand_evaluation(hand_2) == 21:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Congratulations ! You got 2 blackjacks !") 
                players_win += 2
                wallet += 3 * wage
                
            elif hand_evaluation(hand_1) == 21 and hand_evaluation(hand_2) != 21:
                if hand_evaluation(dealers_card) > hand_evaluation(hand_2):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack but you lost the other hand to dealer.") 
                    players_win += 1
                    dealers_win += 1
                    wallet += 0.5 * wage
                    
                elif hand_evaluation(dealers_card) == hand_evaluation(hand_2):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack but you pushed the other hand.") 
                    players_win += 1
                    draws += 1
                    wallet += 1.5 * wage
                    
                elif hand_evaluation(dealers_card) < hand_evaluation(hand_2):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack and you won the other hand.") 
                    players_win += 2
                    wallet += 2.5 * wage
                    
            elif hand_evaluation(hand_2) == 21 and hand_evaluation(hand_1) != 21:
                if hand_evaluation(dealers_card) > hand_evaluation(hand_1):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack but you lost the other hand to dealer.") 
                    players_win += 1
                    dealers_win += 1
                    wallet += 0.5 * wage
                    
                elif hand_evaluation(dealers_card) == hand_evaluation(hand_1):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack but you pushed the other hand.") 
                    players_win += 1
                    draws += 1
                    wallet += 1.5 * wage
                    
                elif hand_evaluation(dealers_card) < hand_evaluation(hand_1):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You got a blackjack and you won the other hand.") 
                    players_win += 2
                    wallet += 2.5 * wage
        
        # Dealer Bust
        elif hand_evaluation(dealers_card) > 21:
            print("")
            print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
            print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Dealer busted ! You have won this round.") 
            players_win += 2
            wallet += 2 * wage
            
        
        elif hand_evaluation(dealers_card) <= 21:
            
            # Both hands wins 
            if hand_evaluation(dealers_card) < hand_evaluation(hand_1) and hand_evaluation(dealers_card) < hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Nice ! You have won both hands against the dealer") 
                players_win += 2
                wallet += 2 * wage
            
            # Both hands pushes
            elif hand_evaluation(dealers_card) == hand_evaluation(hand_1) and hand_evaluation(dealers_card) == hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Both hands pushed against the dealer. You have not won or lost this round.")
                draws += 2
        
            # Both hands loses
            elif hand_evaluation(dealers_card) > hand_evaluation(hand_1) and hand_evaluation(dealers_card) > hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("Both too low ! You have lost both hands against the dealer") 
                dealers_win += 2
                wallet -= 2 * wage
                
            # One win and one loss
            elif hand_evaluation(dealers_card) < hand_evaluation(hand_1) and hand_evaluation(dealers_card) > hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and lost one hand.") 
                players_win += 1
                dealers_win += 1
                
            elif hand_evaluation(dealers_card) > hand_evaluation(hand_1) and hand_evaluation(dealers_card) < hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and lost one hand.") 
                players_win += 1
                dealers_win += 1
        
            # One win and one push
            elif hand_evaluation(dealers_card) == hand_evaluation(hand_1) and hand_evaluation(dealers_card) < hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and pushed one hand.") 
                players_win += 1
                draws += 1
                wallet += wage
            
            elif hand_evaluation(dealers_card) < hand_evaluation(hand_1) and hand_evaluation(dealers_card) == hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and pushed one hand.") 
                players_win += 1
                draws += 1
                wallet += wage
                
            # One loss and one push
            elif hand_evaluation(dealers_card) == hand_evaluation(hand_1) and hand_evaluation(dealers_card) > hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You pushed one hand and lost one hand.") 
                dealers_win += 1
                draws += 1
                wallet -= wage
            
            elif hand_evaluation(dealers_card) > hand_evaluation(hand_1) and hand_evaluation(dealers_card) == hand_evaluation(hand_2):
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You pushed one hand and lost one hand.") 
                dealers_win += 1
                draws += 1
                wallet -= wage
                
    elif hand_1[0] != 'A':
        # Play Hand 1
        hand_1.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        blackjack_count = 0
        
        print("")
        print("You're playing your first split")
        print("")
        print(f"Your hand: {hand_1}  ({hand_evaluation(hand_1)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        
        if hand_evaluation(hand_1) == 21:
            blackjack_count +=1
        
        elif hand_evaluation(hand_1) != 21:
            print("Choice of Action:")
            print("1. Hit")
            print("2. Double Down")
            print("3. Stand")

            decision_1 = input("Please input action: ")

            if decision_1 == '2':
                double_down(hand_1)

            elif decision_1 == '3':
                stand(hand_1)

            elif decision_1 == '1':
                hit(hand_1)
        
        # Play Hand 2
        hand_2.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        
        print("")
        print("You're playing your second split")
        print("")
        print(f"Your hand: {hand_2}  ({hand_evaluation(hand_2)})")
        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
        print("")
        
        if hand_evaluation(hand_2) == 21:
            blackjack_count +=1
        
        elif hand_evaluation(hand_2) != 21:
            print("Choice of Action:")
            print("1. Hit")
            print("2. Double Down")
            print("3. Stand")

            decision_1 = input("Please input action: ")

            if decision_1 == '2':
                double_down(hand_2)

            elif decision_1 == '3':
                stand(hand_2)

            elif decision_1 == '1':
                hit(hand_2)
        
        # Evaluate results
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        
        # 2 blackjacks, dealer no 21
        if blackjack_count == 2 and hand_evaluation(dealers_card) != 21:
            print("")
            print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
            print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Congratulations ! You got 2 blackjacks !") 
            players_win += 2
            wallet += 3 * wage
        
        # 2 blackjacks, dealer 21
        elif blackjack_count == 2 and hand_evaluation(dealers_card) == 21:
            print("")
            print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
            print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("You got 2 blackjacks but dealer got it too ! :(")
            draws += 2
            
        # 1 blackjack
        elif blackjack_count == 1:
            
            # 1 blackjack, 1 bust
            if hand_evaluation(hand_1) > 21 or hand_evaluation(hand_2) > 21 and hand_evaluation(dealers_card) != 21:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You got a blackjack and a bust! ") 
                players_win += 1
                dealers_win += 1
                wallet += 0.5 * wage
                
            # 1 blackjack, 1 bust, dealer 21
            elif hand_evaluation(hand_1) > 21 or hand_evaluation(hand_2) > 21 and hand_evaluation(dealers_card) == 21:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You pushed your blackjack and bust one hand! ") 
                draws += 1
                dealers_win += 1
                wallet -= wage
                
            # 1 blackjack, no bust, dealer bust
            elif hand_evaluation(hand_1) <= 21 and hand_evaluation(hand_2) <= 21 and hand_evaluation(dealers_card) > 21:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You got a blackjack and won the other hand! ") 
                players_win += 2
                wallet += 2.5 * wage
                
            # 1 blackjack, no bust, dealer 21
            elif hand_evaluation(hand_1) <= 21 and hand_evaluation(hand_2) <= 21 and hand_evaluation(dealers_card) == 21:
                
                # 2 push (all 21)
                if hand_evaluation(hand_1) == hand_evaluation(hand_2):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("Both hands pushed.")
                    draws += 2
                
                # 1 push 1 loss             
                elif hand_evaluation(hand_1) != hand_evaluation(hand_2):
                    print("")
                    print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                    print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                    print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                    print("")
                    print("You have pushed one hand and lost one hand.")
                    draws += 1
                    dealers_win += 1

            # 1 blackjack, no bust, dealer no 21
            elif hand_evaluation(hand_1) <= 21 and hand_evaluation(hand_2) <= 21 and hand_evaluation(dealers_card) != 21:
                
                # Evaluate smaller hand against dealer
                if hand_evaluation(hand_1) > hand_evaluation(hand_2):
                    if hand_evaluation(hand_2) > hand_evaluation(dealers_card):
                        print("")
                        print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                        print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                        print("")
                        print("You got a blackjack and won the other hand! ") 
                        players_win += 2
                        wallet += 2.5 * wage
                        
                    elif hand_evaluation(hand_2) < hand_evaluation(dealers_card):
                        print("")
                        print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                        print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                        print("")
                        print("You got a blackjack and lost another hand! ") 
                        players_win += 1
                        dealers_win += 1
                        wallet += 0.5 * wage
                        
                    elif hand_evaluation(hand_2) == hand_evaluation(dealers_card):
                        print("")
                        print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                        print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                        print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                        print("")
                        print("You got a blackjack and pushed another hand! ") 
                        players_win += 1
                        draws += 1
                        wallet += 1.5 * wage
                        
        # 0 blackjacks
        elif blackjack_count == 0:
            local_win = 0
            local_loss = 0
            local_push = 0
            
            local_evaluation(hand_1)
            local_evaluation(hand_2)
            
            if local_win == 2:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won both hands!") 
                players_win += 2
                wallet += 2 * wage
                
            elif local_push == 2:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You pushed both hands!") 
                draws += 2
                
            elif local_loss == 2:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You lost both hands!") 
                dealers_win += 2
                wallet -= 2 * wage
                
            elif local_win == 1 and local_loss == 1:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and lost one hand!") 
                players_win += 1
                dealers_win += 1
                
            elif local_win == 1 and local_push == 1:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You won one hand and pushed one hand!") 
                players_win += 1
                draws += 1
                wallet += wage
                
            elif local_push == 1 and local_loss == 1:
                print("")
                print(f"Hand 1: {hand_1}  ({hand_evaluation(hand_1)})")
                print(f"Hand 2: {hand_2}  ({hand_evaluation(hand_2)})")
                print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
                print("")
                print("You lost one hand and pushed one hand!") 
                dealers_win += 1
                draws += 1
                wallet -= wage
        
one_suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
one_deck = 4 * one_suit
one_deck_shuffled = random.sample(one_deck, len(one_deck))
no_deck = int(input('How many decks do you want to play ? '))
all_cards = no_deck * one_deck_shuffled

players_win = 0
dealers_win = 0
draws       = 0
wallet      = 0

to_continue = True
while to_continue == True:
    wage = int(input("Please place your bet for this round. "))
    
    # Shuffling cards
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
        players_win += 1
        wallet += 1.5 * wage

    elif hand_evaluation(players_card) == 21 and hand_evaluation(dealers_card) == 11:
        while hand_evaluation(dealers_card) < 17:
            dealers_card.append(cards_for_play.pop(random.choice(list(range(0,len(cards_for_play))))))
        if hand_evaluation(dealers_card) == 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Push ! You have not won or lost this round.")
            draws += 1
        elif hand_evaluation(dealers_card) < 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Nice ! You have won this round.")
            players_win += 1
            wallet += 1.5 * wage
        elif hand_evaluation(dealers_card) > 21:
            print("")
            print(f"Your hand: {players_card}  ({hand_evaluation(players_card)})")
            print(f"Dealer hand: {dealers_card}  ({hand_evaluation(dealers_card)})")
            print("")
            print("Dealer busted ! You have won this round.")
            players_win += 1
            wallet += 1.5 * wage

    elif hand_evaluation(players_card) < 21:
        
        if players_card[0] != players_card[1]:
            print("Choice of Action:")
            print("1. Hit")
            print("2. Double Down")
            print("3. Stand")

            decision_1 = input("Please input action: ")

            if decision_1 == '2':
                double_down(players_card)

            elif decision_1 == '3':
                stand(players_card)

            elif decision_1 == '1':
                hit(players_card)
                
        elif players_card[0] == players_card[1]:
            print("Choice of Action:")
            print("1. Hit")
            print("2. Double Down")
            print("3. Stand")
            print("4. Split")
            
            decision_1 = input("Please input action: ")
            
            if decision_1 == '2':
                double_down(players_card)

            elif decision_1 == '3':
                stand(players_card)

            elif decision_1 == '1':
                hit(players_card)
                
            elif decision_1 == '4':
                split()
    
    print(f"Current Profit/Loss: {wallet}")
    to_continue_decision = input("Do you want to continue? (y/n)")
    if to_continue_decision == 'y':
        to_continue = True
    else:
        to_continue = False
print("")
print("Session Summary")
print("---------------")
print(f"Player Wins: {players_win}")
print(f"Dealer Wins: {dealers_win}")
print(f"Draws      : {draws}")
print("")
print(f"Session Profit/Loss: {wallet}")
print("")
print("Thank You for Playing This Blackjack Simulator !")