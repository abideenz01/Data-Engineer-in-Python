# For loop in a list of strings
items=['Banana','Apple','Orange','Gauav','Blueberries','Avocado']
for item in items:
    print(f"Fruit:{item}")
# For loop in a single string 
Name="ZainULAbideen"
for letters in Name:
    print(f"Alphabets in Name:{letters}")
# Range function in For Loop
# range(start,end,step)
for numbers in range(6):
    print(f"Numbers:{numbers}")
# Range with start,end(end is not included) and step
# Generate even numbers 
for odd_numbers in range(1,11,2):
    print(f"Odd Numbers:{odd_numbers}") 
# Generate even numbers 
for even_numbers in range(2,11,2):
    print(f"Even Numbers:{even_numbers}") 
# Real World Application
# 1.Data Aggregation
Scores=[20,90,70,60,45,32,65]
Total=0
for Score in Scores:
    Total+=Score
    print(f"Current Total: {Total}")
print(f"Final Total: {Total}")

#2. Data Cleaning and Transformation
files=[' FINANCE.csv',' hr.csv ',' Marketing. TXT ']
# Issues in data:
#1. Inconsistent case letters
#2. Leading and Trailing spaces
#3. Spaces in text
#4. txt files are not required
for file in files:
    Clean_File= file.strip().lower().replace(' ','').replace('.txt','.csv')
    # order--> clean up the data by .stripe() then transform the data by .lower() and .replace() 
    print(f"Cleaned File: {Clean_File}")

