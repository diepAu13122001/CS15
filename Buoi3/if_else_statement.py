#  age 
# age = int(input("Enter your age: "))

# if (age < 0):
#     print("not born")
# elif (age < 18):
#     print("teen")
# elif (age < 60):
#     print("adult")
# else:
#     print("old")


# boolean
a = True
b = False

# print(a and b)
# print(b or a)
# print(not a)
# print(not b)

# keo bua bao
import random
list_str = ["keo", "bua", "bao"]

def randomSkill(list_skill):
    return random.choice(list_skill)

userInput = input("keo, bua or bao? ")

machineInput = randomSkill(list_str) 
def checkResult(user, machine):
    if (user == "keo"):
        if (machine == "bao"):
            print("thang")
        elif(machine == "bua"):
            print("thua")
        else:
            print("hoa")
    
    if (user == "bua"):
        if (machine == "keo"):
            print("thang")
        elif(machine == "bao"):
            print("thua")
        else:
            print("hoa")

    if (user == "bao"):
        if (machine == "bua"):
            print("thang")
        elif(machine == "keo"):
            print("thua")
        else:
            print("hoa")

print(machineInput)
checkResult(machine=machineInput, user=userInput)