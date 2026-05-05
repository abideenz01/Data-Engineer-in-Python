#Validate the Quality and Correctness of Passwords
# -Must not be empty
# -Must be at least 8 charcaters
# -Must include at least 1 uppercase
# -Must include at least 1 lowercase
# -Must not be same as email
# -Must not contain any spaces
# -Must start and end with a letter or digit
Password='SaJUITYE'
Email='SaJdfre'
if Password=='':
    print('Password cannot be empty')
elif len(Password)<8:
    print('Password is too short')
elif Password.isupper():
    print('Must contain at least 1 lowercase letter')
elif Password.islower():
    print('Must contain at least 1 uppercase letter')
elif Password==Email:
    print('password must not be same as Email')
elif Password.find(''):
    print('Spaces betweeen password is not allowed')
elif not(Password[0].isalnum() and Password[0].isalnum()):
    print('Password must start and end with letter or digit')
else:
    print('Password is Valid')