t=int(input())
a=list(map(int,input().split()))
c=0
c1=0
c2=0
c3=0
for i in range(len(a)):
    if(a[i]%4==0):
        c+=1
    elif(a[i]%4==1):
        c1+=1
    elif(a[i]%4==2):
        c2+=1
    else:
        c3+=1
if(c%2==0 and c1%2==0 and c2%2==0 and c3%2==0):
    print('X')
else:
    print('Y')
    