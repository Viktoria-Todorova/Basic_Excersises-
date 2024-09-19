price_skumria_kg = float(input())
price_caca_kg = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_muscles = int(input())

price_palamud = price_skumria_kg*1.6
final_price_palamud=price_palamud*kg_palamud

price_safrid = price_caca_kg*1.8
final_price_safrid=price_safrid*kg_safrid

final_price_muscles = kg_muscles* 7.5

total_price=final_price_palamud+final_price_safrid+final_price_muscles

print(f"{total_price:.2f}")

