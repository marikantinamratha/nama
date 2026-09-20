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
#this program is used to check whether the given number is strong or not. A strong number is a number in which the sum of the factorial of digits is equal to the original number. For example, 145 is a strong number because 1! + 4! + 5! = 145.