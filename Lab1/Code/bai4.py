year = input("What year is it?")
if len(year) == 4 and year.isdigit():
    print("HAPPY NEW YEAR\n\t!!!"+ str(year)+"!!!")
    # ve phao bong
    print("   . : .")
    print(" '.  :  .'")
    print(".  '.:.'  .")
    print(".  .':'.  .")
    print(" .'  :  '.")
    print("   ' : '")
else:
    print("Số bạn nhập không hợp lệ.")