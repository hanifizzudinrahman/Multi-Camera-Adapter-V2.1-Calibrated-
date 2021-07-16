import RPi.GPIO as gp
from datetime import datetime as dtm
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

camera = PiCamera()

# Resolution
# Default = 640x480
# Raspberry Pi Camera v2 (8 megapixel): 3280 x 2464
# video at 1080p30, 720p60, 640x480p90
# width =  #1920 - 1280 - 640 - 320 - 160 - 80 - 40 [BEST = 3280]
# height = #1080 - 720 - 480 - 240 - 120 - 60 - 30  [BEST = 2464]
width = 640        
height = 480 
camera.resolution = (width, height)

#camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(width, height))

time.sleep(1)

def main():
    
    print("Start testing the camera C")
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(3)

def captureCamera(cam):
    
    # Rotate
    camera.rotation = 270
    # Flip
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array
        
        saat_ini = dtm.now() #tgl dan jam saat ini
        now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
        
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        
        rawCapture.truncate(0)

        if key == ord("q"):
            break
        elif key == ord("s"):
            camera.capture("Hasil_Gambar/[Camera C]_%s.jpg" % now)
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)







