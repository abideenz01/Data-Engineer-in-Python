# Rules of unpacking list
#1. number of variables must match number of values in elements
#2. order of variables must match order of values in elements
#3 *Asterick collects leftovers, it is ok if there are less variables while using *Asterick
#4. Unpacking can be used to unpack list,tuples,strings

person_details=['Zain','32','Data Engineer','Italy']
# order of variables and list elements must be same
name, age, role, country = person_details
print(name)
print(age)
print(role)
print(country)

# Rest Controller *Asterick
person_details=['Zain','32','Rome','Italy','Data Engineer']
# order of variables and list elements must be same
# *Asterick combines unnecessary variables in a single variable
# only one *Asterick is allowed in unpacking 
# we only need name and role
name, *other_details, role = person_details
print(name)
print(other_details)
print(role)
# now we only need name 
person_details=['Zain','32','Rome','Italy','Data Engineer']
name, *other_details = person_details
print(name)
print(other_details)

#Skipping values underscore using *Asterick and underscore " _ "
person_details=['Zain','32','Rome','Italy','Data Engineer']
name, *_, role = person_details
print(name)
print(role)




