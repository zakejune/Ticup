import time, sensor, image, pyb
from pyb import UART
from pyb import LED
import json

uart = UART(3, 115200)
uart.init(115200, bits=8, parity=None, stop=1)  # init with given parameters
threshold =(60, 24, 36, 76, -19, 71)
blue_led = LED(1)
la_led = LED(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)  # must be turned off for color tracking
clock = time.clock()

x=0
y=0

while (True):
    clock.tick()

    img = sensor.snapshot()
    blobs = img.find_blobs([threshold], pixels_threshold=10, area_threshold=10, merge=True)
    la_led.on()
    time.sleep(500)
    la_led.off()

    verify = bytearray([0xB3, 0xB3])
    uart.write(verify)

    for b in blobs:
        img.draw_rectangle(b[0:4])
        img.draw_cross(b.cx(), b.cy())
        img.draw_circle(b[5], b[6], 10, color=(255, 0, 0))
        x = b.cx()
        y = b.cy()
        area=w*h
        data = bytearray([x, y])
        uart.write(data)
        print(x)
        print(y)
