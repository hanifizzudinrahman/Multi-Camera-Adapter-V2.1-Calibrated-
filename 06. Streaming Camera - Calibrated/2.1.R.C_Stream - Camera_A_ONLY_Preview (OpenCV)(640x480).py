# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019

@author: seraj
"""
import time
import cv2 
from flask import Flask, render_template, Response

import RPi.GPIO as gp
from datetime import datetime as dtm
import os
import numpy as np

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

# For Perspective Images
#=======================================
print("=> For Perspective Images")
print("=="*25)
#===============================================
# Coordinate Kiri Atas
#===============================================
corKriAts = [[33, 65]]
#==============================
print("==> Coordinate Kiri Atas")
print("=-"*25)
print('x1A,y1A = ', corKriAts)
#===============================================
# Coordinate Kanan Atas
#===============================================
corKanAts = [[471,  52]]
#==============================
print("==> Coordinate Kanan Atas")
print("=-"*25)
print('x2A,y2A = ', corKanAts)
#===============================================
# Coordinate Kanan Bawah
#===============================================
corKanBwh = [[470, 638]]
#==============================
print("==> Coordinate Kanan Bawah")
print("=-"*25)
print('x3A,y3A = ', corKanBwh)
#===============================================
# Coordinate Kiri Bawah
#===============================================
corKriBwh = [[ 18, 631]]
#==============================
print("==> Coordinate Kiri Bawah")
print("=-"*25)
print('x4A,y4A = ', corKriBwh)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print()

# For Crop Images (Final)
#=======================================
print("=> For Crop Images (Final)")
print("=="*25)
#===============================================
xMinCrop = 33
yMinCrop = 33
xMaxCrop = 475
yMaxCrop = 631
pixelXCrop = 442 
pixelYCrop = 598
#===============================================
print("xMinCrop: ", xMinCrop)
print("yMinCrop: ", yMinCrop)
print("xMaxCrop: ", xMaxCrop)
print("yMaxCrop: ", yMaxCrop)
print("pixelXCrop: ", pixelXCrop)
print("pixelYCrop: ", pixelYCrop)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("==> 1. Template Perspective Images")
print("="*50)
print()
# Perspective Camera A
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 2. Template Crop Images
print("==> 2. Template Crop Images")
print("="*50)
print()
start_point = (xMinCrop, yMinCrop)
end_point = (xMaxCrop, yMaxCrop)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def captureCamera(cam):
    
    print("Start testing the Camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    
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
            
            if cam == 2 or cam == 4:
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            elif cam == 1 or cam == 3:
                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            #    print('putar')
            
            # ========================================= Perspective Images
            # Images A is same
            imgPerspective = img
            
            # ========================================= Crop Images (Final)
            imgCropFinal = imgPerspective[yMinCrop:yMaxCrop+1, xMinCrop:xMaxCrop+1]
            
            frame = cv2.imencode('.jpg', imgCropFinal)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            cv2.imshow("CSI Camera", imgCropFinal)
            # This also acts as
            key = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if key == ord("q"):
                break
            elif key == ord("s"):
                if cam == 1:
                    cv2.imwrite("Hasil_Gambar/Camera_A_ %s.jpg" % now, imgCropFinal)
                elif cam == 2:
                    cv2.imwrite("Hasil_Gambar/Camera_B_ %s.jpg" % now, imgCropFinal)
                elif cam == 3:
                    cv2.imwrite("Hasil_Gambar/Camera_C_ %s.jpg" % now, imgCropFinal)
                elif cam == 4:
                    cv2.imwrite("Hasil_Gambar/Camera_D_ %s.jpg" % now, imgCropFinal)
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(captureCamera(1),    # 1 = CAM A
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    # defining server ip address and port
    # '192.168.1.112' - '192.168.43.37'
    HOST = '192.168.1.112'
    PORT = '4000'
    app.run(host=HOST,port=PORT, debug=True)


