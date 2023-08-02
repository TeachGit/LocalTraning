set1 = set("abac")
print(set1)

s1 = {1, 3, 5}
s2 = {1, 2, 4}
print("union :", s1.union(s2))
print("intersection :", s1.intersection(s2))
print("difference :",s1.difference(s2))
print("symmetric_difference :",s1.symmetric_difference(s2))
print(s1)
s1.add(6)
print("add item to set", s1)
s1.remove(3)
print("remove item", s1)
s1.clear()
print("clear all item", s1)
