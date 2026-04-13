#for i in range(0,100,1):
  #  if(i%2==0 and i%3==0):
      #  print(i)

#a=input("enter any name")
#reverse= ""
#for x in a:
   # reverse = x + reverse
#print (reverse)

#b=reversed(a)
#print("reversed name is=", b)
#for i in b :
 #   print(i, end =" ")
#a= [0,1,2,3,4,5]
#for x in a:
 #   if(x==3):
   #     break
  #  print(x)
for i in range(1,101):
    if i<2:
        print(i)
        continue
    for j in range(2,i):
        if i%j==0:
            print(i)
            break