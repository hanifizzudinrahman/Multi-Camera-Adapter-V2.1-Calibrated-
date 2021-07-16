import RPi.GPIO as gp
from datetime import datetime as dtm
import cv2
import time
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

def main():

    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
    
    print("Start testing the Camera A", now)
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(1)     # Camera A
    
    print("Start testing the Camera C")
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(2)     # Camera C
    
    print("Start testing the Camera B")
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(3)     # Camera B
    
    print("Start testing the Camera D")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(4)     # Camera D
    
def captureCamera(cam):
    #cmd = "raspistill -o capture_%d.jpg" % cam
    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string

    if cam == 1:
        cmd = "nvgstcapture-1.0 -A --capture-auto -S 0 --image-res=3 --file-name=Hasil_Gambar/Camera_A_ %s.jpg" % now
    elif cam == 2:
        cmd = "nvgstcapture-1.0 -A --capture-auto -S 0 --image-res=3 --file-name=Hasil_Gambar/Camera_C_ %s.jpg" % now
    elif cam == 3:
        cmd = "nvgstcapture-1.0 -A --capture-auto -S 0 --image-res=3 --file-name=Hasil_Gambar/Camera_B_ %s.jpg" % now
    elif cam == 4:
        cmd = "nvgstcapture-1.0 -A --capture-auto -S 0 --image-res=3 --file-name=Hasil_Gambar/Camera_D_ %s.jpg" % now
    os.system(cmd)
    
if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)


