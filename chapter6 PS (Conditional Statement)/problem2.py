# WAP to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

dict={}
subject=input("Enter subject:")
m1=int(input("Enter marks:"))
dict.update({subject:m1})
subject=input("Enter subject:")
m2=int(input("Enter marks:"))
dict.update({subject:m2})
subject=input("Enter subject:")
m3=int(input("Enter marks:"))
dict.update({subject:m3})

if(m1>33 and m2>33 and m3>33 and ((m1+m2+m3)/3)>44):
    print("You are pass")
else:print("You are failed")    