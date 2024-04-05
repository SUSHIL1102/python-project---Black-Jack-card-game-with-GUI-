import blackjack
import tkinter
from tkinter import messagebox # Dialog boxes
from PIL import Image, ImageTk # Images for cards
import time
import os
import sys

game_on = False

def restart():
	global game_on
	game_on = True
	window.destroy()

# Called when the player hits
def hit():
	p.draw()
	if p.sum() > 21: # Player is bust
		messagebox.showinfo(message="You bust\nYou lost!!")
		restart()

	elif p.sum() == 21: # Player wins
		messagebox.showinfo(message="Blackjack!! \nYou won!!")
		restart()

# Called when the player stands
def stand():
	# Destroy the "Hit" and "Stand" buttons and the frame that contains the two
	# face-down cards for the dealer
	for w in (hitButton, standButton):
		w.destroy()


	imglabel.destroy()

	# Keep hitting as long as the hand score is less than 21
	while d.sum() < 17:
		d.draw()
		if d.sum() > 21: # Dealer bust
			messagebox.showinfo(message="Dealer bust\nYou won!!")
			# window.destroy() # Destroy the window and its contents
			restart()
			return

	# Dealer completes turn without busting
	endGame()

# command for the Rules button
def Rules():
	r = """
	RULES:
Beat the dealers hand to win.
Kings, Queens and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
HIT - to draw another card.
STAND - to stop taking cards.
a pushback(tie) is when the dealer and the player have equal hand.
The dealer stops hitting at 17."""
	messagebox.showinfo(message=r)


# Called after a player stands and dealer plays without going bust
def endGame():
	psum = p.sum()
	dsum = d.sum()
	# Template for the final message that will be displayed when game ends
	scoreboard = f"Dealer score: {dsum}\nYour score: {psum}\n"

	# Construct and display the final message from the "scoreboard", based on the result of the game.
	if psum > dsum:
		messagebox.showinfo(message=scoreboard + "You win!!")
	elif psum < dsum:
		messagebox.showinfo(message=scoreboard + "You lose!!")
	else:
		messagebox.showinfo(message=scoreboard + "Push (Tie)...")

	# window.destroy() # Destroy the window and its contents
	restart()

# Initialise the window
window = tkinter.Tk()
window.geometry('1200x600')
window['background'] = "green"

# The player
p = blackjack.player(window, 'Player')
p.draw(); p.draw();

# Just a frame to show two cards face down, as is the convention for the dealer.
# The dealer isn't actually initialised.\
d = blackjack.player(window, 'Dealer')
d.draw()
im = Image.open("backside.png")
im = im.resize((150, 217))
img = ImageTk.PhotoImage(im)
imglabel = tkinter.Label(d.frame, image=img)
imglabel.image = img
imglabel.pack(side="left")

# Frame for buttons
buttonFrame = tkinter.Frame(window)
buttonFrame['background'] = "green"
buttonFrame.pack()

# Button for the player to hit
hitButton = tkinter.Button(buttonFrame, text="Hit", command=hit, font=("Helvetica", 14))
hitButton.grid(row=0, column=1, padx=10)

# Button for the player to stand
standButton = tkinter.Button(buttonFrame, text="Stand", command=stand, font=("Helvetica", 14))
standButton.grid(row=0,column=2)

# rules button
rulesButton = tkinter.Button(buttonFrame, text="Rules", command=Rules, font=("Helvetica", 14))
rulesButton.grid(row=1,column=1,padx=5,pady=5)

# exit button
button_quit = tkinter.Button(buttonFrame,text='Exit game',command=window.quit,font=("Helvetica", 14))
button_quit.grid(row=1, column=2,padx=5,pady=5 )

tkinter.mainloop()
