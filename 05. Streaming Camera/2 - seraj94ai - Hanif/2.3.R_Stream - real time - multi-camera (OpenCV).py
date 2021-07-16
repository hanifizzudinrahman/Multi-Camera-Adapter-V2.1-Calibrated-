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
import io
import picamera
import picamera.array
from PIL import Image

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

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def pre_main():
    
    #numberOfCameras = int(input("Number of cameras:"))
    numberOfCameras = 4
    
    ## >>>>>>>>>>>>>>>>>>> C O N F I G U R E
    # Resolution
    # Default = 640x480
    # Raspberry Pi Camera v2 (8 megapixel): 3280 x 2464
    # video at 1080p30, 720p60, 640x480p90
    # width =  #1920 - 1280 - 640 - 320 - 160 - 80 - 40 [BEST = 3280]
    # height = #1080 - 720 - 480 - 240 - 120 - 60 - 30  [BEST = 2464]
    width = 320        
    height = 240
    
    with picamera.PiCamera() as camera:
        camera.resolution = [width, height]
        camera.framerate = 30
        
        #time to wait for the settings to be applied successfully
        time.sleep(2)
        
        #create all camera streams
        stream = list()
        for i in range(1,numberOfCameras+1):
            stream.append(io.BytesIO())
            
            check = 0
            
        while True:
            
            startTime = time.time()
            
            img = list()
            
            #===================================== C A M E R A - A
            cam = 1
            #print('-')
            i2c = "i2cset -y 1 0x70 0x00 0x04"
            os.system(i2c)
            gp.output(7, False)
            gp.output(11, False)
            gp.output(12, True)
            if cam == 1 and check == 1:
                camera.rotation = 90
            if cam == 3:
                camera.rotation = 270
                check = 1
            camera.capture('foto-'  + str(cam) + '.jpg')
            camera.capture(stream[cam-1], format='jpeg')
            data = np.fromstring(stream[cam-1].getvalue(), dtype=np.uint8)
            #Decode the image from the array, preserving colour
            image = cv2.imdecode(data, 1)
            #get the array of the image
            img.append(image.copy())
            #Delete the contents of a stream.
            stream[cam-1].seek(0)
            
            #===================================== C A M E R A - C
            cam = 2
            #print('-+')
            i2c = "i2cset -y 1 0x70 0x00 0x06"
            os.system(i2c)
            gp.output(7, False)
            gp.output(11, True)
            gp.output(12, False)
            if cam == 1 and check == 1:
                camera.rotation = 90
            if cam == 3:
                camera.rotation = 270
                check = 1
            camera.capture('foto-'  + str(cam) + '.jpg')
            camera.capture(stream[cam-1], format='jpeg')
            data = np.fromstring(stream[cam-1].getvalue(), dtype=np.uint8)
            #Decode the image from the array, preserving colour
            image = cv2.imdecode(data, 1)
            #get the array of the image
            img.append(image.copy())
            #Delete the contents of a stream.
            stream[cam-1].seek(0)
            
            if numberOfCameras == 4:
                #===================================== C A M E R A - B
                cam = 3
                #print('-+-')
                i2c = "i2cset -y 1 0x70 0x00 0x05"
                os.system(i2c)
                gp.output(7, True)
                gp.output(11, False)
                gp.output(12, True)
                if cam == 1 and check == 1:
                    camera.rotation = 90
                if cam == 3:
                    camera.rotation = 270
                    check = 1
                camera.capture('foto-'  + str(cam) + '.jpg')
                camera.capture(stream[cam-1], format='jpeg')
                data = np.fromstring(stream[cam-1].getvalue(), dtype=np.uint8)
                #Decode the image from the array, preserving colour
                image = cv2.imdecode(data, 1)
                #get the array of the image
                img.append(image.copy())
                #Delete the contents of a stream.
                stream[cam-1].seek(0)
                
                #===================================== C A M E R A - D
                cam = 4
                #print('-+-+')
                i2c = "i2cset -y 1 0x70 0x00 0x07"
                os.system(i2c)
                gp.output(7, True)
                gp.output(11, True)
                gp.output(12, False)
                if cam == 1 and check == 1:
                    camera.rotation = 90
                if cam == 3:
                    camera.rotation = 270
                    check = 1
                camera.capture('foto-'  + str(cam) + '.jpg')
                camera.capture(stream[cam-1], format='jpeg')
                data = np.fromstring(stream[cam-1].getvalue(), dtype=np.uint8)
                #Decode the image from the array, preserving colour
                image = cv2.imdecode(data, 1)
                #get the array of the image
                img.append(image.copy())
                #Delete the contents of a stream.
                stream[cam-1].seek(0)
            
            ##>>>>>>>>>>>>>>>>>>>>> D I S P L A Y - I M A G E
            """
            Displays the four images
            """
            mode = 1
            if not len(img) <= 0 and mode == 1:
                height, width, z = img[0].shape
                if len(img) < 4:
                    for i in range(4 - len(img), 4):
                        img.append(np.zeros((height, width, 3), dtype=np.uint8))
                #identifying the images
                cv2.putText(img[0], 'Cam 1', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
                cv2.putText(img[1], 'Cam 2', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
                cv2.putText(img[2], 'Cam 3', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
                cv2.putText(img[3], 'Cam 4', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
                #Combines the images into one to display
                image = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)
                image[0:height, 0:width, :] = img[0]
                image[height:, 0:width, :] = img[2]
                image[0:height, width:, :] = img[1]
                image[height:, width:, :] = img[3]
                
                # S T R E A M
                frame = cv2.imencode('.jpg', image)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
                # Display
                cv2.imshow('Multi-Camera Raspberry Pi', image)
            if mode == 2:
                for i in xrange(0, len(img)):
                    cv2.imshow('Camera ' + str(i+1), img[i])
            #===========================================================================
                    
            totalTime = time.time() - startTime
            print("Aquisition time: %f s" %(totalTime))
            print("FPS(all cameras): %f" %(1 / totalTime))
            
            # If we press ESC then break out of the loop
            key = cv2.waitKey(7) % 0x100
            if key == 27:
                break
            
        ##====================== D I S A B L E
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        
        #Clears the cash at the end of the application
        cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(pre_main(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    # defining server ip address and port
    # '192.168.1.112' - '192.168.43.37'
    HOST = '192.168.43.37'
    PORT = '5000'
    app.run(host=HOST,port=PORT, debug=True)




