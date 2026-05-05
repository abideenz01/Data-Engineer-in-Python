#positional and keyword Arguments
def cleaned_text(First_name,Last_name,country):
    cleaned_first_name=First_name.strip().lower()
    cleaned_last_name=Last_name.strip().lower()
    full_name= cleaned_first_name + " " + cleaned_last_name
    print(full_name,country)
# keyword Arguments
cleaned_text(First_name=" ZAIN  ", Last_name="ABIDEEN", country="DE")