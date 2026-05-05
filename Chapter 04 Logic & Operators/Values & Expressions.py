print(bool)
print(type(bool))
print(bool(123))
print(bool(""))
print(bool(' '))
print(bool(None))
print(bool('Hi'))
#Allows registartion
#if any field is filled 
Email=''
Phone='1234567'
Username=''
print(any([Email,Phone,Username]))
#Allows registartion
#if all fields are filled 
Email='1'
Phone='1234567'
Username='2'
print(all([Email,Phone,Username]))
#isinstance: check value and its data type
print(isinstance(123,int))
print(isinstance(True,str))
#check if string start with a specific letter
print('Hello'.endswith('o'))
print("Zain".endswith('n'))

