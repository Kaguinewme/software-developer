# num1=int(input("enter the first number\n"))
# num2=int(input("enter the second  number\n"))
# if num2>num1:
#     mn=num1
# else:
#     mn=num2
# for i in range(1,mn+1):
#     if num1%i==0 and num2%i==0:
#         hcf=1      
# print("\nHCF (" + str(num1) + "," + str(num2) + ")=",hcf)


# print("enter two number",end="")
n=int(input("enter the number"))
n1=int(input("enter the number"))

if n>n1:
    hcf=n
else:
    hcf=n1
while True:
    if n%hcf==0 and n1%hcf==0:
       break 
    
    else:
        hcf=hcf-1
print("\nHCF (" + str(n) + "," + str(n1) + ")=",hcf)


    
