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
    
    # A / B / C / D
    ChooseCamera = 'D'   
    
    if ChooseCamera == 'A':
        print("Start testing the Camera A")
        i2c = "i2cset -y 1 0x70 0x00 0x04"
        os.system(i2c)
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        captureCamera(1)     # Camera A
    elif ChooseCamera == 'B':
        print("Start testing the Camera B")
        i2c = "i2cset -y 1 0x70 0x00 0x05"
        os.system(i2c)
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        captureCamera(3)     # Camera B
    elif ChooseCamera == 'C':
        print("Start testing the Camera C")
        i2c = "i2cset -y 1 0x70 0x00 0x06"
        os.system(i2c)
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        captureCamera(2)     # Camera C
    elif ChooseCamera == 'D':
        print("Start testing the Camera D")
        i2c = "i2cset -y 1 0x70 0x00 0x07"
        os.system(i2c)
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        captureCamera(4)     # Camera D

def captureCamera(cam):
    
    # used to record the time when we processed last frame
    prev_frame_time = 0
    # used to record the time at which we processed current frame
    new_frame_time = 0
    
    if cam == 1:
        CAM = 'A'
    elif cam == 2:
        CAM = 'C'
    elif cam == 3:
        CAM = 'B'
    elif cam == 4:
        CAM = 'D'
        
    if CAM == 'B' or CAM == 'D':
        # Rotate
        camera.rotation = 90
    elif CAM == 'A' or CAM == 'C':
        camera.rotation = 270
    # Flip
    #
    
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        image = frame.array
        
        saat_ini = dtm.now() #tgl dan jam saat ini
        now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
        
        # FPS
        # font which we will be using to display FPS
        font = cv2.FONT_HERSHEY_SIMPLEX
        # time when we finish processing for this frame
        new_frame_time = time.time()
        # since their will be most of time error of 0.001 second
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        # converting the fps into integer
        #fps = int(fps)
        # converting the fps into 2 decimal pint
        fps = format(fps, ".2f")
        fps = "FPS: " + str(fps)
        # puting the FPS count on the frame
        cv2.putText(image, fps, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
        
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        
        rawCapture.truncate(0)

        if key == ord("q"):
            break
        elif key == ord("s"):
            ImagePath = "Hasil_Gambar/[Camera_VID_" + CAM + "]_ %s.jpg" % now
            camera.capture(ImagePath)
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)







