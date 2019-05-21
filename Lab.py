def check(s1, s2):
	for i in range(10):
		if s1[i]==0 and s2[i]==0:
			return False
	return True

l = [input() for i in range(int(input()))]
freq_list = [[0 for i in range(10)] for j in range(len(l))]
for i in range(len(l)):
	for j in range(len(l[i])):
		freq_list[i][int(l[i][j])] = 1
count = 0
for i in range(len(freq_list)):
	for j in range(i+1, len(freq_list)):
		if check(freq_list[i], freq_list[j])==True:
			count+=1
print(count)
		