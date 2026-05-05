# Creating empty dictionary for we don't know values yet
user=dict.fromkeys(["id","name","age","country"],None)
print(user)
#updating values once values are available
user["id"]=1
user["name"]='Zain'
user["age"]=20
user["country"]='Brazil'
print(user)