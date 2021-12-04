
age=int(input("enter thr age="))
sex=input("enter the sex:y or n")
if sex=="f":
    print("she can work only in urban areas")
elif age>=20 and age<=40:
    if sex=="m":
        print("he may work in anywhere")
elif age>=40 and age<=60:
    if sex=="m":
        print("he will work in urban areas only")
else:
    print("error")