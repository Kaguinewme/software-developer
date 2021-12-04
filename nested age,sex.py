
age=int(input("enter the age"))
sex=input("enter the sex:m or f")
days=int(input("enter the number of days"))
if age>=18 and age<30:
    if sex=="m":
        wage=days*700
        print(wage)
    else:
        wage=days*750
        print(wage)
elif age>=30 and age<=40:
    if sex=="f":
        wage=days*850
        print(wage)
else:
    wage=days*800
    print(wage