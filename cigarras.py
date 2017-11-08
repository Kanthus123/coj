def mdc (a, b):
	i = 1
	ret = 1
	while (i <= a and i <= b):
		if (a % i == 0) and (b % i == 0):
			ret = i
		i += 1

	return ret

def mmc (a, b):
	return a / mdc (a, b) * b

s = raw_input ()
n,l = map(int, s.split())
s = raw_input ()
vet = map(int, s.split())

a = vet[0]
for i in vet[1:]:
	a = mmc (a, i)

#print a
b = l / a
#print b


c = mmc (a, b)
#print c

d = l / c

print b * d

