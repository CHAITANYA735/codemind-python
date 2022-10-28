n=int(input())
a=[]
for i in range(1,n):
    k=i*i
    a.append(k)
if n in a:
    print("True")
else:
    print("False")
