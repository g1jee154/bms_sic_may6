input_number=int(input("enter number who's tables you need: "))

for i in range (1,21):
    print('{:1d} * {:2d} = {:03d}'.format(input_number,i,input_number*i))