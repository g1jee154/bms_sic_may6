boys = [1,2,3]
girls = [1,2,4]
l = boys + girls
l.sort()

check = False
for i in range(len(l)-2):
    if l[i] in boys and l[i+1] in girls:
        check = True
    elif l[i] in girls and l[i+1] in boys:
        check = True
    else:
        check = False
        break

if check == True:
    print("final arrangement:\n",l)
else:
    print("The given input height cannot be arranged:")