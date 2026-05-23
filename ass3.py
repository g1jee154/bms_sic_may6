n = int(input("Enter number of shoes avilabel: "))
p = int(input("Enter number of shoes can be carried: "))
prize = []
sum = 0

for j in range(n):
    prize.append(int(input("enter prizes of shoes: ")))

for i in range(n):
    m = 0
    while(p != 0):   
        m = min(prize)
        prize.remove(m)
        if m <= 0:
            sum += m
        p -= 1

print(abs(sum))