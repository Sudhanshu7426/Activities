sp=int(input())
a=int(input())
b=int(input())
if sp==1:
    print(a+b)
elif sp==2:
    print(a-b)
elif sp==3:
    print(a*b)
elif sp==4:
    print(a/b)
elif sp==5:
    print(a%b)
elif sp==6:
    print(a//b)
elif sp==7:
    print(a**b)
else:
    print('Invalid Input')
