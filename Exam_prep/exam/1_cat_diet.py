percent_lipids = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

gram_lipids = ((percent_lipids/100) * total_calories) /9
gram_protein = ((percent_protein/100) * total_calories) / 4
gram_carbs = ((percent_carbs/100) * total_calories) / 4
total_grams = gram_lipids + gram_protein + gram_carbs
calories_per_gram = total_calories / total_grams
percent = 100 - percent_water

weight_without_water = (percent/100) * calories_per_gram

print(f"{weight_without_water:.4f}")
