matrix=[['a','b','c'],
        ['d','e','f'],
        ['g','h','i']]
matrix.append(['j','k','l'])
matrix.insert(0,[1,2,3])
# -IMP- adding item in a specific position in a matrix
matrix[1].append('m')
# adding item at the start in a matrix
matrix[0].insert(0,'z')
print(matrix)

# Remove items from list
letters=['a','b','c','d']
letters.clear()  
print(f"Empty List: {letters}")  # clearing all items in list
letters_1= ['a','b','c','d','e']
# removing last items in list
letters_1.remove('e')
print(f"List after removing 'd' that is end value: {letters_1}")
letters_2= ['a','b','c','d','e']
#removing items from a specific position
#pop: removes items from a specific position in a list and 
# also returns the deleted value
removed_value=letters_2.pop(0)
print(f"Removed Value: {removed_value}")    
print(f"List after poping 'a': {letters_2}")   

# Matrix
matrix_1=[['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
matrix_1.remove(['d','e','f'])
matrix_1.pop()  # removing last row by default

matrix_2=[['j','k','l'],
          ['m','n','o'],
          ['p','q','r']]
#removing 'l' by value from first row of matrix
matrix_2[0].remove('l')
#removing 'q' by position from last row of matrix
matrix_2[-1].pop(1)
# removing 'o' from second row of matrix
matrix_2[1].pop(2)
print(matrix_2)

# Update list
matrix_3=[['j','k','l'],
          ['m','n','o'],
          ['p','q','r']]
#updating value 'r' to 's' in third row
matrix_3[2][2]='s'
#updating value 'n' to 't' in second row
matrix_3[1][1]='t'
#updating value 'l' to 'u' in first row
matrix_3[0][2]='u'
print(matrix_3)







