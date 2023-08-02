# Page 158 Exercise 10 using loop show start pattern
n = eval(input("Enter N:"))
for i in range(1, n, 1):
    for j in range(i):
        print("* ", end="")
    print()
for x in range(n, 1, -1):
    for y in range(x - 1, 1, -1):
        print("* ", end="")
    print()
