class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ist {self.age} Jahre alt."
cat1 = Cat("Tiggi", 4)
cat2 = Cat("Stella", 14)

print(cat1)  
print(cat2)
