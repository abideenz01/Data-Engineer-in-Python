# Print the 7 times table from 1 to 10 using a for loop
count=0
for table in range(1,11):
    seven_table= 7*table
    count=count+1
    print(f"7 * {count}  = {seven_table}")
# Challenge: 02
# print a left-aligned pyramid of stars with 6 rows using a for loop

for stars_count in range(1,7):
    stars_count='*'*stars_count
    print(f"{stars_count}")

