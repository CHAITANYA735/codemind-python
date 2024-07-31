def fac(r):
    if r==1: return 1
    if r==0: return 1
    return r*fac(r-1)
n=int(input())
tem=n
s=0
while(n>0):
    r=n%10
    a=fac(r)
    s=s+a
    n=n//10
if(s==tem): print("The number",tem,"is a strong number")
else: print("The number",tem,"is not a strong number")
    
    