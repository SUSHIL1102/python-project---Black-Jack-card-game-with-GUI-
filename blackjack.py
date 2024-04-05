import random
import tkinter
from PIL import Image, ImageTk

deck = []
# Initialise the deck of cards. Each card is a dictionary of the form:
# {
#  'name':  'ace', 'jack', '1', '4', etc.
#  'suite': 'spades', 'clubs', etc.
#  'value': the value of the card in the hand, as an integer
# }
def deck_init():
	for suite in ('spades', 'clubs', 'diamonds', 'hearts'):
		deck.append({ # The ace
			'name': 'ace',
			'suite': suite,
			'value': 1
		})

		for i in range(2, 11): # 9 number cards
			deck.append({
				'name': str(i),
				'suite': suite,
				'value': i
			})

		for i in ('jack', 'queen', 'king'): # Face cards
			deck.append({
				'name': i,
				'suite': suite,
				'value': 10
			})
	random.shuffle(deck)
deck_init()

# A class to represent a player. Both the dealer and user are players.
# Each player object keeps track of the cards in the hand.
# Each player object is associated with one tkinter.Frame, which is used to display cards.
class player():
	def __init__(self, window, playerTitle):
		# The player's hand
		self.hand = []

		# The name of the player
		self.title = playerTitle

		# Frame to contain the player's cards
		self.frame = tkinter.Frame(window)
		self.frame.pack(anchor="w")
		self.frame['background'] = "green"

		# A label to display the value of the hand, live
		self.sumLabel = tkinter.Label(self.frame, text=str(self.title) + "'s hand:  ", fg="#ccc")
		self.sumLabel.pack(anchor="w")
		self.sumLabel['background'] = "green"

	# Function to draw a card.
	# Appends that card to the hand, removes from deck, and updates the images.
	def draw(self):
		if len(deck) == 0:
			deck_init()
		random.shuffle(deck)
		self.hand.append(deck.pop(0))
		self.sumLabel['text'] = str(self.title) + "'s hand:  " + str(self.sum())
		card = self.hand[-1]

		im = Image.open(f"{card['name']}_of_{card['suite']}.png")
		im = im.resize((150, 217))
		img = ImageTk.PhotoImage(im)
		imglabel = tkinter.Label(self.frame, image=img)
		imglabel.image = img
		imglabel.pack(side="left")

	# Calculate value of the hand
	def sum(self):
		total = 0
		# First add all the cards that are not aces
		for card in self.hand:
			if not card['name'] == 'ace':
				total += card['value']

		# Now we deal with the aces
		# First add 1 for every ace
		for card in self.hand:
			if card['name'] == 'ace':
				total += 1
		# Then we keep adding 10 for every ace, as long as the sum doesn't exceed 10
		for card in self.hand:
			if card['name'] == 'ace':
				if total <= 11:
					total += 10

		return total
