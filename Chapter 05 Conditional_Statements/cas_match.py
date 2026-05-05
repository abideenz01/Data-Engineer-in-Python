#Task 
#Convert full name of countries into 2 letters abbreviations
Country= "BRA"
match Country:
    case "United States" | "USA":
        print('US')
    case "United kingdom" | "UK":
        print('UK')
    case "Pakistan" | "PAK":
        print("PK")
    case "Brazil" | "BRA":
        print("BR")
    case _:
        print('Unknown')

