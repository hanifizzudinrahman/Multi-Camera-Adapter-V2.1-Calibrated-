# Get Best Pixel

import numpy as np
import cv2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderDrawLine = r"_Result Calibration_\Test " + str(numberTest) + "\\2.0_Line Callibration\\"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("Folder folderDrawLine: ", folderDrawLine)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Camera A
print("Camera A Pixel Rectangle")
print("="*50)
#== Shortest X
if corKriAts[0][0] <= corKriBwh[0][0]:
    xMinA = corKriAts[0][0]
else:
    xMinA = corKriBwh[0][0]
#==  Shortest Y
if corKriAts[0][1] <= corKanAts[0][1]:
    yMinA = corKriAts[0][1]
else:
    yMinA = corKanAts[0][1]
#====== Longest X
if corKanAts[0][0] >= corKanBwh[0][0]:
    xMaxA = corKanAts[0][0]
else:
    xMaxA = corKanBwh[0][0]
#====== Longest Y
if corKriBwh[0][1] >= corKanBwh[0][1]:
    yMaxA = corKriBwh[0][1]
else:
    yMaxA = corKanBwh[0][1]
pixelXA = xMaxA - xMinA
pixelYA = yMaxA - yMinA
print("Coordinate Shortest A = (", xMinA, yMinA, ") and Longest = (", xMaxA, yMaxA, ")")
print("Pixel = ", pixelXA, "x", pixelYA)
print()

# Camera B
print("Camera B Pixel Rectangle")
print("="*50)
#== Shortest X
if corKriAtsB[0][0] <= corKriBwhB[0][0]:
    xMinB = corKriAtsB[0][0]
else:
    xMinB = corKriBwhB[0][0]
#==  Shortest Y
if corKriAtsB[0][1] <= corKanAtsB[0][1]:
    yMinB = corKriAtsB[0][1]
else:
    yMinB = corKanAtsB[0][1]
#====== Longest X
if corKanAtsB[0][0] >= corKanBwhB[0][0]:
    xMaxB = corKanAtsB[0][0]
else:
    xMaxB = corKanBwhB[0][0]
#====== Longest Y
if corKriBwhB[0][1] >= corKanBwhB[0][1]:
    yMaxB = corKriBwhB[0][1]
else:
    yMaxB = corKanBwhB[0][1]
pixelXB = xMaxB - xMinB
pixelYB = yMaxB - yMinB
print("Coordinate Shortest B = (", xMinB, yMinB, ") and Longest = (", xMaxB, yMaxB, ")")
print("Pixel = ", pixelXB, "x", pixelYB)
print()

# Camera C
print("Camera C Pixel Rectangle")
print("="*50)
#== Shortest X
if corKriAtsC[0][0] <= corKriBwhC[0][0]:
    xMinC = corKriAtsC[0][0]
else:
    xMinC = corKriBwhC[0][0]
#==  Shortest Y
if corKriAtsC[0][1] <= corKanAtsC[0][1]:
    yMinC = corKriAtsC[0][1]
else:
    yMinC = corKanAtsC[0][1]
#====== Longest X
if corKanAtsC[0][0] >= corKanBwhC[0][0]:
    xMaxC = corKanAtsC[0][0]
else:
    xMaxC = corKanBwhC[0][0]
#====== Longest Y
if corKriBwhC[0][1] >= corKanBwhC[0][1]:
    yMaxC = corKriBwhC[0][1]
else:
    yMaxC = corKanBwhC[0][1]
pixelXC = xMaxC - xMinC
pixelYC = yMaxC - yMinC
print("Coordinate Shortest C = (", xMinC, yMinC, ") and Longest = (", xMaxC, yMaxC, ")")
print("Pixel = ", pixelXC, "x", pixelYC)
print()

# Camera D
print("Camera D Pixel Rectangle")
print("="*50)
#== Shortest X
if corKriAtsD[0][0] <= corKriBwhD[0][0]:
    xMinD = corKriAtsD[0][0]
else:
    xMinD = corKriBwhD[0][0]
#==  Shortest Y
if corKriAtsD[0][1] <= corKanAtsD[0][1]:
    yMinD = corKriAtsD[0][1]
else:
    yMinD = corKanAtsD[0][1]
#====== Longest X
if corKanAtsD[0][0] >= corKanBwhD[0][0]:
    xMaxD = corKanAtsD[0][0]
else:
    xMaxD = corKanBwhD[0][0]
#====== Longest Y
if corKriBwhD[0][1] >= corKanBwhD[0][1]:
    yMaxD = corKriBwhD[0][1]
else:
    yMaxD = corKanBwhD[0][1]
pixelXD = xMaxD - xMinD
pixelYD = yMaxD - yMinD
print("Coordinate Shortest D = (", xMinD, yMinD, ") and Longest = (", xMaxD, yMaxD, ")")
print("Pixel = ", pixelXD, "x", pixelYD)
print()

# Write Rectangle
lineA = cv2.imread(folderDrawLine + "R.Line Perspective - Camera A.jpg")
lineB = cv2.imread(folderDrawLine + "R.Line Perspective - Camera B.jpg")
lineC = cv2.imread(folderDrawLine + "R.Line Perspective - Camera C.jpg")
lineD = cv2.imread(folderDrawLine + "R.Line Perspective - Camera D.jpg")
colorRectangle = (255, 255, 255)
ThicknessRect = 1

# Rectangle A
cv2.imshow('Rectangle A', lineA)
cv2.rectangle(lineA, (xMinA, yMinA), (xMaxA, yMaxA), colorRectangle, ThicknessRect)
cv2.imshow('Rectangle A', lineA)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera A (Rectangle).jpg", lineA)
# Rectangle B
cv2.imshow('Rectangle B', lineB)
cv2.rectangle(lineB, (xMinB, yMinB), (xMaxB, yMaxB), colorRectangle, ThicknessRect)
cv2.imshow('Rectangle B', lineB)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera B (Rectangle).jpg", lineB)
# Rectangle C
cv2.imshow('Rectangle C', lineC)
cv2.rectangle(lineC, (xMinC, yMinC), (xMaxC, yMaxC), colorRectangle, ThicknessRect)
cv2.imshow('Rectangle C', lineC)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera C (Rectangle).jpg", lineC)
# Rectangle D
cv2.imshow('Rectangle D', lineD)
cv2.rectangle(lineD, (xMinD, yMinD), (xMaxD, yMaxD), colorRectangle, ThicknessRect)
cv2.imshow('Rectangle D', lineD)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera D (Rectangle).jpg", lineD)

cv2.waitKey(0)
cv2.destroyAllWindows()