n=int(input())
l=0
while n>0:
    d=n%10
    if l<d:
        l=d
    n=n//10
print(l)
    