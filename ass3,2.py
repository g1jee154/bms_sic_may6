n = int(input("Enter number of shoes avilabel: "))
p = int(input("Enter number of shoes can be carried: "))
prize = []
sum = 0

for j in range(n):
    prize.append(int(input("enter prizes of shoes: ")))

prize.sort()

for i in range(p):
    if prize[i] <= 0:
        sum += prize[i]
print(abs(sum))
