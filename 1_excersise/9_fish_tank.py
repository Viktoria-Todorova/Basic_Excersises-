length_in_cm=int(input())
width_in_cm=int(input())
height_in_cm=int(input())
percent=int(input())

tank_volume=length_in_cm*width_in_cm*height_in_cm
volume_in_litres=tank_volume*0.001
space_occupied=percent/100
litres_needed=volume_in_litres*(1-space_occupied)


print(litres_needed)