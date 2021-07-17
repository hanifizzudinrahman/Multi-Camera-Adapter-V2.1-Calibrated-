import os 
import cv2
import numpy as np

# For Read Images
#=======================================
numberTest = 1
folderPercobaan = r"Percobaan 1 - Depan Kamar (Horizontal)\\"
    #   "Percobaan 1 - Depan Kamar (Horizontal)\\"
    #   "Percobaan 2 - Atap Kamar (Vertikal)\\"
folderOriginalImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\1_Original-Images\\" + folderPercobaan
folderFinalImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\_Final-Images_Calibration\\" + folderPercobaan
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("=> For Read Images")
print("=="*25)
print("Number Test: ", numberTest)
print("folderPercobaan: ", folderPercobaan)
print("folderOriginalImages: ", folderOriginalImages)
print("folderFinalImages: ", folderFinalImages)
print("="*50)
#===============================================
    # IMAGES INFORMATION
print("==> IMAGES INFORMATION")
Rotate = "R."    # if no Ratate, change to ""
noImage = 1
anotherParams = 1
imagesName = Rotate + str(noImage) + "." + str(anotherParams)
#===============================================
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("noImage: ", noImage)
print("anotherParams: ", anotherParams)
print("imagesName: ", imagesName)
print("="*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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
CropKriAts = [33, 32]
CropKanAts = [475, 33]
CropKanBwh = [476, 634]
CropKriBwh = [7, 631]
#===============================================
print("CropKriAts: ", CropKriAts)
print("CropKanAts: ", CropKanAts)
print("CropKanBwh: ", CropKanBwh)
print("CropKriBwh: ", CropKriBwh)
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Process Image (Final)
print("==> Process Image (Final)")
print("="*50)
print()
for filename in os.listdir(folderOriginalImages):
    if filename[:2] == Rotate:
        print(filename)
        imagePath = folderOriginalImages + filename
        img = cv2.imread(imagePath)
        #cv2.imshow("img", img)
        # ========================================= Perspective Images
        # Images A
        if filename[2:3] == "A":
            # ==> Perspective Camera A is same
            imgPerspective = img
        # Images B
        elif filename[2:3] == "B":
            # Perspective Camera B-A
            imgPerspective = cv2.warpPerspective(img,matrixB,(480,640))
        # Images C
        elif filename[2:3] == "C":
            # Perspective Camera C-A
            imgPerspective = cv2.warpPerspective(img,matrixC,(480,640))
        # Images D
        elif filename[2:3] == "D":
            # Perspective Camera D-A
            imgPerspective = cv2.warpPerspective(img,matrixD,(480,640))
        #cv2.imshow("imgPerspective", imgPerspective)
        # =====================================================================
        # ========================================= Crop Images (Final)
        imgCropFinal = imgPerspective[yMinCrop:yMaxCrop+1, xMinCrop:xMaxCrop+1]
        #cv2.imshow("imgCropFinal", imgCropFinal)
        # =====================================================================
        # ========================================= Write Images (Final)
        pathWrite = folderFinalImages + imagesName + "." + filename[4:5] + "-" + filename[2:3] + "-Final.jpg"
        # print(pathWrite)
        cv2.imwrite(pathWrite, imgCropFinal)
cv2.destroyAllWindows()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>