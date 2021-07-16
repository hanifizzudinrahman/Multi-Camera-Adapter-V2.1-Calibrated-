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
    
def main():
    
    print("Start testing the Camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(1)     # Camera A
    
def captureCamera(cam):
    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string

    cap = cv2.VideoCapture(0)
        
    if cap.isOpened():
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        
        # Resolution
        # Default = 640x480
        # Raspberry Pi Camera v2 (8 megapixel): 3280 x 2464
        # video at 1080p30, 720p60, 640x480p90
        # width =  #1920 - 1280 - 640 - 320 - 160 - 80 - 40 [BEST = 3280]
        # height = #1080 - 720 - 480 - 240 - 120 - 60 - 30  [BEST = 2464]
        width = 640        
        height = 480        
        cap.set(3, width)
        cap.set(4, height)
        
        # Window
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            
            #Rotate
            #img = cv2.rotate(img, cv2.ROTATE_180)
            # Flip   (0 = vertical, 1 = horizontal, -1 = vertical&horizontal
            #img = cv2.flip(img, 0) 
    
            cv2.imshow("CSI Camera", img)
            # This also acts as
            key = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if key == ord("q"):
                break
            elif key == ord("s"):
                cv2.imwrite("Hasil_Gambar/Camera_A_ %s.jpg" % now, img)
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)

