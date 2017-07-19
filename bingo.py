t = int(raw_input())

for  i in range(t):
	cartela = []
	linhas=[5]*5
	colunas=[5]*5
	diagonal = 4
	cdiagonal = 4
	linhas[2]=4
	colunas[2]=4
	n = 75
	sorteados = 0
	fim = False
	
	for  j in range(5):
		s = raw_input ()
		cartela.append(map(int, s.split()))

	cartela[2].append(cartela[2][-1])
	cartela[2][-2] = cartela[2][-3]
	cartela[2][2] = 0

	while (n > 0):
		s = raw_input ()
		v = map(int, s.split())
		n -= len(v)
		
		if fim:
			continue

		for k in v:
			x = 0
			sorteados += 1
			for l in cartela:
				if (k in l):
					linhas[x] -= 1
					colunas[l.index(k)] -= 1
					if x == l.index(k):
						diagonal -= 1
					if x == 4 - l.index(k):
						cdiagonal -= 1
				x += 1
			
			if 0 in linhas or 0 in colunas or diagonal == 0 or cdiagonal == 0:
				fim = True
				break
	
	print "BINGO after %d numbers announced" % sorteados
