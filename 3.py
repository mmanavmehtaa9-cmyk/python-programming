import random

lst = []

for i in range(10):
    lst.append(random.randint(-15,15))

print("Original List:",lst)

square_lst = [x**2 for x in lst]

print("Square List:",square_lst)
