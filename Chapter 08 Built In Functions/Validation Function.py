#Task:01 Checks whether the password meets the minimum requirement of 8 charcaters
def ch_len_check(password):
    Char_length=len(password)
    return Char_length>=8
   
print("Is password valid :", ch_len_check("Zain"))

#Task 02:check whether an email has a vaild format
def valid_format(email):
    return '@' in email  and '.' in email
print("Email is valid:", valid_format("zain@gmail.com"))
