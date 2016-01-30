
x = 5

if x > 5:
    print("x is greater than 5")
elif x==5:
    print("x is 5")
else:
    print("x is NOT Greater than 5")

if x == 5 and type(x) is int:
    print("x is greater than 5")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer, but is not equal to 5")

x = 10
if x == 5 and type(x) is int:
    print("x is greater then 5")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer, but is not equal to 5")

x = 100
if x == 5 and type(x) is int:
    print("x is greater then 5")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer, but is not equal to 5")
else:
    print(x)
