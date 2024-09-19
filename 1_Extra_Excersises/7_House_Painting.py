x_height_house = float(input())
y_weight_hous = float(input())
h_height_roof = float(input())

green_paint_per_l = 3.4
red_paint_per_l = 4.3

front_wall = (x_height_house * x_height_house)-(1.2*2)
back_wall = x_height_house * x_height_house
side_wall = (x_height_house*y_weight_hous) - (1.5*1.5)

total_walls = front_wall + back_wall + (side_wall*2)

sides_roof = (x_height_house * y_weight_hous)*2
fronts_roof = ((h_height_roof * x_height_house)/2) *2
total_roof = sides_roof + fronts_roof

green_paint_needed= total_walls/green_paint_per_l
red_paint_needed = total_roof / red_paint_per_l

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
