# Write a program that keeps asking until the user agree:
# while True:
#     answer=input("Do you agree?(yes/no): ")
#     if answer=='yes':
#         break
# print("Thank You")

# Write a program that keeps asking until the user agree:
#1. Allow upto 3 attempts
#2. if the user types 'yes' print 'Glad we are on the same page'
#3. otherwise, print '3 strikes you are out'
i=0
while i<3:
    
    answer=input("Do you agree? (yes/no): ")
    if answer=='yes':
        print("Glad we are on the same page")
        break
    if answer=='no':
        i+=1
    if i==3:
        print(f"3 strikes, you are out !")
    



