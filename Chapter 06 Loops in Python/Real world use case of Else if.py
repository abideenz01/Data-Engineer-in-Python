#check if list of names has garbage values
Names=['Zain','Adam','Aden','n/a']
Bad_Data=['',' ','n/a','NULL']
for name in Names:
    if name in Bad_Data:
        print(f"Bad data detected")
        break
else:
    print(f"Data is Validated: No garbage value detected")
# Check if all files are CSV files
Files=['marketing.csv','hr.csv','accounts.csv','data.pdf','manager.txt']
for file in Files:
    if not file.endswith('.csv'):
        print(f"{file} is not csv")
        break
else:
    print(f"{file} is csv")