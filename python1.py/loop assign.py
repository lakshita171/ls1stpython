for i in range(0,100,1):
   if(i%2==0 and i%3==0):
       print(i)

a=input("enter any name")
reverse= ""
for x in a:
    reverse = x + reverse
print (reverse)

b=reversed(a)
print("reversed name is=", b)
for i in b :
    print(i, end =" ")