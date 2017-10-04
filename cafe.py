a1 = int(raw_input())
a2 = int(raw_input())
a3 = int(raw_input())

s1 = a2*2 + a3*4
s2 = a1*2 + a3*2
s3 = a1*4 + a2*2

if s1 < s2:
	if s1 < s3:
		print s1
	else:
		print s3
else:
	if s2 < s3:
		print s2
	else:
		print s3
		
