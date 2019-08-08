import pyb,sensor,time,image,math

from pyb import UART
from pyb import LED
import json 

uart =UART(3,115200)
uart.init(115200,bits=8,parity=None,stop=1)
threshold =(60, 24, 36, 76, -19, 71)
blue_led =LED(1)
red_led=LED(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)  # must be turned off for color tracking
clock = time.clock()

x=0
y=0

while(True)
   clock.tick()

   img=sensor.snapshot()
   blobs = img.find_blobs([threshold], pixels_threshold=10, area_threshold=10, merge=True)
    red_led.on()
    time.sleep(500)
    red_led.off()

    verify=bytearray([0xb3,0xb3])
    uart.write(verify)

    for b in blobs:
        img.draw_rectangle(n[0:4])
        