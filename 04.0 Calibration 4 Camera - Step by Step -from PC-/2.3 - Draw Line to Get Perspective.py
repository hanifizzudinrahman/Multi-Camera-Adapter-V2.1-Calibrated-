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
# Draw Line
colorA = (0,0,255)
colorB = (0,255,0)
colorC = (255,0,0)
colorD = (0,255,255)
Thickness=2


# Camera A
blankA = np.zeros((640,480,3), dtype='uint8')
cv2.imshow('Blank', blankA)
# 4. Draw a line
cv2.line(blankA, tuple(corKriAts[0]), tuple(corKanAts[0]), colorA, Thickness)
cv2.imshow('Blank', blankA)
cv2.line(blankA, tuple(corKanAts[0]), tuple(corKanBwh[0]), colorA, Thickness)
cv2.imshow('Blank', blankA)
cv2.line(blankA, tuple(corKanBwh[0]), tuple(corKriBwh[0]), colorA, Thickness)
cv2.imshow('Blank', blankA)
cv2.destroyWindow('Blank')
cv2.line(blankA, tuple(corKriBwh[0]), tuple(corKriAts[0]), colorA, Thickness)
cv2.imshow('Camera A', blankA)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera A.jpg", blankA)

# Camera B
blankB = np.zeros((640,480,3), dtype='uint8')
cv2.imshow('Blank', blankB)
# 4. Draw a line
cv2.line(blankB, tuple(corKriAtsB[0]), tuple(corKanAtsB[0]), colorB, Thickness)
cv2.imshow('Blank', blankB)
cv2.line(blankB, tuple(corKanAtsB[0]), tuple(corKanBwhB[0]), colorB, Thickness)
cv2.imshow('Blank', blankB)
cv2.line(blankB, tuple(corKanBwhB[0]), tuple(corKriBwhB[0]), colorB, Thickness)
cv2.imshow('Blank', blankB)
cv2.destroyWindow('Blank')
cv2.line(blankB, tuple(corKriBwhB[0]), tuple(corKriAtsB[0]), colorB, Thickness)
cv2.imshow('Camera B', blankB)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera B.jpg", blankB)

# Camera C
blankC = np.zeros((640,480,3), dtype='uint8')
cv2.imshow('Blank', blankC)
# 4. Draw a line
cv2.line(blankC, tuple(corKriAtsC[0]), tuple(corKanAtsC[0]), colorC, Thickness)
cv2.imshow('Blank', blankC)
cv2.line(blankC, tuple(corKanAtsC[0]), tuple(corKanBwhC[0]), colorC, Thickness)
cv2.imshow('Blank', blankC)
cv2.line(blankC, tuple(corKanBwhC[0]), tuple(corKriBwhC[0]), colorC, Thickness)
cv2.imshow('Blank', blankC)
cv2.destroyWindow('Blank')
cv2.line(blankC, tuple(corKriBwhC[0]), tuple(corKriAtsC[0]), colorC, Thickness)
cv2.imshow('Camera C', blankC)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera C.jpg", blankC)

# Camera D
blankD = np.zeros((640,480,3), dtype='uint8')
cv2.imshow('Blank', blankD)
# 4. Draw a line
cv2.line(blankD, tuple(corKriAtsD[0]), tuple(corKanAtsD[0]), colorD, Thickness)
cv2.imshow('Blank', blankD)
cv2.line(blankD, tuple(corKanAtsD[0]), tuple(corKanBwhD[0]), colorD, Thickness)
cv2.imshow('Blank', blankD)
cv2.line(blankD, tuple(corKanBwhD[0]), tuple(corKriBwhD[0]), colorD, Thickness)
cv2.imshow('Blank', blankD)
cv2.destroyWindow('Blank')
cv2.line(blankD, tuple(corKriBwhD[0]), tuple(corKriAtsD[0]), colorD, Thickness)
cv2.imshow('Camera D', blankD)
cv2.imwrite(folderDrawLine + Rotate + "Line Perspective - Camera D.jpg", blankD)

cv2.waitKey(0)
cv2.destroyAllWindows()