"""
higher lower consolegame
"""

from pyfiglet import Figlet
import csv
import time


f = Figlet(font="slant")
s = Figlet(font="big")

print(f.renderText("Welcome to \nHIGHER LOWER"))

def prepare_data():
	"""
	initializes a dictionary with
	country (key) : country data (value)
	for better accessibility later

	Args:
		None
	
	Returns:
		dict: the dataset
	"""

	dataset = list()

	with open("data/stats.csv", mode="r") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			dataset.append(row)
	return dataset


def shuffle_data(dataset:list):
	"""
	shuffles the dataset based on the current time
	(for studying purposes, instead of using random)

	Args:
		dict: the unshuffled dataset
	
	Returns:
		dict: the shuffled dataset
	"""
	# assign a seed to every country
	for i in range(len(dataset)):
		time.sleep(0.003)
		dataset[i]["seed"] = time.time_ns() % 122
	
	# sort by the assigned seed	
	shuffle_data = sorted(dataset, key=lambda country: country["seed"])
	return shuffle_data

		

def game_loop(dataset:list):
	"""
	higherlower game loop

	Args:
		dataset
	
	Returns:
		None
	"""


	running = True

	while running:
		dataset = shuffle_data(dataset)

		left_country = dataset[0]
		right_country = dataset[1]

		print("Which countries population is greater?")
		versus = f"{left_country["Country"]} VS {right_country["Country"]}"
		print(s.renderText(versus))

		left_count = left_country["Population 2024"]
		right_count = right_country["Population 2024"]

		if int(left_count) > int(right_count):
			winner = "left"
		else:
			winner = "right"


		invalid_choice = True
		
		while invalid_choice:
			choice = input("Your Choice (Enter 1 or 2): ")
			match choice:
				case "1":
					invalid_choice = False
				case "2":
					invalid_choice = False
				case _:
					print("Invalid choice (only 1 or 2)")
		
		match (winner, choice):
			case ("left", "1"):
				print("THATS CORRECT!")
			case ("right", "2"):
				print("THATS CORRECT!")
			case _:
				print("OH NO SO WRONG!")
		


print(game_loop(prepare_data()))
