matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix_copy= matrix.copy()
matrix.pop()
matrix_copy[0].insert(0,'z')
print(f"Original Matrix: {matrix}")
print(f"Copied matrix:    {matrix_copy}")
print('----------------------------------------')
# Deep copy to work at a deeper level so changes won't affect
# original list
import copy            #importing copy module to use deepcopy function 
matrix_1=[['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix_copy_1= copy.deepcopy(matrix_1)
matrix_1.pop()
matrix_copy_1[0].insert(0,'z')
print(f"Original Matrix: {matrix_1}")
print(f"Copied matrix:    {matrix_copy_1}")
