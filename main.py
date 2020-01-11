import random, copy

# GLOBAL CONFIG
FILE = './my_deck.dat'	# path to deck recipe file
NUM_DRAW = 4			# number of draw
NUM_ROUNDS = 10			# number of simulation rounds

##
def convert_to_list(file_path):
	with open(file_path, 'r') as f:
		card_list = []
		
		for line in f:
			if not line[0].isalpha():
				continue
				
			card_number_pair = line.strip().split(',')
			
			for _ in range(int(card_number_pair[1])):
				card_list.append(card_number_pair[0])
				
	return card_list

if __name__ == '__main__':
	card_list = convert_to_list(FILE)
	print('Number of cards in deck:', len(card_list))
		
	for i in range(1, NUM_ROUNDS+1):
		
		if type(NUM_DRAW) == list:
			num_draw = random.choice(NUM_DRAW)
		elif type(NUM_DRAW) == int:
			num_draw = NUM_DRAW
		else:
			raise TypeError('NUM_DRAW must be either list or int.')
			
		print('Round %s (%s cards drawn):' % (i, num_draw))
		
		hand = []
		cl_copy = copy.copy(card_list)
		for _ in range(num_draw):
			chosen = random.choice(cl_copy)
			hand.append(chosen)
			cl_copy.remove(chosen)
		
		print(hand, '\n')