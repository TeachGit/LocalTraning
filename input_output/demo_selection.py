# n = 999
# if n % 3 == 0:
#     print(n, " is a multiple of 3")
# num = 5
# if num>0:
#     print(num," is positive number.")
# print("This is always prints.")
# num = -2
# if num>0:
#     print(num," is positive number.")
#
import random

# n = int(input("Enter Number: "))
# if n % 3 == 0:
#     print("multiple of 3")
# else:
#     print("not multiple of 3")

# score = int(input("Enter Score:"))
# if score < 50:
#     print("F")
# elif score<60:
#     print("E")
# elif score<70:
#     print("D")
# elif score<80:
#     print("C")
# elif score<90:
#     print("B")
# else:
#     print("A")


# n1 = int(input("Enter Number1: "))
# n2 = int(input("Enter Number2: "))
# n3 = int(input("Enter Number3: "))
# if (n1 > n2):
#     if (n1 > n3):
#         print("The biggest number is ", n1)
#     else:
#         print("The biggest number is ", n3)
# else:
#     if (n2 > n3):
#         print("The biggest number is ", n2)
#     else:
#         print("The biggest number is ", n3)


n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
# print(n1, "+", n2, " = ?")
# answer = int(input("Enter your answer: "))
answer = int(input(f"{n1} + {n2} = ? "))
if (answer == n1 + n2):
    print("Correct")
else:
    print("Incorrect. Try again!")
    # print("The answer ", n1, " + ", n2, " = ", n1 + n2)
    print("The answer of {} + {} = {}".format(n1,n2,answer))
