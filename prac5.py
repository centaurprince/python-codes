#Calculation of roots of quadratic equation
import math
print("for a quadratic equation , a*x**2 +b*x +c")
print("Enter coeficients below : ")
a = int (input("Enter a : "))
b = int (input("Enter b : "))
c = int (input("Enter c : ")) 

if a==0 :
    print("value of a" ,'should not be zero')
    print("\nAborting !!!!!!")
else :
    delta= b*b -4*a*c
    if delta >0 :
        root1 = (-b + math.sqrt(delta))/(2*a)
        root2= (-b - math.sqrt(delta))/(2*a)
        print("ROOTS ARE REAL AND EUNEQUAL")
        print("Roots are : ",root1 ,root2)
    elif delta == 0 :
        root1 = -b/2*a 
        root2 = -b/2*a
        print("ROOTS ARE REAL AND EQUAL")
        print("Roots are : ", root1, root2)
    else:
        print("roots of complex number is not possible ")