age1 = 24
age2 = 16
if(age1 >= 18 and age2 >= 18):
    print("Both are adults")
elif(age1 >= 18 or age2 >= 18):
    print("At least one is an adult")
else:
    print("Neither is an adult")

is_hungry = False
if(not is_hungry):
    print("You are not hungry")