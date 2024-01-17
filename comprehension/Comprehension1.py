# Comprehension list:
double = [i * 2 for i in range(10)]
print(double)

# Default method:
double = []
for i in range(10):
    double.append(i * 2)
print(double)


# Using if statement:
evenOfDoubles = [i * 2 for i in range(10) if i % 2 == 0]
print(evenOfDoubles)

# Default method:
evenOfDoubles = []
for i in range(10):
    if i % 2 == 0:
        evenOfDoubles.append(i * 2)
print(evenOfDoubles)
