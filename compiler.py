try:
    N=int(input())
    for _ in range(N):
        s=input()
        one=0
        two=0
        ans=0
        for i in s:
            if i=='<':
                one+=1
            else:
                one-=1
                two+=1
                if one==0:
                    ans+=two*2
                    two=0
                elif one<0:
                    break
        print(ans)
except:
    pass