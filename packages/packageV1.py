from package1 import Module1
from package1 import Module2
from package2 import Module1 as module1_sub

print(type(Module1))
print(Module1.sum(2, 3))

Module2.main()
print('Sum', Module1.sum(2, 3))
print('Sub', module1_sub.sub(2, 3))
