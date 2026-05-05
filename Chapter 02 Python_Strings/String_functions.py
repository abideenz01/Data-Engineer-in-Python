#Types
name='Zain'
Age=25
print(type(name))
print(type(Age))
#concatenating strings by converting integer to string by function str()
print('My age is:' + str(Age)) 
#Maths
password='123456789'
if len(password)<8:
    print('password is too short')
else:
    print('password is strong')

# Detecting Quality issues in data
data="""
python is simple to learn.
python is powerful and scalable.
python is used in data engineering.
"""
print(data.count('python'))
print(data.count('$'))

