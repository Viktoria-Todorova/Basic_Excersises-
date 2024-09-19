
yearly_price_of_training=int(input())

price_of_shoes=yearly_price_of_training-(yearly_price_of_training*0.4)
price_of_clothes=price_of_shoes-(price_of_shoes*0.2)
price_of_ball=(price_of_clothes*0.25)
price_of_accesories=price_of_ball*0.2

total_price=yearly_price_of_training+price_of_shoes+price_of_clothes+price_of_ball+price_of_accesories


print(total_price)

