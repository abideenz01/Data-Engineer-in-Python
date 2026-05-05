# Runs a block of code only if the loop finishes naturally.
# That is loop completed without break
# Real usage of for-else:
# Else + Break
# check if even number exists
Numbers=[1,3,5,7,9]
for number in Numbers:
    if number%2==0:
        print(f"Even Number: {number}")
        break
else: 
    print(f"All numbers are odd")

