#replacing , with . in prices
price='34,89'
print(price.replace(",", "."))
#replacing ' with / in phone numbers
phone= '345-765-896'
print(phone.replace('-','/'))
#replacing - with blank space
phone= '345-765-896'
print(phone.replace('-',''))
# replacing multiple values in data
price='$23,44.44@'
print(price.replace('$','').replace(',','').replace('@',''))
#challenge
#clean messy data
phone='+49 (176) 123-4567'
print(phone.replace('+','00').replace(' ','').replace('(','').replace(')','').replace('-',''))
#join strings(concatenate two strings)
First_Name='Zain'
Last_Name='UL Abideen'
Full_Name=First_Name + ' ' + Last_Name
print(Full_Name)
#concatenate file paths
Folder_Location='C:/Users/Zain/'
File_Name='reports.csv'
Full_Location=Folder_Location + File_Name
print(Full_Location)
#f-string/formatted strings
Name='Zain'
Age=25
is_student= True
print(f'My name is {Name}, and I am {25} years old, student status is {is_student}. ')
#split
data= '1011,Zain,USA,2000-01-01,M'
print(data.split(','))
data2= '2000-01-01,14:30'
print(data2.split(','))
data3='2000-01-01'
print(data3.split('-'))
#string repeatitions
print('he'*10)
print('='*10)
print('#'*10)
text='python'
#Extracting last two characters
print(text[4:6])
#Extracting last three characters
print(text[-3:])
date='2000-09-20'
#Extract year
print(date[0:4])
#Extract month
print(date[5:7])
#Extract day
print(date[-2:])
#extract all characters after year
print(date[5:])
