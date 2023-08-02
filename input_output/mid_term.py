# total_price = eval(input("Input total price(Original Price):"))
# discount_rate = 0
# discount_amount = 0
# discount_price = 0
# if total_price >= 40000:
#     discount_rate = 4 / 100
#     discount_amount = discount_rate * total_price
#     discount_price = total_price - discount_amount
# elif total_price >= 20000:
#     discount_rate = 2 / 100
#     discount_amount = discount_rate * total_price
#     discount_price = total_price - discount_amount
# elif total_price >= 10000:
#     discount_rate = 1 / 100
#     discount_amount = discount_rate * total_price
#     discount_price = total_price - discount_amount
# else:
#     discount_rate = 0
#     discount_amount = discount_rate * total_price
#     discount_price = total_price - discount_amount
#
# print("Original price : ", total_price, " Discounted price :", discount_price)
# print("Discount rate: ", discount_rate, " Discount amount :", discount_amount)


# def sum(start, end):
#     sum = 0
#     for i in range(start, end + 1):
#         sum += i
#     return sum
#
#
# n1 = eval(input("1st number: "))
# n2 = eval(input("2st number: "))
# if (n1 < n2):
#     print(n1, " from ", n2, "to sum is :", sum(n1, n2))
# else:
#     print(n2, " from ", n1, "to sum is :", sum(n2, n1))


n = int(input("Enter a number of n: "))
for i in range(n):
    print(" " * (i + 1), end="")
    for j in range(n - i):
        print("* ", end="",)
    print()
