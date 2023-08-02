import module_calculate_score

scores = []
score = eval(input("khmer :"))
scores.append(score)
score = eval(input("Math :"))
scores.append(score)
score = eval(input("ICT :"))
scores.append(score)

print("Total score is ", module_calculate_score.totoalScore(scores))
module_calculate_score.average(scores, 3)
