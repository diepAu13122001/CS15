# bai 3
name = input("username: ")

email = input("email: ")
while (
    email.find("@") == -1
    or email.find(".") == -1
    or email.find("@") + 1 == len(email)
    or email.find(".") == -1
    or email.find(".") + 1 == len(email)
    or email.find("@.")
    or email.find(".@")
):
    print("error email")
    email = input("email again: ")
    continue


password = input("password: ")
while (len(password) < 8 
        or password.isdigit() 
        or password.isalpha()):
    print("error password")
    password = input("password again: ")
    continue

confirm_pass = input("confirm pass: ")
while (password != confirm_pass):
    print("confirm pass not match")
    confirm_pass = input("confirm pass again: ")
    continue
