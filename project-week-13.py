#collecting name of the visitor

from multiprocessing.sharedctypes import Value
from random import random
from secrets import choice
from string import ascii_letters
from unicodedata import digit
import string
import random


print("Welcome to Ec2 Generator")
print("-" * 90)
name = input("Please enter your name: ")
name = (name.capitalize())    # capitalize : Makes first alphabet capital
print("Hi," + name)
print("-" * 60)


#Get the user department name
dept = input("Please enter your department " + name +  "(HR, Digital Marketing, IOS, Android?)" ).upper()
list = ["HR", "Digital Marketing", "IOS", "Android"]

if dept not in list:
    print("")
    print("-->Either you have input the wrong department - or - We dont support this department")
    exit()
    
else:
    print("thanks")


#EC2 instances 
while True:
    try:
        ec2 = int(input("Enter the amount of EC2 instances required : "))   
        print( " Thanks!! Provisioning Instances ")
        print( str(ec2) +   " Instances Provisioned")
        break
    except ValueError:
        print("Looks like an input error, Please re-try with numeric value")
        continue
    else:
        break

N = 3
for x in range(ec2):
 uid = str(''.join([random.choice(string.ascii_letters + string.digits) for z in range(10)]))
 print('-' * 90)
 print('{}-{}'.format(dept[0 : N], uid))
 
