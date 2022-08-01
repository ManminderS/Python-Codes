import random
names=['Mark', 'Sam', 'Henry']

#Set any array
random_array_item=random.choice(names)

#Declare a variable as a random choice
print(random_array_item)

#Print the random choice
#Or, if you want to arrange them in any order:
for j in range(names):
    print(random.choice(names))