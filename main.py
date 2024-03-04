#import the random module
import random
#import my_module


#generate a random integer
random_integer = random.randint(1, 10)

#generate a random float without a range (0.000000 - 0.999999)
#get whole numbers by multiplying the float by 5
# e.g. random_float * 5

random_float = random.random() * 5

love_score = random.randint(1, 100)






#print(my_module.pi)
#print(random_integer)
#print(random_float)
print(f"Your love score is {love_score}")
