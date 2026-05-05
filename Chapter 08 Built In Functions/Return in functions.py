def user_name(name):
    lo_name=name.strip().lower()
    up_name=name.strip().upper()
    return lo_name,up_name
lowercase,uppercase=user_name("Mo")
print(lowercase)
print(uppercase)
