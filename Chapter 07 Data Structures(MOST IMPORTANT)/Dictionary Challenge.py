user={"id":1,
      "name":'John',
      "Age": 30,
      "city":'Berlin'
      }
# Create New Dictionary
# keep only pairs with string values
# convert value to Uppercase
# Elegant and short solution

#Dictionary Comprehension Syntax:
#dict_1={ key: value expression (transformation)
#         for key,value in (Looping)
#         filtering results using if or multiple ifs (filtering) }




user_2= {key:value.upper()
         for key,value in user.items()
         if (isinstance(value,str)) # filter out only string values
         
}

print(user_2)

         
        
        
       





