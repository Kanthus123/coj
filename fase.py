n = int (raw_input ())
k = int (raw_input ())

cont = 0
vet = [0]*n

for i in range (n):
	vet[i] = int (raw_input ())

vet.sort (reverse=True)
print vet

for i in range (n):
	if (k > 0):
		k -= 1
		ult = vet[i]
	else:
		if ult != vet[i]:
			break
	cont += 1

print cont
		
		
