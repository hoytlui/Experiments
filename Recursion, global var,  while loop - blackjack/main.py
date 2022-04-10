import random
from art import logo


# global variables
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
DECK_OF_CARDS = CARDS * 4


def deal_card():
    """Return a random card from a deck of cards."""
    card_drawn = random.choice(DECK_OF_CARDS)
    DECK_OF_CARDS.remove(card_drawn)
    return card_drawn


def calculate_score(card_list):
    """Return the calculated score from a card list."""
    score = sum(card_list)
    # blackjack scenario
    if score == 21 and len(card_list) == 2:
        new_score = score
    # 'A' scenario
    elif score > 21 and 11 in card_list:
        idx = card_list.index(11)
        card_list[idx] = 1
        new_score = sum(card_list)
    # other scenarios
    else:
        new_score = score
    return new_score


def compare_score(player_score, dealer_score):
    """Return announcement from compared scores."""
    if player_score > 21 and dealer_score > 21:
        return "It's a draw."
    elif dealer_score == 21 or player_score > 21:
        return "You lose."
    elif player_score == 21 or dealer_score > 21:
        return "You win."
    elif player_score == dealer_score:
        return "It's a draw."
    elif player_score > dealer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(logo)
    print("Welcome to my table. Take a seat.\n")
    # create lists for player and dealer
    player_cards = []
    dealer_cards = []
    
    # distribute 2 cards to each participant
    for _ in range(0, 2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    print(f"Your cards: {player_cards}")
    print(f"Dealer's cards: [{dealer_cards[0]}, _]\n")
    
    # loop game - player's turn
    end_of_game = False
    while not end_of_game:
        player_score = calculate_score(player_cards)
        print(f"Your cards: {player_cards}, your score: {player_score}\n")
        # end game if score >= 21
        if player_score >= 21:
            end_of_game = True
        
        # force to accept card if score <= 16
        elif player_score <= 16:
            input("Press 'enter' to accept card.")
            player_cards.append(deal_card())
            end_of_game = False
        
        # let player choose whether to draw another card if score in between 17 and 20
        else:
            to_continue = input("Press 'space' to draw another card. Press anything else to pass.")
            if to_continue == ' ':
                player_cards.append(deal_card())
                end_of_game = False
            else:
                end_of_game = True

    # loop game - dealer's turn
    dealer_score = calculate_score(dealer_cards)
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\n")  
    while dealer_score <= 16:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}\n")  
    
    # print announcement when game ends 
    print(compare_score(player_score=player_score, dealer_score=dealer_score))



while input("Type 'y' to start the game. ").lower() == 'y':
    play_game()