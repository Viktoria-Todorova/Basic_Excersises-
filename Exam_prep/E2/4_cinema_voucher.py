vaucher = int(input())
price= count_tickets = count_other=0
while True:
    name_of_movie = input()

    if name_of_movie == "End":
        break

    if len(name_of_movie) > 8:
        price = ord(name_of_movie[0]) + ord(name_of_movie[1])

        if price > vaucher:
            break
        else:
            vaucher -= price

        count_tickets += 1

    elif len(name_of_movie) <= 8:

        price = ord(name_of_movie[0])
        if price > vaucher:
            break
        else:
            vaucher -= price

        count_other += 1




print(f'{count_tickets}')
print(f"{count_other}")


