Score=49
project_submitted= True
if Score>=90 and project_submitted:
    print('Garde: A+')
elif Score>=90:
    print('Garde:A')
elif Score>=80:
    print('B Grade')
elif Score>=70:
    print('C Grade')
elif Score>=60 or project_submitted:
    print('D Grade')
else:
    print('F')
