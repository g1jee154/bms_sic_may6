l1 = [1,4,8,5,2,2]
l2 = [2,5]
ml = []

for i in range(len(l1)):
    c = l1.count(l1[i]) - l2.count(l1[i])
    if l1[i] not in l2:
            ml.append(l1[i])
    else:
        ml.append(l1[i])
        if l1.count(l1[i]) >= l2.count(l1[i]):
            for i in range(abs(c)):
                l2.append(l1[i])
        elif l1.count(l1[i]) <= l2.count(l1[i]):
            for i in range(abs(c)):
                l1.append(l1[i])
        

for i in range(len(l2)):
    if l2[i] not in l1:
        ml.append(l2[i])
    else:
        ml.append(l2[i])
        if l2.count(l2[i]) >= l1.count(l2[i]):
            for i in range(abs(c)):
                l1.append(l2[i])
        elif l2.count(l2[i]) <= l1.count(l2[i]):
            for i in range(abs(c)):
                l2.append(l2[i])

print("The missing numbers are:\n",ml)