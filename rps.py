#adapted from realpython.com

import random

score = 0

while True:

	
	pplay = input("Enter a choice R(rock) P(paper) S(scissors)")

	hands = ["R", "P", "S"]
	cplay = random.choice(hands)

	print(f"\nYou played {pplay}.\n")
	print(f"\nThe computer played {cplay}.\n")

	if pplay == cplay:
		print(f"A Tie!")
	elif pplay == "R":
		if cplay == "S":
			print("Rock beats Scissors!")
			score+=1
			print(f"\nYou've won {score} times.\n")
		else:
			print("Paper covers Rock!")
	if pplay == "P":
		if cplay == "R":
			print("Paper covers Rock!")
			score+=1
			print(f"\nYou've won {score} times.\n")
		else:
			print("Scissors cuts Paper!")
	if pplay == "S":
		if cplay == "P":
			print("Scissors cuts Paper!")
			score+=1
			print(f"\nYou've won {score} times.\n")
		else:
			print("Rock beats Scissors!")


	repeat = input("Play again? y/n?")
	if repeat != "y":
		break