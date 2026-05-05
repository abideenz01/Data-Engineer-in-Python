#List Comprehension
#Syntax: [
       #1. Data Transformation
       #2. Looping
       #3. Data Filtering
#]
# List Comprehension is used for:
#1. Data Transformations and Filteration
#2. Only Data Transformations
#3. Only Data Filteration

orders = [
    {"order_id": 1, "customer": "Alice", "amount": 250, "status": "completed"},
    {"order_id": 2, "customer": "Bob", "amount": 120, "status": "pending"},
    {"order_id": 3, "customer": "Charlie", "amount": 560, "status": "completed"},
    {"order_id": 4, "customer": "David", "amount": 80, "status": "cancelled"},
    {"order_id": 5, "customer": "Eva", "amount": 300, "status": "completed"},
    {"order_id": 6, "customer": "Frank", "amount": 150, "status": "pending"}
]

#Tasks:Tasks (Use ONLY List Comprehension)
# 1. Filter High-Value Completed Orders
# Extract order_ids where:
# status == "completed"
# amount > 200
# Expected output:
#[1, 3, 5]
high_value_orders=[
                  o
                  for o in orders
                  if o["status"]== "completed" and o["amount"]>200 
]
print(high_value_orders)
print("-------------------------------")

# 2. Apply Discount Transformation
# Create a new list where:
# Only completed orders are included
# Apply a 10% discount to their amount
# Output format: (order_id, discounted_amount)
# Expected output:
# [(1, 225.0), (3, 504.0), (5, 270.0)]

completed_orders=[ (p["order_id"],p["amount"]*0.9)
                   for p in orders
                   if p["status"]=="completed" 

]
print(f"{completed_orders}")
print("----------------------------")

# 3. Label Orders Based on Amount
# Create a list of strings:
# "HIGH" if amount >= 300
# "MEDIUM" if 150 <= amount < 300
# "LOW" if amount < 150
# Output example:
# ['MEDIUM', 'LOW', 'HIGH', 'LOW', 'HIGH', 'MEDIUM']
orders_label= [ 
               'HIGH' if l["amount"]>=300 
                else 'MEDIUM' if 150<=l["amount"]<300 
                else 'LOW'  
                for l in orders

]
print(orders_label)


# 4. Nested Condition Filtering
# Extract customer names where:
# Order is not cancelled
# Amount is between 100 and 400
# Expected output:
# ['Alice', 'Bob', 'Eva', 'Frank']
print("------------------------------")
customer_names=[ c["customer"]
                 for c in orders
                 if c["status"]!="cancelled"
                 if 100<c["amount"]<400
                                    
]
print(customer_names)

                 
                




