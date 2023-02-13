import random

#number of decks
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

#kaartide segamine
random.shuffle(deck)


player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]


print("Player's hand:", player_hand)
print("Player's hand value:", sum(player_hand))


print("Dealer's hand: [{}, X]".format(dealer_hand[0]))


while True:
    choice = input("Do you want to hit or stand? ").lower()
    if choice == "hit":
        
        player_hand.append(deck.pop())
        
        print("Player's hand:", player_hand)
        print("Player's hand value:", sum(player_hand))
        
        if sum(player_hand) > 21:
            print("You lose!")
            break
    elif choice == "stand":
        
        print("Dealer's hand:", dealer_hand)
        print("Dealer's hand value:", sum(dealer_hand))
        
        while sum(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print("Dealer's hand:", dealer_hand)
            print("Dealer's hand value:", sum(dealer_hand))
        
        if sum(dealer_hand) > 21:
            print("Dealer busts! You win!")
        elif sum(player_hand) > sum(dealer_hand):
            print("You win!")
        elif sum(player_hand) == sum(dealer_hand):
            print("It's a tie!")
        else:
            print("You lose!")
        break
    else:
        
        print("Invalid input. Please enter 'hit' or 'stand'.")
