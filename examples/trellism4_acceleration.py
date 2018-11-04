import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()

while True:
    x, y, z = trellis.acceleration
    print(x, y, z)
    time.sleep(0.1)
