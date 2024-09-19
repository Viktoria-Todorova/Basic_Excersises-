player1 = input()
player2 = input()
count1_player = count2_player = count = 0

while True:
    card1 = input()

    if card1 == "End of game":
        print(f"{player1} has {count1_player} points")
        print(f"{player2} has {count2_player} points")
        break
    card2 = input()

    player1_card = int(card1)
    player2_card = int(card2)

    if player1_card > player2_card:
        count1_player += player1_card - player2_card
    elif player1_card < player2_card:
        count2_player += player2_card - player1_card
    elif player1_card == player2_card:
        print("Number wars!")
        card_1 = int(input())
        card_2 = int(input())
        if card_1 > card_2:

            print(f"{player1} is winner with {count1_player} points")
            break
        elif card_2 > card_1:

            print(f"{player2} is winner with {count2_player} points")
            break




