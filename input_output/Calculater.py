class Calculater:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print(self.n1, " + ", self.n2, " = ", self.n1 + self.n2)

    def sub(self):
        print(self.n1, " - ", self.n2, " = ", self.n1 - self.n2)

    def mul(self):
        print(self.n1, " * ", self.n2, " = ", self.n1 * self.n2)


calc1 = Calculater(10,20)
calc1.add()
