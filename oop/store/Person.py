class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if self.age is None:
            return self.name
        return f'{self.name} ({self.age} years)'