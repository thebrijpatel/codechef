try:
    N = int(input())
    for _ in range(N):
        g = int(input())
        for _ in range(g):
            i,n,q = map(int, input().split())
            if n%2==0:
                print(n//2)
                continue
            heads = 0
            tails = 0
            if q == 1:
                if i==1:
                    print(n//2)
                    continue
                else:
                    print(n - n//2)
            else:
                if i==1:
                    print(n - n//2)
                else:
                    print(n//2)
except:
    pass
