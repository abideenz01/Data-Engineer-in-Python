# Summary 
#1. Avoid using Assignment = to create copy since it is confusing
#2. Use .copy() method for shallow copy when dealing with simple,one dimensional, flat lists
#3. Use deepcopy() function to create deep copy when dealing with 2-dimensional lists 

import copy
list=[['a','b'],
      ['c','d']]
copy_list=copy.deepcopy(list)
# It produces 'False' because list and copy_list are seperate 
# lists having completely different memory addresses 
print(f" Same Object? (Verification of shallow copy): {list is copy_list}")
print(f" Same List? (verification of Deep Copy):      {list[0] is copy_list[0]}")
