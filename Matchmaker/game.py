import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbol(x,y):
    global firstCard
    global previousx_cord, previousy_cord
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if firstCard:
        previousx_cord = x
        previousy_cord = y
        firstCard = False
    elif previousx_cord!=x or previousy_cord!=y:
        if buttons[previousx_cord,previousy_cord]['text']!=buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx_cord,previousy_cord]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx_cord, previousy_cord]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        firstCard = True

win = Tk()
win.title("Match Maker")
win.resizable(width=False, height=False)
firstCard = True
previousx_cord = 0
previousy_cord = 0
# Adding symbols
print(U'\u2702')
buttons = {}
button_symbols = {}
symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u270A', u'\u2709', u'\u270B',
            u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2718',
            u'\u2702', u'\u2705', u'\u2708', u'\u270A', u'\u2709', u'\u270B',
            u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2718']
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x, y=y: show_symbol(x,y), width=4, height=4)
        button.grid(column=x, row=y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

win.mainloop()