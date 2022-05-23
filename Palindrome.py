n=int(input())
res=0
temp=n
while n>0:
    d=n%10
    res=res*10+d
    n=n//10
if res==temp:
    print(True)
else:
    print(False)