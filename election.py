t = int(raw_input())

i = 0

for  i in range(t):
	s = raw_input ()
	n,m = s.split()
	n = int(n)
	m = int (m)
	total = [0]*n
	for j in range (m):
		s = raw_input ()
		votos = map (int, s.split())
		k = 0
		while k < n:
			total[k]+=votos[k]
			k += 1
	print total.index(max(total))+1
