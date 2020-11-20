try:
    N=int(input())
    for _ in range(N):
        res=0
        for _ in range(int(input())):
            s,p,v=map(int, input().split())
            temp=(p//(s+1))*v
            if temp>res:
                res=temp
        print(res)
except:
    pass