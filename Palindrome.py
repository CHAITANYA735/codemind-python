a=int(input())
rev=0
temp=a
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
if rev==temp:
    print('True')
else:
    print('False')