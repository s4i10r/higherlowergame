"""
higher lower consolegame
"""

from pyfiglet import Figlet
import csv
import time


f = Figlet(font="slant")

print(f.renderText("Welcome to \n HIGHER LOWER"))


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

	dataset = dict()

	with open("data/stats.csv", mode="r") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			dataset[row["Country"]] = row
	return dataset


def shuffle_data(dataset:dict):
	"""
	shuffles the dataset based on the current time
	(for studying purposes, instead of using random)

	Args:
		dict: the unshuffled dataset
	
	Returns:
		dict: the shuffled dataset
	"""
	# assign a seed to every country
	for key in dataset:
		time.sleep(0.003)
		dataset[key]["seed"] = time.time_ns() % len(dataset)
	
	# sort by the assigned seed
	shuffle_data = {key: value for key, value in sorted(dataset.items(),
													 key=lambda item: item[1]["seed"])}
	
	return shuffle_data


print(shuffle_data(prepare_data()))

		

def game_loop(dataset:dict):
	"""
	higherlower game loop

	Args:
		dataset
	
	Returns:
		None
	"""
	if len(dataset) > 1:
		pass
	else:
		return f.renderText("GAME \n OVER")
	
