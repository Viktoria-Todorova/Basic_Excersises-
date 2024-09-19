
cover_per_m=int(input())
paint_per_litres=int(input())
thinner_per_litres=int(input())
hours_needed=int(input())

price_cover=(cover_per_m+2)*1.5
price_paint=(paint_per_litres+(paint_per_litres* 0.1))*14.5
price_thinner=thinner_per_litres*5
price_bags=0.40


total_price_of_matterials=price_cover+price_paint+price_thinner+price_bags
total_price_for_workers=(total_price_of_matterials*0.3)*hours_needed

final_price=total_price_of_matterials+total_price_for_workers

print(final_price)
