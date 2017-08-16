def vencperd (p1,m1,p2,m2):
	if (dict[m1+m2] == 1):
		return [int(p1), int(p2)]
	else:
		return [int(p2), int(p1)]

dict = {
'paperrock':1,
'paperscissors':0,
'rockpaper':0,
'rockscissors':1,
'scissorspaper':1,
'scissorsrock':0,
}
while (True):
	s = raw_input ()
	vet = s.split()

	n = int(vet[0])

	if n == 0:
		break

	k = int(vet[1])

	vit = [0]*n
	der = [0]*n

#	print vit

	for  i in range(k):
		s = raw_input ()
		p1,m1,p2,m2 = s.split()

		if (m1 == m2):
			continue

		v,p = vencperd (p1,m1,p2,m2)

#		print m1, m2, p1, "venceu"

		vit[v-1] += 1
		der[p-1] += 1

	for  i in range(n):
		if (vit[i] + der[i] == 0):
			print "-"
		else:
			print "%.3f" % (vit[i]/float(vit[i]+der[i]))

	print ""
