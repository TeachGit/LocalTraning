# Page 142 Exercise 3 how many credits they have taken
credit = "Unknown"
taken = eval(input("Enter Your Taken:"))
if taken <= 23:
    credit = "Freshman"
elif taken <= 53:
    credit = "Sophomore"
elif taken <= 83:
    credit = "Junior"
else:
    credit = "Senior"
print("Your credit is ", credit)
