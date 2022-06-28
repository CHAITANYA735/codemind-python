n=int(input())
I=[]
for i in range(0,n):
    I.append(int(input()))
v=int(input())
c=0
for i in I:
    if v>=i:
        c+=1
    else:
        c+=2
print(c)        