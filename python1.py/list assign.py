#program1
a=int(input("enter first numbers"))
b=int(input("enter second number"))
c=int(input("enter third number"))
print("value of a=",a)
print("value of b=",b)
print("value of c=",c)
d=[a,b,c]
print(d)
#program 2
a=[]
for i in range(1,6):
    a.append(i)
print(a)
#program3
a=[1,1,3,2,5,5,6,3]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


#program4
a="hello world"
count=0
for i in a:
    if i in "aeiou":
        count+=1
print("vowels in string",count)

#program5
a=[1,2,3,4,5]
b=reversed(a)
print("reversed list is=", b)
for i in b :
    print(i, end =" ")
   # or
a=[1,2,3,4,5]
print(a[::-1])



