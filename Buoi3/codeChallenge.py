num = None
while(not num):
    num = input("Nhap 1 so chan: ")
    if (num.isdigit()):
        if(int(num)%2 == 0):
            print(f"{num} la so chan")
            break
    print(f"{num} khong phai so chan")  
    num = None
    continue