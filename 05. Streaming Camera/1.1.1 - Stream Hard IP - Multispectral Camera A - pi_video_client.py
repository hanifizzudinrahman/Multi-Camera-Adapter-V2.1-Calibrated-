import RPi.GPIO as gp
import os
import cv2

import io
import socket
import struct
import time
import picamera
import sys

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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '192.168.43.210'     # '192.168.1.106' - '192.168.43.210'
Port = 8000
client_socket.connect((IP, Port))

connection = client_socket.makefile('wb')
try:
    print("Start testing the camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    #captureCamera(1)     # Camera A
    
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        print("starting Camera...........")
        time.sleep(2)
        stream = io.BytesIO()        
        
        for foo in camera.capture_continuous(stream, 'jpeg'):
            
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            stream.seek(0)
            stream.truncate()
        
finally:
    connection.close()
    client_socket.close()



