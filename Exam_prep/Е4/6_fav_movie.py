from sys import maxsize
max_num = -maxsize
current_movie = ""
count_movies = 0
while True:
    movie = input()
    current_points = 0

    if movie == "STOP":
        break
    count_movies += 1
    if count_movies == 7:
        print("The limit is reached.")
        break

    for letters in range(len(movie)):
        current_points += ord(movie[letters])

        if movie[letters].isupper():
            current_points -= len(movie)
        elif movie[letters].islower():
            current_points -= 2 * len(movie)

    if current_points > max_num:
        max_num = current_points
        current_movie = movie

print(f"The best movie for you is {current_movie} with {max_num} ASCII sum.")







