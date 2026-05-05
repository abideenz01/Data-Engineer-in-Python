# Set uses Hash Mechanism to speed up processing and provide results quickly
# Set Methods:

#1. Union(): provides all unique values of both sets
a={1,2,3,4,5}
b={3,4,5,6,7,8}
print(a.union(b))

#2. Intersection(): provides all shared values of both sets
a_1={1,2,3,4,5}
b_1={3,4,5,6,7,8}
print(a_1.intersection(b_1))

#3. symmetric_difference: provides all non-shared values of both sets
a_2={1,2,3,4,5}
b_2={3,4,5,6,7,8}
print(a_2.symmetric_difference(b_2))

#4. difference(): provides values that are in one set but not in other
#Rule: order is important: a.difference(b): means values that are in a but in b
a_3={1,2,3,4,5}
b_3={3,4,5,6,7,8}
print(a_3.difference(b_3))
print(b_3.difference(a_3))





