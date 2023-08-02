n = int(input("Enter a number of n: "))
for i in range(n):
    print(" " * (i + 1), end="")
    for j in range(n - i):
        if (i % 2 != 0):
            print("* ", end="", )
    print()
