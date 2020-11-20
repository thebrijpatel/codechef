N=int(input())
for _ in range(N):
    e=input()
    a=0
    ans=0
    for i in e:
        if i == '<':
            a+=1
        else:
            a-=1
            ans=ans+1
            if ans<0:
                break
    print(ans)