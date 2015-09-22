from sys import argv

script, filename =argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"


print "Now I'm going to ask you for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

w = '\n'
target.write(line1)
target.write(w)
target.write(line2)
target.write(w)
target.write(line3)
target.write(w)

print "And finilly, we close it"
target.close()