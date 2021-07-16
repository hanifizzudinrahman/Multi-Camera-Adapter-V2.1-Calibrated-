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

saat_ini = dtm.now() #tgl dan jam saat ini
now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string

camera = PiCamera()
camera.resolution = (3280, 2464)
time.sleep(1)

def main():
    
    print("Start testing the camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    captureRGB(1)     # Camera A

def captureRGB(cam):
    camera.rotation = 180
    camera.start_preview(resolution=(1920,1080))
    #time.sleep(5)             # Waktu Pengambilan Gambar
    time.sleep(2)
    camera.capture("Hasil_Gambar/[Camera A]_%s.jpg" % now)
    time.sleep(0.5)
    camera.stop_preview()
    time.sleep(0.2)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)





