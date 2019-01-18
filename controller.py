from microbit import *
import radio

radio.on()
radio.config(channel=18)

display.show(Image.CHESSBOARD)

while True:
    if button_a.was_pressed():
        radio.send('togglelight')
        
    if button_b.was_pressed():
        radio.send('togglemovement')
        