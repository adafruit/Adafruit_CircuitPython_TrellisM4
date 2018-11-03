from adafruit_trellism4 import trellis

while True:
    pressed = trellis.pressed_keys
    if pressed:
        print("Pressed:", pressed)
