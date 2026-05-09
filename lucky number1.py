def lucky_digit(num):
    sum=0
    while num!=0 :
        rem = num%10
        num = num//10
        sum +=rem
        
        if sum>=10 and num==0:
            num=sum
            sum=0
    return sum      
num = int(input("enter lucky number: "))
print("lucky digit is:",lucky_digit(num))