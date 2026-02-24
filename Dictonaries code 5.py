prices = {
    "rice": 50,
    "wheat": 40,
    "sugar": 45,
    "milk": 30
}
quantity = {
    "rice": 2,
    "wheat": 3,
    "sugar": 1,
    "milk": 4
}

total = 0

for item in prices:
    total += prices[item] * quantity[item]

print("Total Bill =", total)
