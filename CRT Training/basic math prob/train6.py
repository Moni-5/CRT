#write a program to check the on road price of a bike under the conditions
#if te price is greateer than 72k{actual price} then income taxe is 10% of actual price and insurance will be 15% of thr actual price
# if the price is greater than 150k and less than 200k te tax would be 25 % nad insurance would be 20%
#if the price is above 200k then tax will be 35% and insurance will be 28%
# else minimum price with us starts from 72k and enter a valid value
# on road price = actual price + tax + insurance

print("to check the on road price of the bike")
actprice=int(input("Enter the price:"))
if actprice>72000 and actprice<150000:
    incotax= (10/100)*actprice
    print(incotax)
    insurance= (15/100)*actprice
    print(insurance)
elif actprice>150000 and actprice<200000:
    incotax= (25/100)*actprice
    print(incotax)
    insurance= (20/100)*actprice
    print(insurance)
elif actprice>200000:
    incotax= (35/100)*actprice
    print(incotax)
    insurance= (28/100)*actprice
    print(insurance)
else:
    print("the min price starts from 72000 enteer te valid price")
onroadprice= (actprice+incotax+insurance)
print(onroadprice)
