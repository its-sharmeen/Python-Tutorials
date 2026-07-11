# WAP to find greatest of 4 numbers entered by user

num1=int(input("Write 1st number:"))
num2=int(input("Write 2nd number:"))
num3=int(input("Write 3rd number:"))
num4=int(input("Write 1st number:"))

if((num1>num2)and(num1>num3)and(num1>num4)):
    print(f"{num1} is largest")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"{num2} is largest")
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"{num3} is largest")
else: print(f"{num4} is largest")