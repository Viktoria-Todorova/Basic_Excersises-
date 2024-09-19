from sys import maxsize
max_num = -maxsize
current_player = ""
turn = 0
while True:
    name = str(input())
    points_player = 0

    if name == "Stop":
        break
    turn += 1
    for every_player in range(len(name)):
        current_number = int(input())
        current_letter = ord(name[every_player])

        if current_number == current_letter:
            points_player += 10
        else:
            points_player += 2

        if points_player > max_num or (points_player == max_num and turn > max_turn):
            max_num = points_player
            current_player = name
            max_turn = turn

print(f"The winner is {current_player} with {max_num} points!")




