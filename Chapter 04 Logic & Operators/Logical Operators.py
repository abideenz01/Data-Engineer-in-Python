#and | or
#check if the system is under pressure 
cpu_usage= 70
memory_usage=95
#if both usage is greater than 90 then it is critical
print('Is system critical?',cpu_usage >=90 or memory_usage>=90)
#checking user email credentials before login 
Email='aaa@gmail.com'
Password=123456
#check if user both credentials are correct
print('Details are correct?', Email=='aaa@gmail.com' and Password==123456)
#NOT Operator
print(not 3>2)
print(not 0)
name=''
print(not '')
print(not bool(''))
#AND has higher priority than OR
print(5==5 or 6<5 and 6>9)
#use parenthesis () to control the flow of execution and to 
#make sure OR has the higher priority 
print((5==5 or 6<5) and 9>6)
#task: allow access only if the user is logged in or they are
#guest but they must not be banned 

is_logged_in= False
is_guest= False
is_banned= True
print((is_logged_in or is_guest) and not is_banned)
#check if domain is not banned
domain='@spam.com'
banned_domain=['@spam.com','@blacklist.com','@bot.com']
print(domain not in banned_domain )
#Python Challenge 
#1. Check if a user name is not empty and the age is greater than or equal to 18.
user_name='Zain'
age=10
print(user_name!='' and age >18 or age==18)
#2. check if the password is at least 8 characters long and does not conatins spaces.
password='Zain'
print(len(password)==8 and password!=' ')
#3. check if a user name is not empty, contains "@" and ends with .com.
user_name='abideen@gmail.com'
print(user_name!= "" and '@' in user_name and user_name.endswith('.com'))
#4. check if a username is string, is not None,and is longer than 5 characters.
user_name='Zainul'
print(isinstance(user_name,str) and user_name is not None and len(user_name)>5)
#5. check if a username is either an admin or moderator, and either 
# they are not banned or they've verified their email.
is_admin=False
is_moderator=False
is_banned=True
is_email_verified=True
print((is_admin or is_moderator) and (not is_banned or is_email_verified))