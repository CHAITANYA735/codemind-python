l=list(map(str,input().split()))
v=l[len(l)-1]
v=sorted(v)
if v[0].isupper:
    if v[0].lower()==v[1]:
        print(v[1])
    else:
        print(v[0])
else:
    print(v[0])