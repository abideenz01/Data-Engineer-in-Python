# Why do we need iterators?
#1. For Looping
#2. To Save Memory
#3. For Speed and Flexibility
# Iterators: 
# 1.enumerate
# 2.reversed
# 3.zip
# 4.map
# 5.filter

#Enumerate
# Use Case: to identify exact location of bad data 
Letters=['a','','c','d']
for index, value in enumerate(Letters):
    print(index,value)
print("-----------------------")
#Reversed
Letters_1=['a','b','c','d']
for l in (reversed(Letters_1)):
    print(l)

#Zip
Ids=['101','102','103','104']
Names=['Zain','Ali','Sara','John']
for ID,Name in zip(Ids,Names):
    print(ID,Name)

#map(function,Iterable)
Names_1=['zain','sophie','karen','tiffany']
print(list(map(str.upper,Names_1)))

#map USE CASES
#converting string to integer
Numbers=['1','2','3']
print(list(map(int,Numbers)))

#cleaning unwanted spaces in data
Names_2=[' Zain ',' Maria','Jacky ']
print(list(map(str.strip,Names_2)))
print("---------------------")
#cleaning unwanted spaces in data using map in loop
Names_3=[' Zain ',' Maria','Jacky ']
for Name in map(str.strip,Names_3):
    print(Name)

#Filtering the bad data
items=['a','',None,False,'b','c']
print(list(filter(None,items))) # use None or bool with filter to remove unwanted data

#filtering only alphabetical values
items_1=['SQL','123','PYTHON','987']
print(list(filter(str.isalpha,items_1)))

#using loop
items_2=['SQL','123','PYTHON','987']
for n in filter(str.isalpha,items_1):
    print(n)









