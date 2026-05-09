num = int(input("enter lucky number: "))

sum = 0
while num!=0 :
    rem = num%10
    num = num//10
    sum +=rem
    
    if sum>=10 and num==0:
        num=sum
        sum=0
print("lucky digit is:",sum)