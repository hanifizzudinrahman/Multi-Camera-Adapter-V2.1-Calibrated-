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

# For Perspective Images
#=======================================
print("=> For Perspective Images")
print("=="*25)
#===============================================
# Coordinate Kiri Atas
#===============================================
corKriAts = [[33, 65]]
corKriAtsB = [[19, 38]]
corKriAtsC = [[ 7, 58]]
corKriAtsD = [[ 9, 45]]
#==============================
print("==> Coordinate Kiri Atas")
print("=-"*25)
print('x1A,y1A = ', corKriAts)
print('x1B,y1B = ', corKriAtsB)
print('x1C,y1C = ', corKriAtsC)
print('x1D,y1D = ', corKriAtsD)
#===============================================
# Coordinate Kanan Atas
#===============================================
corKanAts = [[471,  52]]
corKanAtsB = [[461,  24]]
corKanAtsC = [[461,  35]]
corKanAtsD = [[455,  24]]
#==============================
print("==> Coordinate Kanan Atas")
print("=-"*25)
print('x2A,y2A = ', corKanAts)
print('x2B,y2B = ', corKanAtsB)
print('x2C,y2C = ', corKanAtsC)
print('x2D,y2D = ', corKanAtsD)
#===============================================
# Coordinate Kanan Bawah
#===============================================
corKanBwh = [[470, 638]]
corKanBwhB = [[462, 602]]
corKanBwhC = [[470, 622]]
corKanBwhD = [[458, 603]]
#==============================
print("==> Coordinate Kanan Bawah")
print("=-"*25)
print('x3A,y3A = ', corKanBwh)
print('x3B,y3B = ', corKanBwhB)
print('x3C,y3C = ', corKanBwhC)
print('x3D,y3D = ', corKanBwhD)
#===============================================
# Coordinate Kiri Bawah
#===============================================
corKriBwh = [[ 18, 631]]
corKriBwhB = [[ 16, 597]]
corKriBwhC = [[ 16, 633]]
corKriBwhD = [[ 14, 599]]
#==============================
print("==> Coordinate Kiri Bawah")
print("=-"*25)
print('x4A,y4A = ', corKriBwh)
print('x4B,y4B = ', corKriBwhB)
print('x4C,y4C = ', corKriBwhC)
print('x4D,y4D = ', corKriBwhD)
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
# Coordinate A
pts1 = np.float32([corKriAts[0],corKanAts[0],corKriBwh[0],corKanBwh[0]])
# Perspective Camera B-A
# Coordinate B
pts2 = np.float32([corKriAtsB[0],corKanAtsB[0],corKriBwhB[0],corKanBwhB[0]])
matrixB = cv2.getPerspectiveTransform(pts2,pts1)
# Perspective Camera C-A
# Coordinate C
pts2 = np.float32([corKriAtsC[0],corKanAtsC[0],corKriBwhC[0],corKanBwhC[0]])
matrixC = cv2.getPerspectiveTransform(pts2,pts1)
# Perspective Camera D-A
# Coordinate D
pts2 = np.float32([corKriAtsD[0],corKanAtsD[0],corKriBwhD[0],corKanBwhD[0]])
matrixD = cv2.getPerspectiveTransform(pts2,pts1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 2. Template Crop Images
print("==> 2. Template Crop Images")
print("="*50)
print()
start_point = (xMinCrop, yMinCrop)
end_point = (xMaxCrop, yMaxCrop)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
		
		# ========================================= Rotate Images
		# ================= Rotate Images A
		img[0] = cv2.rotate(img[0], cv2.ROTATE_90_COUNTERCLOCKWISE)
		# ================= Rotate Images B
		img[1] = cv2.rotate(img[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
		# ================= Rotate Images C
		img[2] = cv2.rotate(img[2], cv2.ROTATE_90_CLOCKWISE)
		# ================= Rotate Images D
		img[3] = cv2.rotate(img[3], cv2.ROTATE_90_CLOCKWISE)
		
		# ========================================= Perspective Images
		# ================= Images A is Same
		imgPerspectiveA = img[0]
		# ========================================= Perspective Images B-A
		imgPerspectiveB = cv2.warpPerspective(img[1],matrixB,(480,640))
		# ========================================= Perspective Images C-A
		imgPerspectiveC = cv2.warpPerspective(img[2],matrixC,(480,640))
		# ========================================= Perspective Images D-A
		imgPerspectiveD = cv2.warpPerspective(img[3],matrixD,(480,640))
		
		# ========================================= Crop Images (Final)
		imgCropA = imgPerspectiveA[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
		imgCropB = imgPerspectiveB[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
		imgCropC = imgPerspectiveC[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
		imgCropD = imgPerspectiveD[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
		
		#identifying the images
		cv2.putText(imgCropA, 'Cam A', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
		cv2.putText(imgCropB, 'Cam B', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
		cv2.putText(imgCropC, 'Cam C', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
		cv2.putText(imgCropD, 'Cam D', (5, 10), cv2.FONT_HERSHEY_SIMPLEX, .4, 255)
		#Combines the images into one to display
		image = np.zeros((2 * pixelYCrop, 2 * pixelXCrop, 3), dtype=np.uint8)
		image[0:pixelYCrop, 0:pixelXCrop, :] = imgCropA   # 0 = Camera A
		image[pixelYCrop:, 0:pixelXCrop, :] = imgCropC    # 2 = Camera C
		image[0:pixelYCrop, pixelXCrop:, :] = imgCropB    # 1 = Camera B
		image[pixelYCrop:, pixelXCrop:, :] = imgCropD    # 3 = Camera D
		
		cv2.putText(image, FPS, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
		
		# Display
		cv2.imshow('Multi-Camera Raspberry Pi', image)
	if mode == 2:
		for i in xrange(0, len(img)):
			# ================= Rotate Images A
			img[0] = cv2.rotate(img[0], cv2.ROTATE_90_COUNTERCLOCKWISE)
			# ================= Rotate Images B
			img[1] = cv2.rotate(img[1], cv2.ROTATE_90_COUNTERCLOCKWISE)
			
			# ========================================= Perspective Images
			# ================= Images A is Same
			imgPerspectiveA = img[0]
			# ========================================= Perspective Images B-A
			imgPerspectiveB = cv2.warpPerspective(img[1],matrixB,(480,640))
			
			# ========================================= Crop Images (Final)
			imgCropA = imgPerspectiveA[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
			imgCropB = imgPerspectiveB[yMinCrop:yMaxCrop, xMinCrop:xMaxCrop]
			
		cv2.putText(imgCropA, FPS, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
		cv2.putText(imgCropB, FPS, (0, 30), font, 1, (100, 255, 0), 3, cv2.LINE_AA)
		
		cv2.imshow('Camera A', imgCropA)
		cv2.imshow('Camera B', imgCropB)
		

if __name__ == "__main__":
	numberOfCameras = int(input("Number of cameras:"))
	configureMultiCamera()
	with picamera.PiCamera() as camera:
		
		#camera settings
		# width = 1280 - 640 - 320 - 160
		# height = 720 - 480 - 240 - 112
		width = 640
		height = 480
		camera.resolution = [width, height]
		print("Width: ", width, " and Height = ", height)
		print("="*50)
		print("Width-Calibrated: ", pixelYCrop, " and Height-Calibrated = ", pixelXCrop)
		
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
			
			for i in range(1,numberOfCameras+1):
				enableCamera(i)
				
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
			#cv2.imshow("camera A", img[0])
			#cv2.imshow("camera B", img[1])
			#cv2.imshow("camera C", img[2])
			#cv2.imshow("camera D", img[3])
			#cv2.waitKey(0)
			displayImage(img, 1, fps)
			#displayImage(img, 2)
			
			# If we press ESC then break out of the loop
			key = cv2.waitKey(7) % 0x100
			if key == 27:
				break
			
	disableMultiCamera()
	#Clears the cash at the end of the application
	cv2.destroyAllWindows()





