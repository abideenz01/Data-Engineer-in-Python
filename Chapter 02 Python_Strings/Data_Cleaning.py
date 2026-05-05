#clean whitespaces
text='Data Engineering'
print(text.strip()) # strip() method to remove spaces from both ends
text='###Data Engineering###'
print(text.strip('#'))#passing arguments to remove specific value
#data cleaning real world example
text='Data Engineering'
print(len(text))
print(len(text.strip()))
No_of_Spaces=(len(text)-len(text.strip()))
Is_data_clean=(len(text)==len(text.strip()))
print('No of spaces:', No_of_Spaces)
print('Is data clean?',Is_data_clean)
#case conversions
text='python PROGRAMMING'
print(text.lower())
print(text.upper())
#USE CASE: clean data for matching
data='Email '.lower().strip()
text=' email'.lower().strip()
print(data==text)
#Challenge: Messy data '968-Maria,( Data Engineer );; 27y  '
#Turns above messy data into:
#name: maria | role: data engineer | age: 27 
messy_data='968-Maria,( Data Engineer );; 27y  '
clean_data= messy_data.replace('968','name: ').replace(',',' | ').replace('-','').replace('(','role: ').replace(')',' ').replace(';;','| age:').replace('y','').lower()
print(clean_data)
#dynamically searching using @ operator
Email='abideenz095@gmail.com'
print('@' in Email)
Data='https://api.sellingsphere.com'
print('/api' in Data)
#dynamically slicing strings usin find() function
# find() function extracts index of a specific character in string
phone1='+92-300-1234567' 
phone2='92-300-1234567'
phone3='0092-300-1234567'
# we have to slice phone number without country code
# dynamically slicing phone number 
print(phone1[(phone1.find('-')+1):])
print(phone2[(phone2.find('-')+1):])
print(phone3[(phone3.find('-')+1):])
#Validating 
#check if the string conatains only letters
country="USA"
print(country.isalpha())
#check if the string contains only digits
phone='03006543456'
print(phone.isnumeric())
number='319'
print(number.isnumeric())


