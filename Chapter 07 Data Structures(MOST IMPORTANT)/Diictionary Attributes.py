# Dictionary Attributes
# 1. Dictionary is ordered
# 2. Dictionary allows unique keys and duplicate values
# 3. Dictionary is not indexed but keyed: we can access values using keys
# 4. Dictionary is mutable 

#Cheking order
dict_1={'Name':'Zain','Age':30,'Country':'USA'}
print(dict_1)
#Checking if it allows duplicates
dict_2={'Name':'Zain','Age':30,'Country':'UK','Country':'Spain'}
print(dict_2)
#Checking if is indexed
dict_3={'Name':'Zain','Age':30,'Country':'Spain'}
print(dict_3['Name'])
dict_4={'Name':'Zain','Age':30,'Country':'Spain'}
dict_4['Name']='John'
print(dict_4)



