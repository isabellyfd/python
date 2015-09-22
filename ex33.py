i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i += 1
	print "Numbers now:", numbers
	print "At the botton i is %d" % i

print "the numbers:"

for num in numbers:
	print num
