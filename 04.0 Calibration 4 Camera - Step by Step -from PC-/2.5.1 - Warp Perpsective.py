import numpy as np
import cv2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderCallibration = r"_Result Calibration_\\Test " + str(numberTest) + r"\\2_Calibration-Images\\"
folderOriginalImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\1_Original-Images\\"
folderImages = r"Percobaan 2 - Atap Kamar (Vertikal)\\"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("folderCallibration: ", folderCallibration)
print("folderOriginalImages: ", folderOriginalImages)
print("folderImages: ", folderImages)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# WARP Perspective
noImage = 1
print("=> no. Image = ", noImage)
imgA = cv2.imread(folderOriginalImages + folderImages + Rotate + "A_" + str(noImage) + ".jpg")

cv2.imshow('Camera A - Perspective', imgA)

# CAMERA A - B
imgB = cv2.imread(folderOriginalImages + folderImages + Rotate + "B_" + str(noImage) + ".jpg")
cv2.imshow('Camera B - Perspective', imgB)
# Coordinate A
pts1 = np.float32([corKriAts[0],corKanAts[0],corKriBwh[0],corKanBwh[0]])
# Coordinate B
pts2 = np.float32([corKriAtsB[0],corKanAtsB[0],corKriBwhB[0],corKanBwhB[0]])
matrix = cv2.getPerspectiveTransform(pts2,pts1)
imgOutputB = cv2.warpPerspective(imgB,matrix,(480,640))

# CAMERA A - C
imgC = cv2.imread(folderOriginalImages + folderImages + Rotate + "C_" + str(noImage) + ".jpg")
# Coordinate A
pts1 = np.float32([corKriAts[0],corKanAts[0],corKriBwh[0],corKanBwh[0]])
# Coordinate C
pts2 = np.float32([corKriAtsC[0],corKanAtsC[0],corKriBwhC[0],corKanBwhC[0]])
matrix = cv2.getPerspectiveTransform(pts2,pts1)
imgOutputC = cv2.warpPerspective(imgC,matrix,(480,640))

# CAMERA A - D
imgD = cv2.imread(folderOriginalImages + folderImages + Rotate + "D_" + str(noImage) + ".jpg")
# Coordinate A
pts1 = np.float32([corKriAts[0],corKanAts[0],corKriBwh[0],corKanBwh[0]])
# Coordinate D
pts2 = np.float32([corKriAtsD[0],corKanAtsD[0],corKriBwhD[0],corKanBwhD[0]])
matrix = cv2.getPerspectiveTransform(pts2,pts1)
imgOutputD = cv2.warpPerspective(imgD,matrix,(480,640))

cv2.imshow('Camera A - Perspective', imgA)
cv2.imshow('Camera B - Perspective', imgOutputB)
cv2.imshow('Camera C - Perspective', imgOutputC)
cv2.imshow('Camera D - Perspective', imgOutputD)
#==== W R I T E
anotherParams = 1
cv2.imwrite(folderCallibration + Rotate + str(noImage) + "." + str(anotherParams) + "-A.jpg", imgA)
cv2.imwrite(folderCallibration + Rotate + str(noImage) + "." + str(anotherParams) + "-B.jpg", imgOutputB)
cv2.imwrite(folderCallibration + Rotate + str(noImage) + "." + str(anotherParams) + "-C.jpg", imgOutputC)
cv2.imwrite(folderCallibration + Rotate + str(noImage) + "." + str(anotherParams) + "-D.jpg", imgOutputD)

cv2.waitKey(0)
cv2.destroyAllWindows()