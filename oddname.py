"""
William
"""
try:
    Name = input("Please enter your name = ")
except TypeError:
    print ("Please enter a correct response")
b=""
Name_1 = Name[1::2]
print (Name_1)