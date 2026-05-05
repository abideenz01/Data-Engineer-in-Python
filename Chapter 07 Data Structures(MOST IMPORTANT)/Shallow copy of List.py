# Shallow copy only works at the parent level 
# at the child level only deep copy works
letters_List=['a','b','c','d','e']
copy_letters_List=letters_List.copy()
letters_List.insert(1,'b')
copy_letters_List.pop(1)
print(f"Original List: {letters_List}")
print(f"Copied List: {copy_letters_List}")
