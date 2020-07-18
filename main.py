import random, copy
import os
from PIL import Image

# GLOBAL CONFIG
NUM_DRAW = 4			# number of draw
NUM_ROUNDS = 10			# number of simulation rounds

##
def convert_to_list(file_path, mode):
	if mode == 'use-dat':
		with open(file_path, 'r') as f:
			card_list = []

			for line in f:
				if not line[0].isalpha():
					continue

				card_number_pair = line.strip().split(',')

				for _ in range(int(card_number_pair[1])):
					card_list.append(card_number_pair[0])
	else:
		card_list = os.listdir(file_path)

	return card_list

def show_hands(path, hand_buffer):
	flatten = lambda l: [item for sublist in l for item in sublist] # function to flatten hand_buffer

	# a list which contains the Image objects
	hand_buffer_img = [[Image.open(path + img_name) for img_name in hand] for hand in hand_buffer]

	min_width = min([img.size[0] for img in flatten(hand_buffer_img)])
	min_height = min([img.size[1] for img in flatten(hand_buffer_img)])

	hand_buffer_img = [[img.resize((min_width, min_height)) for img in hand] for hand in hand_buffer_img]

	x_gap = 10
	y_gap = 20
	total_width = min_width * NUM_DRAW + x_gap * (NUM_DRAW + 1)
	total_height = min_height * NUM_ROUNDS + y_gap * (NUM_ROUNDS + 1)
	new_im = Image.new('RGB', (total_width, total_height), color=(255, 255, 255))

	x_offset = x_gap
	y_offset = y_gap
	for hand in hand_buffer_img:
		for card in hand:
			new_im.paste(card, (x_offset, y_offset))
			x_offset += min_width + x_gap

		y_offset += min_height + y_gap
		x_offset = x_gap

	new_im.show()

if __name__ == '__main__':
	import sys
	mode = 'use-img' # use image folder as default
	path = './deck/' # default deck folder
	try:
		if sys.argv[1][:2] == '--':
			if sys.argv[1] == '--use-dat':
				mode = 'use-dat'
				path = sys.argv[2]
		else:
			path = sys.argv[1]
	except IndexError:
		pass

	card_list = convert_to_list(path, mode)
	print('Number of cards in deck:', len(card_list))

	hand_buffer = []
	for _ in range(NUM_ROUNDS):
		hand = []
		cl_copy = copy.copy(card_list)
		for _ in range(NUM_DRAW):
			chosen = random.choice(cl_copy)
			hand.append(chosen)
			cl_copy.remove(chosen)

		hand_buffer.append(hand)

	if mode == 'use-dat':
		for hand in hand_buffer:
			print(hand, '\n')
	else:
		show_hands(path, hand_buffer)