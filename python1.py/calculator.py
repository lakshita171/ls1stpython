opt=input("enter the operation you want to perform (+, -, *, /): ")
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if opt=='+':
    print(a+b)
elif opt=='-':
    print(a-b)
elif opt=='*':
    print(a*b)
elif opt=='/':
    print(a/b)
elif opt=='//':
    print(a//b)
elif opt=='%':
    print(a%b)
elif opt=='**':
    print(a**b)