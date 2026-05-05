Numbers=[1,2,1000,4,5,6]
Numbers_1=[0,1,2,3,4,5]
print(f"MAX: {max(Numbers)}")
print(f"MIN: {min(Numbers)}")
print(f"SUM: {sum(Numbers)}")
print(f"LENGTH: {len(Numbers)}")
print(f"ALL: {all(Numbers_1)}") # All real values?
print(f"ANY: {any(Numbers)}") # Any value is real 

# USE .count() to find out How many times a specific value appears
Letters=['a','a','a','b','c','d','e','f']
Numbers_2=[1,2,2,2,3,3,4,4,5,6,7,8]
print(Letters.count('a')) # how many times "a" appears
print(Letters.count('f')) # how many times "f" appears
print(f"Count: {Numbers_2.count(2)}")
print(f"Count: {Numbers_2.count(3)}")
# Find out index of a value
print(f"INDEX: {Numbers_2.index(8)}")
# in and not in operator
numbers=[1,2,3,4,5]
print(4 in numbers)
print(6 in numbers)
print(4 not in numbers)
# == operator 
list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(list_1==list_2)
# > & < operator
list_1=[2,2,3,4]
list_2=[1,2,3,4]
print(list_1>list_2)
list_1=[2,2,3,4]
list_2=[3,2,3,4]
print(list_1<list_2)
#is operator: compares memory addresses of list not values
list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(list_1 is list_2)
