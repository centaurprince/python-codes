# finding multiple of any number from given number 

from math import remainder


print("Enter 5 numbers below...")
n1 = float(input("Enter number 1 : "))
n2 = float(input("Enter number 2 : "))
n3 = float(input("Enter number 3 : ")) 
n4 = float(input("Enter number 4 : "))
n5 = float(input("Enter number 5 : "))
divisor = float (input ("Enter Divisor number : "))
count= 0 
print("multiple of ",divisor," are :")
remainder= n1%divisor
if remainder==0 :
    print(n1 , sep=" ")
    count+=1
remainder= n2%divisor
if remainder==0 :
    print(n2 , sep=" ")
    count+=1
remainder= n3%divisor
if remainder==0 :
    print(n3 , sep=" ")
    count+=1
remainder= n4%divisor
if remainder==0 :
    print(n4 , sep=" ")
    count+=1
remainder= n5%divisor
if remainder==0 :
    print(n5, sep=" ")
    count+=1
print()
print(count, "multiple of ", divisor ,"found")