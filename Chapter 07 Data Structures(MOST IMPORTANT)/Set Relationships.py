# checking relationships b/w sets
#1. issubset():checks if one set is subset of other
a={20,40,60}
b={20,40,60,80,100}
print(a.issubset(b))

#2. issuperset(): checks if one set holds all values of other set
a_1={20,40,60}
b_1={20,40,60,80,100}
print(b_1.issuperset(a_1))

#3. isdisjoint(): checks if both sets are holding completely different values
a_2={110,120,130}
b_2={20,40,60,80,100}
print(a_2.isdisjoint(b_2))



