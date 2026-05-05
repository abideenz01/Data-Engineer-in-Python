# Parameter & Argument: Data input
# Return Value: Data output
# Function to clean and change name to lowercase
def clean_text(name):
    print(name.strip().lower())
clean_text("   ZaIn")

# Local and Global variables:
# transform only when case_transform='lower'
case_transform='n/a'
def cleaned_text(name):
    cleaned=name.strip() # local variable
    if case_transform=='lower':
        cleaned=cleaned.lower()
    print(cleaned)
cleaned_text("MARIA")






