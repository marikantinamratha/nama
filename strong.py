num=int(input("enter a number: "))
temp=num
sum=0
while temp>0:
    digit = temp%10
    f=1
    i=1
    while i<=digit:
        f=f*i
        i=i+1
    sum=sum+f
    temp = temp//10
if sum==num:
    print('strong')
else:
    print('not strong')
    
