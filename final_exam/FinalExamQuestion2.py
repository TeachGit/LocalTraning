# 1. Make dictionary Country with Capital city
capital_cities = {
    "Korea": "Seoul",
    "Cambodia": "Phnom Penh",
    "USA": "Washington",
    "France": "Paris"
}
# 2. Show countries in the dictionary
for key, value in capital_cities.items():
    print(key, end='  ')
print()

# 3. Show capital cities in the dictionary
for key, value in capital_cities.items():
    print(value, end='  ')
print()

# 4. Add the Germany and Berlin as the capital city to the dictionary
capital_cities["Germany"] = "Berlin"

# 5. Print the country and related city as follows
print()
for key, value in capital_cities.items():
    print("country: ", key, ", city: ", value)

# 6. Remove the last added item and show the result
capital_cities.popitem()
print(capital_cities)


