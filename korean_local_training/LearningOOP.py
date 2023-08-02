class Person:
    def __init__(self,pname,page):
        self.var_name = pname
        self.var_page = page

p1 = Person("Panharith",29)
p2 = Person("Noch",49)
p3 = Person("Vanary",46)
print("Name: ",p1.var_name , " Age = ", p1.var_page)
print("Name: ",p2.var_name , " Age = ", p2.var_page)
print("Name: ",p3.var_name , " Age = ", p3.var_page)