# tuple1 = (1, 2, 3, 4, 5, 6)
# print("max :", max(tuple1))
# print("min :", min(tuple1))
# print("sum :", sum(tuple1))
# tuple2 = 2 * tuple1  #duplicate
# print(tuple2)
# tuple3 = tuple1 + tuple2
# print(tuple3)
# print(tuple3[0:4])
# print(2 in tuple3)
# for i in tuple3:
#     print(i,end=' ')
# tuple1 = tuple3
# print(tuple1)

# print(tuple3 < tuple2)

# tuple1 = ()
# tuple1 = (1, 2, 3, 4)
# result = tuple1[1]
# print(tuple1[1:3])

# numberList = [1,2,3,4,5]
# tuple2 = tuple(numberList)
# print(tuple2)
# numberList = list(tuple2)
# numberList[3] = 10
# tuple2 = tuple(numberList)
# print(tuple2)

# dayofweek = ["monday","tue","wed","the","fri","sat","sun"]
sports = ('Takwondo', 'Baseball', 'Basketball', 'Soccer', 'Tennis', 'Boxing', 'Shooting', 'Swimming')
for index,value in enumerate(sports):
    if index % 2 != 0:
        print(index, ":", value)
