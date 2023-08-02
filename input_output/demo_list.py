# t1 = {1, 2, 3}
# t2 = {6, 4, 5, 3, 1, 2}
# t3 = {3, 2, 1}
# print(t1 == t3)
# print(t1 <= t2)
import random

# mylist = ["apple", "banana", "orange", "mango", "kiwi"]
# mylist[1:3] = ["watermelon", "strawberry"]
# print(mylist)
# mylist[1:3] = ["strawberry"]
# print(mylist)
# mylist.insert(2, "watermelon")
# print(mylist)
# mylist.append("papaya")
# print(mylist)

# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# print("Before :", numbers)
# numbers.insert(5, 6)
# numbers.append(10)
# print("After :", numbers)

# fruit = ["apple", "banana", "orange", "mango", "kiwi"]
# animal = ["cow", "dog", "cat"]
# animal.extend(fruit)
# print(animal)
# puthys = ["black", "white", "orange"]
# thuys = ["yellow", "pink", "white"]
# puthys.extend(thuys)
# print(puthys)
# for i in puthys:
#     print(i, end=" ")
# print()
# for i in range(len(puthys)):
#     print(puthys[i], end=" ")

# todoList = ["clean teeth","showing","break first",""]
todoList = []
# todoList.append("clean teeth")
# todoList.append("do exercise")
# todoList.append("showing")
# todoList.append("break first")
# todoList.append("go to study")
# print(todoList)
# todoList.pop(0)
# todoList.remove("showing")
# print(todoList)
# user = input("click + for add:")
# while user != "e":
#     todo = input("Enter Todo:")
#     todoList.append(todo)
#     print(todoList)
#     user = input("click e for add:")


# questions = ["name", "color"]
# answers = ["puthy", "black","tt"]
# for q, a in zip(questions, answers):
#     # print(f"what is your {q}? It is {a}")
#     print("what is your {}? It is {}".format(q,a))

# numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# print(max(numbers))
# print(min(numbers))
# print(random.choice(numbers))
# numbers.sort(reverse=True)
# print(numbers)


scores = []
for i in range(3):
    score = eval(input("Enter Score of Subject:"))
    scores.append(score)
print(scores)
average = sum(scores) / len(scores)
max = max(scores)
min = min(scores)
count = 0
for i in scores:
    if i >= 80:
        count += 1
print("Average of Score is ", average)
print("Max of score is ", max)
print("Min of score is ", min)
print("Score 80 or higher :", count)
