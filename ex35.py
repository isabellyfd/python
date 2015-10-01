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

	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("the bear looks at you than slaps your face off")
		elif choice == "taunt bear" and not bear_moved:
			print "the bear has moved from the door. you can go throught it"
			bear_moved = True
		elif choice == "taunt bear"  and bear_moved:
			dead("The bear get pissed off and chews your leg off")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no ideia what that means"

def cthulhu_room():
	print "here you see the great evil Cthulhu"
	print "he, it, whatever stares at you and you go insane"
	print "do you flee for your life or eat your head?"

	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty!")
	else:
		cthulhu_room()

def dead (why):
	print why, "good job!"
	exit(0)


def start():
	print "You ar in a dark room"
	print "there is a door to your right and left"
	print "which one you take?"

	choice = raw_input("> ")
		
	if choice == "left":
		bear_room()
	elif choice ==  "right":
		cthulhu_room()
	else: dead("you stumble around the room until starve")


start()
