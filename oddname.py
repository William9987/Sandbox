"""
William
"""
try:
    Name = input("Please enter your name = ")
except TypeError:
    print ("Please enter a correct response")
b=""
for i in range(len(Name)):
    if (i%2)==0:
        b+=Name[i]