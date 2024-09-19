from sys import maxsize
number_of_movies = int(input())
max_rating = -maxsize
min_rating = maxsize
current_movie_max = current_movie_min = ""
avg_rating = 0
for movies in range(number_of_movies):
    movie_name = input()
    rating = float(input())
    avg_rating += rating

    if rating > max_rating:
        max_rating = rating
        current_movie_max = movie_name
    elif rating < min_rating:
        min_rating = rating
        current_movie_min = movie_name

print(f"{current_movie_max} is with highest rating: {max_rating}")
print(f"{current_movie_min} is with lowest rating: {min_rating}")
print(f"Average rating: {(avg_rating/number_of_movies):.1f}")