#imports
import time as t
import pyautogui as pg

#important
refreshperiod = '1000' #(default)
refreshperiod = int(pg.prompt(text='refresh period? (dont forget to open a SU terminal)', title='refresh period?', default=''))

#unimportant
delay = 0.5
delvar = 57 + len(str(refreshperiod))
iteration = 0


#DEF:

def openff():
	t.sleep(delay)
	#go to firefox
	pg.click(890,1050)
	t.sleep(delay)

def searchff(query):
	#new tab + google btc price
	pg.hotkey('ctrl','t')
	pg.write(query, interval=0.05)
	pg.press('enter')
	t.sleep(3)

	#highlight + copy text
	pg.moveTo(30, 350)
	pg.mouseDown() #(30,350)
	pg.mouseUp(x=250, y=350)
	t.sleep(delay)
	pg.hotkey('ctrl', 'c')
	t.sleep(delay)
def enterm(keyword):
	pg.click(1300,330)
	pg.hotkey('ctrl','w')
	pg.write(keyword, interval=0.05)
	pg.press('enter')
	pg.press('down')
	pg.press('down')
	pg.press('left', presses=6)

#typeterm with no modifiers
def typetermNOMOD():
	t.sleep(delay)
	pg.press('backspace', presses=delvar) #37
	pg.typewrite('Current BTC price: ', interval=0.05)
	pg.hotkey('ctrl','shift','v')
	pg.typewrite(' (updating every ' + str(refreshperiod) + ' seconds)', interval=0.05)
	t.sleep(delay)
	pg.hotkey('ctrl','s')

#close tab
def closepfftab():
	
	pg.click(890,1050)
	pg.hotkey('ctrl','w')

#the goods:
while True:
	
	#open firefox:
	openff()

	#search for btc:
	searchff('bitcoin price')
	#entering terminal:
	enterm('BITCOININIT')
	#typeterm
	typetermNOMOD()
#	pg.press('right', presses=5)
	#close tab
	closepfftab()

	iteration +=1
	print("iteration " + str(iteration))
	#delay/repeat
	t.sleep(refreshperiod)

