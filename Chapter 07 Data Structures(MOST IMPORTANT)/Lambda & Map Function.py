# using lamba + map to perform transformations 
prices=['$12.50','$4.50','$9.80','$7.0']
# the issue with data is it has '$' value and stored as string data type
# Transformation: remove '$' and convert string to float
# applying transformation on one value to check accuracy
p='$12.50'
print(float(p.replace('$','')))
#applying lambda function and mapping transformation on complete list of prices
print(list(map(lambda p: float(p.replace('$','')),prices)))
 