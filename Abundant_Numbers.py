a=int(input())
k=0
for i in range(1,a):
    if a%i==0:
        k=k+i
if k>a:
    print('True')
else:
    print('False')