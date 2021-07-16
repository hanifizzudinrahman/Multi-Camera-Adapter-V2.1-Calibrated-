import RPi.GPIO as gp
from datetime import datetime as dtm
import cv2
import time
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

def main():
    
    print("Start testing the Camera A")
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
    captureCamera(3)     # Camera C
    
    print("Start testing the Camera B")
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    captureCamera(2)     # Camera B
    
    print("Start testing the Camera D")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(4)     # Camera D
    
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
            
            if cam == 2 or cam == 4:
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                if cam == 2:
                    # ========================================= Perspective Images B-A
                    imgPerspective = cv2.warpPerspective(img,matrixB,(480,640))
                else:
                    # ========================================= Perspective Images D-A
                    imgPerspective = cv2.warpPerspective(img,matrixD,(480,640))
            elif cam == 1 or cam == 3:
                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                if cam == 1:
                    # ========================================= Perspective Images A is same
                    imgPerspective = img
                else:
                    # ========================================= Perspective Images C-A
                    imgPerspective = cv2.warpPerspective(img,matrixC,(480,640))
                    
            # ========================================= Crop Images (Final)
            imgCropFinal = imgPerspective[yMinCrop:yMaxCrop+1, xMinCrop:xMaxCrop+1]
            
            # ========================================= Rotate Vertikal
            imgCropFinal = cv2.rotate(imgCropFinal, cv2.ROTATE_90_CLOCKWISE)
        
            #    print('putar')
            cv2.imshow("CSI Camera", imgCropFinal)
            # This also acts as
            key = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if key == ord("q"):
                break
            elif key == ord("s"):
                if cam == 1:
                    cv2.imwrite("Hasil_Gambar/C.Camera_A_ %s.jpg" % now, imgCropFinal)
                elif cam == 2:
                    cv2.imwrite("Hasil_Gambar/C.Camera_B_ %s.jpg" % now, imgCropFinal)
                elif cam == 3:
                    cv2.imwrite("Hasil_Gambar/C.Camera_C_ %s.jpg" % now, imgCropFinal)
                elif cam == 4:
                    cv2.imwrite("Hasil_Gambar/C.Camera_D_ %s.jpg" % now, imgCropFinal)
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


