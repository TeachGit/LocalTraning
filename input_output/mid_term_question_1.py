total_price = eval(input("Input total price(Original Price):"))
discount_rate = 0
discount_amount = 0
discount_price = 0
if total_price >= 40000:
    discount_rate = 4 / 100
    discount_amount = discount_rate * total_price
    discount_price = total_price - discount_amount
elif total_price >= 20000:
    discount_rate = 2 / 100
    discount_amount = discount_rate * total_price
    discount_price = total_price - discount_amount
elif total_price >= 10000:
    discount_rate = 1 / 100
    discount_amount = discount_rate * total_price
    discount_price = total_price - discount_amount
else:
    discount_rate = 0
    discount_amount = discount_rate * total_price
    discount_price = total_price - discount_amount

print("Original price : ", total_price, " Discounted price :", discount_price)
print("Discount rate: ", discount_rate, " Discount amount :", discount_amount)