# Nested Loop: Real World Application:
# Generate csv reports based on years,months and days
Years=['2026','2025','2024']
Months=['jan','Feb','March']
Days= range(1,32)
for Year in Years:
    for Month in Months:
        for Day in Days:
            print(f"Report-{Year}-{Month}-{Day}.csv")

# Digging through Hierarchy is the most powerful process executes
# using Nested Loops
# Hierarchy: tables,columns and rows
# SELECT COUNT(*) FROM CUSTOMERS WHERE ID IS NULL
Tables=['customers','products','prices','orders']
Columns=['id','create_date']
for t in Tables:
    for c in Columns:
        print(f"SELECT COUNT(*) FROM {t} WHERE {c} IS NULL")
