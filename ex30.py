people = 30
cars = 40
trucks = 15

if cars > people:
	print "we should take the cars"
elif cars < people:
	print "we should no take the cars"
else:
	print "we cant decide"

if trucks > cars:
	print "thats too many trucks"
elif trucks < cars:
	print "maybe we could take the trucks"
else:
	print "we still cant decide"

if people > trucks:
	print "Alright, lets just take the trucks"
else:
	print "Fine, lets stay home then"

