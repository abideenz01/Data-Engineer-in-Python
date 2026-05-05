#Method to add value in set
# Adds any iterable: List,Set,Tuple,Dictionary
my_set={20, 30, 40}
my_set.update({1,2})
my_set.update([3,4,5])
my_set.update((6,7,8))
my_set.update({'a':9,'b':10})
print(my_set)

#Method to remove value in set
my_set_1={20, 30, 40}
my_set_1.discard(40)
print(my_set_1)

