t = int(raw_input ())

for i in range (t):

	dict = {
	'B':0,
	'R':0,
	'O':0,
	'K':0,
	'E':0,
	'N':0,
	}

	s = raw_input ()

	for c in s:
		if c in dict:
			dict[c] = dict[c] + 1

	if len (set (dict.values()))  == 1:
		print "No Secure"
	else:
		print "Secure"

		
