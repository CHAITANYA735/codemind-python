n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if(i%2==0):
        b.append(i)
for i in l:
    if(i%2==1):
        b.append(i)
print(*b)