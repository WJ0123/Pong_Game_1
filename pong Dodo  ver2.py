from Tkinter import *
from datetime import datetime
import time, random

opentime = datetime.strptime('2017-12-18','%Y-%m-%d')
nowtime = datetime.now()

#----------------#
winheight = 400
winwidth = 600
ballsize = 6
ballspeed = 2.2
boxspeed = 7
boxheight = 50
boxwidth = 10

#----------------#

dybox = [1,1.5,2.5,2.7,3,3.3,3.5]
ranbox = [[2.2,'white'], [2.3,'grey'], [2.4,'gold'], [2.5,'blue'], \
			[2.6,'purple'], [3,'yellow'], [4,'orange'], [4.5,'red']] 
aa = 0

player1s = 0
player2s = 0
ballx = winwidth/2
bally = winheight/2
balldx = ballspeed
balldy = ballspeed
box1x = 15
box1y = winheight/2

box2x = winwidth-15-boxwidth
box2y = winheight/2

box1dy = 0
box2dy = 0

if nowtime> opentime: win = Tk()

win.title('Pong')
canv = Canvas(win, width = winwidth, height = winheight, bg = 'black')
ball = canv.create_oval(ballx - ballsize, bally- ballsize, ballx + ballsize, bally + ballsize, fill = 'white', outline = 'white')
box1 = canv.create_rectangle(box1x, box1y, box1x + boxwidth, box1y + boxheight, fill = 'white', outline = 'white')
box2 = canv.create_rectangle(box2x, box2y, box2x + boxwidth, box2y + boxheight, fill = 'white', outline = 'white')
text = canv.create_text(winwidth/2, 10, text = str(player1s) + '|' + str(player2s), tags = 'txt', fill = 'white', font = 'arial 10')

canv.pack()

def box1mv(a): 
	global box1dy
	box1dy = a
	
def box2mv(a): 
	global box2dy
	box2dy = a

def keys(event):
	global aa
	
	if event.keysym == 'Escape': win.destroy()
	elif event.keysym == 'p':
		if aa == 0: aa = 1
		else: 
			aa = 0
			motion()
			
def collision(ball, box):
	return not (ball[0] >= box[2] or ball[2] <= box[0] or ball[1] >= box[3] or ball[3] <= box[1] )
	
def motion():
	global player1s, player2s, winwidth, ballsize, ballspeed, balldx, balldy, boxspeed, boxheight, \
			boxwidth, ballx, bally, box1x, box1y, box2x, box2y, aa, box1dy, box2dy
	
	while aa != 1:
		canv.move(ball, balldx, balldy)
		if canv.coords(ball)[1] <= 0 or canv.coords(ball)[3] >= winheight: balldy = -balldy
		
		if canv.coords(box1)[1] >= 0 and canv.coords(box1)[3] <= winheight: canv.move(box1, 0, box1dy)
		elif canv.coords(box1)[1] <= 0 : canv.move(box1, 0, 2) 
		elif canv.coords(box1)[3] >= winheight: canv.move(box1, 0, -2)
		
		if canv.coords(box2)[1] >= 0 and canv.coords(box2)[3] <= winheight: canv.move(box2, 0, box2dy)
		elif canv.coords(box2)[1] <= 0 : canv.move(box2, 0, 2) 
		elif canv.coords(box2)[3] >= winheight: canv.move(box2, 0, -2)
		
		if collision(canv.coords(ball), canv.coords(box1)) or collision(canv.coords(ball), canv.coords(box2)):
			balldx = -balldx
			
		if canv.coords(ball)[0] <= 0:
			balldx = -balldx
			player2s += 1
			chosen = random.choice(ranbox)
			canv.itemconfig(ball, fill = chosen[1], outline = chosen[1])
			balldx = chosen[0]
			bally = random.choice(dybox)
			canv.coords(ball, winwidth/2 - ballsize, winheight/2 - ballsize, winwidth/2 + ballsize, winheight/2 + ballsize)
			canv.delete('txt')
			canv.create_text(winwidth/2, 10, text = str(player1s) + '|' + str(player2s), \
				tags = 'txt', fill = 'white', font = 'arial 10')
		
		elif canv.coords(ball)[0] >= winwidth:
			balldx = -balldx
			player1s += 1
			chosen = random.choice(ranbox)
			canv.itemconfig(ball, fill = chosen[1], outline = chosen[1])
			balldx = chosen[0]
			bally = random.choice(dybox)
			canv.coords(ball, winwidth/2 - ballsize, winheight/2 - ballsize, winwidth/2 + ballsize, winheight/2 + ballsize)
			canv.delete('txt')
			canv.create_text(winwidth/2, 10, text = str(player1s) + '|' + str(player2s), \
				tags = 'txt', fill = 'white', font = 'arial 10')
		
		canv.update()
		time.sleep(.01)
		


win.bind('<KeyPress-w>', lambda x: box1mv(-boxspeed)) 
win.bind('<KeyRelease-w>', lambda x: box1mv(0))
win.bind('<KeyPress-x>', lambda x: box1mv(boxspeed)) 
win.bind('<KeyRelease-x>', lambda x: box1mv(0))
win.bind('<KeyPress-o>', lambda x: box2mv(-boxspeed)) 
win.bind('<KeyRelease-o>', lambda x: box2mv(0))
win.bind('<KeyPress-m>', lambda x: box2mv(boxspeed)) 
win.bind('<KeyRelease-m>', lambda x: box2mv(0))

win.bind('<Key>', keys)
		
motion()

win.mainloop()

	
