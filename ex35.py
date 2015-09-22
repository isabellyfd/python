from sys import exit 

def gold_room():
	print "this room is full of gold. how much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number")

	if how_much < 50:
		print "nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("you greedy bastard!")


def bear_room():
	print "there is a beear here"
	print "the bear has a bunch oh honey"
	print "the fat bear is in front of another door"
	print "how are you goin to move the bear?"

	bear_moved = false

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("the bear looks at you than slaps your face off")
		elif choice == "taunt bear" and not bear_moved:
			print "the bear has moved from the door. you can go throught it"
			bear_moved = True
		
