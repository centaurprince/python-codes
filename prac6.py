sum=0 
i = int(input("Enter your start point : "))
j = int(input("Enter your ending point : "))
for n in range(i,j):
    sum+=n
    print("sum of natural number <=",n,"is",sum)