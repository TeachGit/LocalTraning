sports = ('Takwondo', 'Baseball', 'Basketball', 'Soccer', 'Tennis', 'Boxing', 'Shooting', 'Swimming')
for index,value in enumerate(sports):
    if index % 2 != 0:
        print(index, ":", value)