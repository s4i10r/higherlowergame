"""
higher lower consolegame
"""

from pyfiglet import Figlet
import csv
import time


f = Figlet(font="slant")

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
	for country in dataset:
		time.sleep(0.003)
		dataset[country]["seed"] = time.time_ns() % len(dataset)
	
	# sort by the assigned seed
	shuffle_data = {key: value for key, value in sorted(dataset.items(),
					key=lambda item: item[1]["seed"])}
	
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

	left_country = dataset[0]
	right_country = dataset[1]

	running = True

	while running:
		print(left_country["Country"], "or", right_country["Country"])
		running = False


print(game_loop(prepare_data()))