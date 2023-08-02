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
