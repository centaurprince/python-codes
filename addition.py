# to print sum of non duplicate numbers 

sum1 = sum2 = 0 
num1 = int(input("enter your number1 : "))
num2 = int(input("Enter your number2 : "))
num3 = int(input("enter your number3 : " ))

sum1 = num1 +num2 +num3

if num1 == num2 :
    if num2 != num3 :
        sum2 =sum+ num3

else :
    if num2==num3 :
        sum2 += num1
    else:
        sum2+=num1+num2+num3

print("numbers are ", num1 ,num2 , num3 )
print("sum of all numbers are : ",sum1)
print("sum of non duplicate numbers is ",sum2)   