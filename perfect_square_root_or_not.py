n=int(input())
for i in range(1,int(n**0.5)+1):
    if i*i==n:
        print('True')
        break
else:
    print('False')