# TASK:
# clean an email and split it into username and domain
def clean_and_split(email):
    cln_email=email.strip().lower()
    username,domain=cln_email.split("@")
    return {"username": username,
            "domain": domain}
print(clean_and_split("   ZAIN@gmail.com   "))

