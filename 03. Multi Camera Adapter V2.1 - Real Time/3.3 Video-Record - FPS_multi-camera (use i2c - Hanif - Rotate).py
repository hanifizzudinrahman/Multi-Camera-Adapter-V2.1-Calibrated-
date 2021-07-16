#!/user/bin/python

# @Author: Maik Basso <maik@maikbasso.com.br>

import RPi.GPIO as gp
import time
import numpy as np
import os
import io
import cv2
import picamera
import picamera.array
from PIL import Image
from datetime import datetime as dtm

def configureMultiCamera():
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

def enableCamera(num):
	if num == 1: # Camera A
		i2c = "i2cset -y 1 0x70 0x00 0x04"
		os.system(i2c)
		gp.output(7, False)
		gp.output(11, False)
		gp.output(12, True)
	elif num == 2: # Camera C
		i2c = "i2cset -y 1 0x70 0x00 0x06"
		os.system(i2c)
		gp.output(7, False)
		gp.output(11, True)
		gp.output(12, False)
	elif num == 3: # Camera B
		i2c = "i2cset -y 1 0x70 0x00 0x05"
		os.system(i2c)
		gp.output(7, True)
		gp.output(11, False)
		gp.output(12, True)
	elif num == 4: # Camera D
		i2c = "i2cset -y 1 0x70 0x00 0x07"
		os.system(i2c)
		gp.output(7, True)
		gp.output(11, True)
		gp.output(12, False)

def disableMultiCamera():
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)

def capture(cam):
    camera.capture('foto-'  + str(cam) + '.jpg')
    
def displayImage(img, mode, FPS):
	"""
	Displays the four images
	"""
	# font which we will be using to display FPS
	font = cv2.FONT_HERSHEY_SIMPLEX
	
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
		
		cv2.putText(image, FPS, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
		
		# Display
		cv2.imshow('Multi-Camera Raspberry Pi', image)
	if mode == 2:
		for i in xrange(0, len(img)):
			cv2.putText(img[i], FPS, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
			
			cv2.imshow('Camera ' + str(i+1), img[i])
	return image

if __name__ == "__main__":
	saat_ini = dtm.now() #tgl dan jam saat ini
	now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
	
	numberOfCameras = int(input("Number of cameras:"))
	configureMultiCamera()
	with picamera.PiCamera() as camera:
		
		#camera settings
		#camera.resolution = [160,120]
		#camera.resolution = [320, 240]
		# width = 640 - 320 - 160
		# height = 480 - 240 - 112
		width = 640
		height = 480
		camera.resolution = [width, height]
		print("Width: ", width, " and Height = ", height)
		
		camera.framerate = 30
		
		#time to wait for the settings to be applied successfully
		time.sleep(2)
		
		#create all camera streams
		stream = list()
		for i in range(1,numberOfCameras+1):
			stream.append(io.BytesIO())
			
			check = 0
			
		# Record
		VideoName = 'Real-Time_Video_' + str(numberOfCameras) + 'Cam_(' + str(width) + 'x' + str(height) + ')-' + now
		VideoPathSave = 'Hasil_Video/' + VideoName + '.avi'
		# Define the codec and create VideoWriter object
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter(VideoPathSave, fourcc, 20.0, (2*width, 2*height))
		
		while True:
			
			startTime = time.time()
			
			img = list()
			
			for i in range(1,numberOfCameras+1):
				enableCamera(i)
				
				if i == 1 and check == 1:
					camera.rotation = 360
				if i == 3:
					camera.rotation = 180
					check = 1
				camera.capture(stream[i-1], format='jpeg')
				data = np.fromstring(stream[i-1].getvalue(), dtype=np.uint8)
				#Decode the image from the array, preserving colour
				image = cv2.imdecode(data, 1)
				#get the array of the image
				img.append(image.copy())
				#Delete the contents of a stream.
				stream[i-1].seek(0)
			
			totalTime = time.time() - startTime
			#print("Aquisition time: %f s" %(totalTime))
			#print("FPS(all cameras): %f" %(1 / totalTime))
			
			fps = 1 / totalTime
			fps = format(fps, ".2f")
			
			#Display all images
			# output the frame (Record)
			out.write(displayImage(img, 1, fps))
			#displayImage(img, 2)
			
			# If we press ESC then break out of the loop
			key = cv2.waitKey(7) % 0x100
			if key == 27:
				break
			
	disableMultiCamera()
	out.release()
	#Clears the cash at the end of the application
	cv2.destroyAllWindows()






