 # A spam comment is defined as a text containing followibg keywords:
# "Make a lot of money","buy now","subscribe this","click this". WAP to detect these spams

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
str=input("Enter a string:")
if(p1.lower() in str.lower() or p2.lower() in str.lower() or p3.lower() in str.lower() or p4.lower() in str.lower() ):
    print("It's a spam")
else:print("Not a spam.")



