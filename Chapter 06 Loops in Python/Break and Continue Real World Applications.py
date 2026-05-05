# Task:01 Loop through a list of days and print only the working days,
# skipping the weekends
Days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
Weekend=['Saturday','Sunday']
for day in Days:
    if day in Weekend:
        print(f"Skipping Weekend")
        continue
    print(f"Working Day: {day}")
# Task:02 Scan emails to block unsafe data from entering the system
Emails=['@gmail.com','@hotmail.com','@outlook.com','DROP TABLE USERS;']
for Email in Emails:
    if ';' in Email: # High Critical Risk- preventing hacker attack
        print(f"SQL Injection: Hacker Attack")
        break
    print(f"Email is safe: {Email}")

