# Pass Statement: For now keep going and do nothing
# will handle empty value later
Names=['Zain','Sophia','','Nico']
for name in Names:
    if name=='':
        pass #to do: handle empty value
    print(f"Name:{name}")

# Handling empty value 
Names=['Zain','Sophia','','Nico']
for name in Names:
    if name=='':
        name=name.replace('','unknown')
    print(f"Name:{name}")
