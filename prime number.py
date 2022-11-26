# checking prime number or not 
n = int(input("Enter your number : "))
if n==1 or n==0 :
    print("0 and 1 is netheir a prime number nor composite number ")
else :
    for i in range(2, n):
        if n%i==0 :
            print(n ,"is not a prime number ") 
            break
        else : 
            print(n," is a prime number ")
            break 


# printing all natural number till n;
print("prime numbers till "+str(n) + " are: " )
if n<=2 :
     print(1)
else :
    for i in range(2,n):
        if i>2 :
            for j in range(2,i):
                if(i % j== 0):
                    break
        else :
            print(i,end=" ")


# printing first n prime numbers 
print ("\nFirst "+ str(n) +" prime numbers are : ")
count =0
value =1
res = []
output = []
while count <n :
    if value >2 :
        for i in range(2,n):
            if value % i == 0:
                break
        else :  
            res.append(value)
            count+=1
    value +=1

for j in range(0 , len(res)):
    if res[j] not in output :
        output.append(res[j])
print(str(output))