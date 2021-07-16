import RPi.GPIO as gp
from datetime import datetime as dtm
from picamera import PiCamera
import time
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

# Resolution
# Default = 640x480
# Raspberry Pi Camera v2 (8 megapixel): 3280 x 2464
# video at 1080p30, 720p60, 640x480p90
# width =  #1920 - 1280 - 640 - 320 - 160 - 80 - 40 [BEST = 3280]
# height = #1080 - 720 - 480 - 240 - 120 - 60 - 30  [BEST = 2464]
width = 1920        
height = 1080 
camera = PiCamera(resolution = (width, height))

def main():
    camera.rotation = 270
    print("Start testing the Camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(1)     # Camera A
    
    camera.rotation = 270
    print("Start testing the Camera C")
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(3)     # Camera C
    
    # Rotate
    camera.rotation = 90
    print("Start testing the Camera B")
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(2)     # Camera B
    
    # Rotate
    camera.rotation = 90
    print("Start testing the Camera D")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(4)     # Camera D
    
def captureCamera(cam):
    #if cam == 1 or cam == 2:
    #    camera.rotation = 180
    #elif cam == 3 or cam == 4:
    #    camera.rotation = 180
    
    camera.start_preview(resolution=(width,height))
    #time.sleep(2)             # Waktu Pengambilan Gambar
    
    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
    
    if cam == 1:
        camera.capture("Hasil_Gambar/[Camera A]_%s.jpg" % now)
    elif cam == 2:
        camera.capture("Hasil_Gambar/[Camera B]_%s.jpg" % now)
    elif cam == 3:
        camera.capture("Hasil_Gambar/[Camera C]_%s.jpg" % now)
    elif cam == 4:
        camera.capture("Hasil_Gambar/[Camera D]_%s.jpg" % now)
        
    #time.sleep(0.5)
    camera.stop_preview()
    #time.sleep(0.2)

if __name__ == "__main__":
    main()
