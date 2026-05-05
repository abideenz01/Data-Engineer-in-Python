letters=['x','z','y']
# sorting in ascending order
letters.sort()
# sorting in descending order
letters.sort(reverse=True)
print(letters)

#soring complete matrix
letters_1=[['g','h','i'],
           ['d','e','f'],
           ['a','b','c']]
letters_1.sort()
letters_1.sort(reverse=True)
print(letters_1)

#sorting complete matrix with same first value
letters_2=[['g','h','i'],
           ['a','e','f'],
           ['a','b','c']]
letters_2.sort()
letters_1.sort(reverse=True)
print(letters_2)

#sorting elements in a specific row of matrix
letters_3=[['i','g','h'],
           ['c','a','b'],
           ['f','d','e']]
letters_3[0].sort()
letters_3[1].sort()
letters_3[2].sort()
#letters_1.sort(reverse=True)
print(letters_3)



