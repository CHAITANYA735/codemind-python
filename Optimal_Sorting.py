t=int(input())
while(t):
    n=int(input())
    k=list(map(int,input().split()))
    l=sorted(k)
    if(l==k):
        print(0)
    else:
        print(l[-1]-l[0])
    t-=1 