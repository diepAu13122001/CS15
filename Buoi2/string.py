# print string has multi lines
s = "There are\nmulti\nlines"
# print(s)

s1 = """This is 
    multi
lines"""
# print(s1)

# operator fot str
# x = input("Type a number: ")
# print("You have " + x + " son")
# string interpolation
# print(f"You have {x * 3 + 2} son")

a = "abc"
# print(a*5)

# string methods
# name = input("Your name: ")
# print(len(name))
# print(name.find("D"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.count("d"))
# print(name.replace("d", "b"))
# print(name.isalpha())

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:end]
# name = "Diep Au"
# first_name = name[name.find("D"):4]
# first_name = name[:4]
# print(first_name)

# last_name = name[name.find("A"):]
# print(last_name)

# reserve_name = name[::-1]
# print(reserve_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_web_name = slice(7, -4)
slice_web_name = slice(7, website1.find("."))
web1_name = website1[slice_web_name]
print(web1_name)

# type casting = convert the data type of a value to another data type
str()
# multiple assignment
