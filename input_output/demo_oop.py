class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
    def my_function(self):
        print("This my function.")

person = Person("Panharith",27)
print(person)
person.my_function()
