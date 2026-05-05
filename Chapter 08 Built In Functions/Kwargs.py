#keyword arguments for different data types
def user_profile(**kwargs):
    print(kwargs)
user_profile(Name='Zain',
             Age=25,
             City='Barcelona',
             Country='Argentina')