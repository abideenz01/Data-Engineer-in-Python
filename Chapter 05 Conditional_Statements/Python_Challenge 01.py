#Validate the quality and correctness of Email Values
#-Must not be empty
#-Must contain "." and "@"
#-Must contain exactly one "@" symbol
#-Must end with ".com", ".org" or ".net"
#-Must not be longer than 254 charcaters
#-Must start and end with a letter or digit

Email='abideenz01@gmail.com'

if Email=='':
    print("Email can not be empty")
elif '.' and '@' not in Email:
    print("Invalid Format")
elif Email.count('@')>1:
    print("Multiple @ are not allowed")
    Valid=False
elif not Email.endswith(('.com','.org','.net')):
    print("Invalid Domain")
elif len(Email)>254:
    print("Email too long")
elif not (Email[0].isalnum() and Email[-1].isalnum()) :
    print("Email must start or end with letter or digit")
else:
    print("Email is Valid")
