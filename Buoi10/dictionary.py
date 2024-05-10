# dictionary = a changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly
capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Vietnam": "Hanoi",
}

#  get item
print(capitals["Vietnam"])
print(capitals.get("USA"))
# update item
capitals["China"] = "Hello"
capitals.update({"USA": "ABC"})
capitals.update({"USa": "ABC"})
print(capitals)
# remove item + clear
capitals.pop("USa")
del capitals["China"]
print(capitals)
# capitals.clear()

# print list
print(len(capitals))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

# duyet qua tung phan tu
for k, v in capitals.items():
    print(k, v)

for i in capitals:
    print(i, ": ") # in key
    print(capitals[i])

for i in capitals.values():
    print(i)