width_cake = int(input())
lenght_cake = int(input())
size_piece = width_cake * lenght_cake

while size_piece > 0 :
    piece_pick = input()

    if piece_pick != "STOP":
        piece_count = int(piece_pick)
        size_piece -= piece_count
        if size_piece < 0:
            print(f"No more cake left! You need {abs(size_piece)} pieces more.")
            break
    else:
        print(f"{size_piece} pieces are left.")
        break
