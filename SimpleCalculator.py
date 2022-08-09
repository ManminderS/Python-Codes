import  math
from re import M


ops = input("Please choose what operation would you like to do here?: (ADD, Sub, Division, Multiplication) : ")


while True:
    try:
        z = ['ADD', 'Sub', 'Division', 'Multiplication']
        if ops not in z:
            raise ValueError
    except ValueError:
        print("Try Again")
        exit()
    else:
        print("Thanks")
        break

#print("Please enter 2 digits below")
#x = float(input("Please first integer: "))
#y = float(input("Please second integer: "))
#a = x + y
#m = x * y
#s = x - y
#d = x / y
#mod = x // y

print("*" * 90)
print("Addition will be : ", a)
print("multiplication will be: ", m)
print("Subtraction will be: ", s)
print("Division will be: ", d)
print("Modulous will be: ", mod)
print("*" * 90)
