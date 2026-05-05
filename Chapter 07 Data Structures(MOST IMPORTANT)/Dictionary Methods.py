# Add:
user={'id':1,'Name':'Zain','Age':30,'Country':'Italy'}
user["City"]="Berlin"
print(user)

#Update:
# Update in dictionary performs two tasks:
#1. It update the key if it already exists
#2. If the key does not already exists, it adds new key value pair
user_1={'id':1,'Name':'Zain','Age':30,'Country':'Italy'}
user_1.update({"id":2}) # it updates the existing key
user_1.update({"City":"Sao Paulo","Height":'5 ft'}) # it adds new key, value pair
print(user_1)

#Remove:
user_2={'id':1,'Name':'Zain','Age':30,'Country':'Italy'}
country=user_2.popitem() # it removes last item in list
id=user_2.pop("id") #removing valid key,value pair
print(user_2.pop("City","Unknown")) # if key does not exists pass default value to avoid breaking code execution
print(id)
print(country)