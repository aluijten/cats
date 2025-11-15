class cat:
    def __init__(self, name, age,state):
        self.name = name
        self.age = age
        self.state = state

    def __str__(self):
        return f"{self.name} ist {self.age} Jahre alt. Der Zustand ist {self.state}"



cat1 = cat("Tiggi", 4)
cat2 = cat("Stella", 14)

print(cat1)  
print(cat2)
