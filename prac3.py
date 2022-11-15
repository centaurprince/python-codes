# menue deiven code for circle 
r = float(input("Enter radius of circle : "))
print("1 . calculate area of sector ")
print('2. claculate length of arc  ')
print("3. area of circle ")
print("4. circumference of circle ")
ch = int(input("Enter your choice "))

if ch==1 :
    t= int(input('Enter angle at center : '))
    sector= (t/360)*3.14*r*r
    print("area of sector is ",sector)
elif ch ==2 :
    t= int(input('Enter angle at center : '))
    arc = (t/360)*2*3.14*r
    print("length of arc is : ",arc)
elif ch==3 :
    area = 3.14*r*r
    print("area of circle is :", area)
else :
    c = 2*3.14*r
    print("circumference of circle is : ",c)