# dic = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(dic)
# print(dic["brand"])
# for key, value in dic.items():
#     print(key, " : ", value)


# sports = {'takwondo': 1, 'baseball': 9, 'basketball': 5, 'soccer': 11, 'tennis': 1, 'boxing': 1, 'shooting': 1,
#           'swimming': 1}
# sports["swimming"] = 2
# sports.update({"boxing": 2})
# sports["fishsport"] = 1
# sports.update({"chicken": 1})
# print(sports)
# if "baseball" in sports:
#     print(sports.pop("baseball"))  # remove
# print(sports)

dictionay_eg_to_kh = {
    "one": "មួយ", "two": "ពីរ", "three": "បី", "four": "បួន", "five": "ប្រាំ", "six": "ប្រាំមួយ", "seven": "ប្រាំពីរ",
    "eight": "ប្រាំបី", "nine": "ប្រាំបួន", "ten": "ដប់"
}
find = input("Enter Number in English:")
if find in dictionay_eg_to_kh:
    print(dictionay_eg_to_kh[find])
