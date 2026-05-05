# Continue real world application: 
# Skip the bad data like empty value instead of stopping whole loop
# Continue is more preferable than break coz it skips one iteration
Names=['Zain','Sophia','','Nico']
for name in Names:
    if name=='':
        print(f"Empty value is Skipped")
        continue
    print(f"Name:{name}")