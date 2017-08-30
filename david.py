s = raw_input ()

soma = 0
for i in s:
	if i in ['a', 'e', 'i', 'o', 'u']:
		continue

	soma += ord(i) - ord('a') + 1
print soma
