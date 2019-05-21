n = int(input())
l = list(map(int, input().split()))
m = int(input())
s = 0
for i in range(n):
	s+=l[i]
	if m==s:
		print('m certificates earned at month', i+1)

