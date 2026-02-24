
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
dict3 = {"e": 50, "f": 60}


dict4 = {**dict1, **dict2, **dict3}


print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Concatenated Dictionary (dict4):", dict4)
