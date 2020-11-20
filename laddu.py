try:
	N=int(input())
	for _ in range(N):
		a,b=input().split()
		points=0
		for _ in range(int(a)):
			c=input().split()
			if c[0]=='CONTEST_WON':
				if int(c[1])<=20:
					points+=300+(20-int(c[1]))
				else:
					points+=300
			elif c[0]=='TOP_CONTRIBUTOR':
				points+=300
			elif c[0]=='BUG_FOUND':
				points+=int(c[1])
			else:
				points+=50
		if b == 'INDIAN':
			print(points//200)
		else:
			print(points//400)
except:
	pass