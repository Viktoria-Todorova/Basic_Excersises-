widht_sapce = int(input())
lenght_space = int(input())
height_space = int(input())
free_space = widht_sapce * lenght_space * height_space
space_taken = 0
while free_space > 0 :
    cubes = input()

    if cubes != "Done":
        cubes_count = int(cubes)
        space_taken += cubes_count
        if space_taken > free_space:
            print(f"No more free space! You need {space_taken-free_space} Cubic meters more.")
            break
    else:
        print(f"{free_space-space_taken} Cubic meters left.")
        break
