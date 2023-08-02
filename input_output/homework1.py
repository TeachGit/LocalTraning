# Page 124 Exercise 5 Convert Celsius temperature to Fahrenheit
# celsius = eval(input("Enter Celsius Temperature:"))
# fahrenheit = (celsius * (9 / 5)) + 32
# print(fahrenheit)

# Page 142 Exercise 3 how many credits they have taken
# credit = "Unknown"
# taken = eval(input("Enter Your Taken:"))
# if taken <= 23:
#     credit = "Freshman"
# elif taken <= 53:
#     credit = "Sophomore"
# elif taken <= 83:
#     credit = "Junior"
# else:
#     credit = "Senior"
# print("Your credit is ",credit)

# Page 158 Exercise 10 using loop show start pattern
n = eval(input("Enter N:"))
for i in range(1, n, 1):
    for j in range(i):
        print("* ", end="")
    print()
for i in range(n, 1, -1):
    for j in range(i - 1, 1, -1):
        print("* ", end="")
    print()
