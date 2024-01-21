class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


d1 = Date(year=2024)
print(d1)

d2 = Date()
d2.day = 21
d2.month = 11
d2.year = 2023

print(d2)
