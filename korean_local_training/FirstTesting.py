# ict_score = eval(input("Enter ICT Score:"))
# if ict_score >= 45:
#     grade = 'A'
#     print("Excellent")
# elif ict_score >= 40:
#     grade = 'B'
#     print("Best")
# elif ict_score >= 35:
#     grade = 'C'
#     print("Good")
# elif ict_score >= 30:
#     grade = 'D'
#     print("Medium")
# elif ict_score >= 25:
#     grade = 'E'
#     print("Low")
# else:
#     grade = 'F'
#     print("Bad")
# print("Your grade: ",grade)

#
# score = [40, 45, 30, 20, 50]
# name = ["Kim", "Ly", "Park", "Long", "Panha"]
# grade = ["", "", "", "", ""]
# for i in range(len(score)):
#     if score[i] >= 45:
#         grade[i] = 'A'
#     elif score[i] >= 40:
#         grade[i] = 'B'
#     elif score[i] >= 35:
#         grade[i] = 'C'
#     elif score[i] >= 30:
#         grade[i] = 'D'
#     elif score[i] >= 25:
#         grade[i] = 'E'
#     else:
#         grade[i] = 'F'
#     print("Name :", name[i], "have grade :", grade[i])

def getGrade(score):
    if score >= 45:
        grade = 'A'
    elif score >= 40:
        grade = 'B'
    elif score >= 35:
        grade = 'C'
    elif score >= 30:
        grade = 'D'
    elif score >= 25:
        grade = 'E'
    else:
        grade = 'F'
    return grade

score = [40, 45, 30, 20, 50]
name = ["Kim", "Ly", "Park", "Long", "Panha"]
grade = ["", "", "", "", ""]
for i in range(len(score)):
    grade[i] = getGrade(score[i])
    print("Name :", name[i], "have grade :", grade[i])

