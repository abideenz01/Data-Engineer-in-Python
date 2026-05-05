print(2+3) #addition
print(2/3) #division
print(2*3) #multiplication
print(2-4) #subtraction
print(2**4) #exponential
print(7//2) #floor division
print(10%2) #modulus: check for even or odd numbers
#operators short cut
x=2
x+=3
print(x)
x-=1
print(x)
x-=3
print(x)
x*=2
print(x)
#Rounding
#Measuring distance
import math
print(abs(2-10)) # absolute value neglecting negative
price=35.54378
print(round(price)) # rounding half to even 
print(round(price,2)) #rounding upto 2 decimals
print(round(price,1)) #rounding upto 1 decimal place
print(math.ceil(price))
print(math.floor(price))
print(math.trunc(price))
#Random
#use to generate test data
import random
#print(random.random()) # random floating numbers b/w 0 and 1
print(random.randint(1,100)) # random numbers b/w 1 and 100
#validation
x=7.0
print(x.is_integer())
x=7.8
print(x.is_integer())
a=7.9
print(isinstance(a,float))
b=9
print(isinstance(b,int))
#Generate a random integer between 1 and 100 and check
#if the result is an even number
x=random.randint(1,100)
print(x)
print(x%2)


