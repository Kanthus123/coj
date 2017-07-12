t = int(raw_input())

for  i in range(t):
	s = raw_input ()
	s = raw_input ()
	ng,nm = s.split()
	ng = int (ng)
	nm = int (nm)

	if (ng == 0 and nm == 0):
		print "uncertain"
		continue
	

	s = raw_input ()
	vg = s.split()
	s = raw_input ()
	vm = s.split()

	mvg = max(vg)
	mvm = max(vm)

	if mvg >= mvm:
		print "Godzilla"
	else:
		print "MechaGodzilla"

