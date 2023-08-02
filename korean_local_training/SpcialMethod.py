class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return Vector3D(self.x == other.x and self.y + other.y and self.z + other.z)

    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)


u = Vector3D(1, 1, 1)
v = Vector3D(2, 3, 4)
print(u + v)
