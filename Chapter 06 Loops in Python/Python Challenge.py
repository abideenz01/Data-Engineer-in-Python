# check whether any file appears more than once
# Print 'duplicate found' if a duplicate exists
# Otherwise print "All files are unique"
count=0
File_List=['report.csv','data.xlsx','summary.docx','report.csv','data.csv',]
for file in File_List:
    if file.count('report.csv'):
        count=count+1
        if count>1:
         print(f"{file}: Count:{count} | duplicate found")
         break
else: 
    print(f"All files are unique")