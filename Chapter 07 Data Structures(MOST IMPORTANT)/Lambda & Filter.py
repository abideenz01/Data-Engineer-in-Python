# Lambda + Filter
prices=[120,30,300,80]
# Remove all prices lower than 100
print(list(filter(lambda p: p>=100,prices)))
print("--------------------------")
students=[['Zain',80],
          ['John',75],
          ['kiran',60]]
# keep only those students with score higher than 70
print(list(filter(lambda students: students[0:3][1]>70,students)))
print("------------------------------")
students_1=[['Maria',85],
            ['Zain',90],
            ['Max',60]]
# keep only students with name starting with 'M'
print(list(filter(lambda row: row[0].startswith('M'),students_1)))
