x = 12 # global var 

def my_func ():
    global x
    x = 10 

print(x)
my_func()
print(x)

# if 3 < 4: 
#     a = 10 # global var 
# else:
#     print(1)

# # print(a)
# # print(x)

# def square (w, h):
#     global s # declare
#     s = w * h

# square(4, 3)
# print(s)