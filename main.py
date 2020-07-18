import random, copy
import os
from PIL import Image

##
def convert_to_list(path, mode):
	if mode == 'use-dat':
		with open(path, 'r') as f:
			card_list = []

			for line in f:
				if not line[0].isalpha():
					continue

				card_number_pair = line.strip().split(',')
				for _ in range(int(card_number_pair[1])):
					card_list.append(card_number_pair[0])
	else:
		card_list = os.listdir(path)

	return card_list

def show_hands(path, hand_buffer, num_draw, num_rounds):
	flatten = lambda l: [item for sublist in l for item in sublist] # function to flatten hand_buffer

	# a list which contains the Image objects
	hand_buffer_img = [[Image.open(path + img_name) for img_name in hand] for hand in hand_buffer]

	min_width = min([img.size[0] for img in flatten(hand_buffer_img)])
	min_height = min([img.size[1] for img in flatten(hand_buffer_img)])

	hand_buffer_img = [[img.resize((min_width, min_height)) for img in hand] for hand in hand_buffer_img]

	x_gap = 10
	y_gap = 20
	total_width = min_width * num_draw + x_gap * (num_draw + 1)
	total_height = min_height * num_rounds + y_gap * (num_rounds + 1)
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
	num_draw = 4     # default number of draw each round
	num_rounds = 10  # default number of rounds to simulate
	try:
		if sys.argv[1][:2] == '--':
			if sys.argv[1] == '--use-dat':
				mode = 'use-dat'
				path = sys.argv[2]
				num_draw = int(sys.argv[3])
				num_rounds = int(sys.argv[4])
			else:
				raise ValueError('Incorrect option. Use "--use-dat" if using .dat files.')
		else:
			path = sys.argv[1]
			num_draw = int(sys.argv[2])
			num_rounds = int(sys.argv[3])
			if path[-1] != '/':
				path += '/'
	except IndexError:
		pass # use default params if no args given

	card_list = convert_to_list(path, mode)
	print('Number of cards in deck:', len(card_list), '\n')

	hand_buffer = []
	for _ in range(num_rounds):
		hand = []
		cl_copy = copy.copy(card_list)
		for _ in range(num_draw):
			chosen = random.choice(cl_copy)
			hand.append(chosen)
			cl_copy.remove(chosen)

		hand_buffer.append(hand)

	if mode == 'use-dat':
		for hand in hand_buffer:
			print(hand, '\n')
	else:
		show_hands(path, hand_buffer, num_draw, num_rounds)