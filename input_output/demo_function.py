# def main():
#     print(min(min(5, 6), min(51, 6)))
#
# def min(n1, n2):
#     if n1 < n2:
#         return n1
#     return n2
# main()

# def nPrintln(message, n):
#     for i in range(n):
#         print(message)
#
# nPrintln(n=4,message="hello")

# x = 4
# y = x
# print(id(x))
# print(id(y))


# def factorial(n):
#     if n == 0:
#         return 1  # base case
#     return n * factorial(n - 1)  # recursive case
# print(factorial(5))

# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n - 1)
# print(sum(4))

def nMessage(message,n):
    if n >= 1:
        print(message)
        nMessage(message,n-1)

nMessage("Hello",5)