bottles = int(input())
count = total_used = dishes_cpunt =pots_count = 0
total_liquid = bottles * 750

while True:
    dishes = input()

    if dishes == "End":
        print("Detergent was enough!")
        print(f"{dishes_cpunt} dishes and {pots_count} pots were washed.")
        print(f"Leftover detergent {total_liquid - total_used} ml.")
        break


    count_disces = int(dishes)
    count += 1

    if count % 3 == 0:
        total_used += count_disces * 15
        pots_count += count_disces
    else:
        total_used += count_disces * 5
        dishes_cpunt += count_disces

    if total_used > total_liquid:
        print(f"Not enough detergent, {total_used - total_liquid} ml. more necessary!")
        break















