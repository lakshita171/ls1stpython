a=[20,40,50,34,23,45,20,20]
print(a)           #to print the list
print(len(a))      #to find the length of list
print(a.index(45)) #find index value from list value
print(a[2])        #find value according to index number
a.append(60)       #adds one element at the end
print(a)
a.insert(1,10)     #adds at specific index
print(a)
a.extend([6,7])    #to add multiple elements
print(a)
a.remove(45)       #to remove specific value
print(a)
a.pop(1)           #to remove by index
print(a)
a[0]=100           #updating elements
print(a)
print(a[2:5])
a.sort()            #ascending order
print(a)
a.reverse()          #reverse
print(a)
print(a.count(20))   #counts recurrence
a.clear              #to remove all elements of list
print(a)