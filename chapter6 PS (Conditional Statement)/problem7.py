# WAP to find out whether a given post is talking about "Harry" or not

post=input("Enter your post:").lower()
if("Harry".lower() in post):
    print("Your post talks about harry..")
else:print("Your post dosen't talk about harry")