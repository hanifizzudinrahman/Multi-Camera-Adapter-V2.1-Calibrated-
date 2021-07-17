# Substraction grayscale

import numpy as np
import cv2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderCropImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\3_Crop-Images (Final)\\"
folderSubstractionImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\4_Substraction-TestImages\\"

noImage = 1
anotherParams = 1
imagesName = Rotate + str(noImage) + "." + str(anotherParams)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("folderSubstractionImages: ", folderSubstractionImages)
print("folderCropImages: ", folderCropImages)
print("noImage: ", noImage)
print("anotherParams: ", anotherParams)
print("imagesName: ", imagesName)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Process Images
for filename in os.listdir(folderCropImages):
    if filename[:5] == imagesName:
        print(filename)
        imagePath = folderCropImages + filename
        if filename[6:7] == "A":
            imgSubsA = cv2.imread(imagePath, 0)
            cv2.imshow('Original Image ' + str(filename), imgSubsA)
        elif filename[6:7] == "B":
            imgSubsB = cv2.imread(imagePath, 0)
            cv2.imshow('Original Image ' + str(filename), imgSubsB)
        elif filename[6:7] == "C":
            imgSubsC = cv2.imread(imagePath, 0)
            cv2.imshow('Original Image ' + str(filename), imgSubsC)
        elif filename[6:7] == "D":
            imgSubsD = cv2.imread(imagePath, 0)
            cv2.imshow('Original Image ' + str(filename), imgSubsD)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Substraction Images A
A_A = imgSubsA - imgSubsA
A_B = imgSubsA - imgSubsB
A_C = imgSubsA - imgSubsC
A_D = imgSubsA - imgSubsD

cv2.imshow("A-A", A_A)
cv2.imshow("A-B", A_B)
cv2.imshow("A-C", A_C)
cv2.imshow("A-D", A_D)
cv2.imwrite(folderSubstractionImages + filename[:6] + "A-A-Subs.jpg", A_A)
cv2.imwrite(folderSubstractionImages + filename[:6] + "A-B-Subs.jpg", A_B)
cv2.imwrite(folderSubstractionImages + filename[:6] + "A-C-Subs.jpg", A_C)
cv2.imwrite(folderSubstractionImages + filename[:6] + "A-D-Subs.jpg", A_D)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Substraction Images B
B_A = imgSubsB - imgSubsA
B_B = imgSubsB - imgSubsB
B_C = imgSubsB - imgSubsC
B_D = imgSubsB - imgSubsD

cv2.imshow("B-A", B_A)
cv2.imshow("B-B", B_B)
cv2.imshow("B-C", B_C)
cv2.imshow("B-D", B_D)
cv2.imwrite(folderSubstractionImages + filename[:6] + "B-A-Subs.jpg", B_A)
cv2.imwrite(folderSubstractionImages + filename[:6] + "B-B-Subs.jpg", B_B)
cv2.imwrite(folderSubstractionImages + filename[:6] + "B-C-Subs.jpg", B_C)
cv2.imwrite(folderSubstractionImages + filename[:6] + "B-D-Subs.jpg", B_D)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Substraction Images C
C_A = imgSubsC - imgSubsA
C_B = imgSubsC - imgSubsB
C_C = imgSubsC - imgSubsC
C_D = imgSubsC - imgSubsD

cv2.imshow("C-A", C_A)
cv2.imshow("C-B", C_B)
cv2.imshow("C-C", C_C)
cv2.imshow("C-D", C_D)
cv2.imwrite(folderSubstractionImages + filename[:6] + "C-A-Subs.jpg", C_A)
cv2.imwrite(folderSubstractionImages + filename[:6] + "C-B-Subs.jpg", C_B)
cv2.imwrite(folderSubstractionImages + filename[:6] + "C-C-Subs.jpg", C_C)
cv2.imwrite(folderSubstractionImages + filename[:6] + "C-D-Subs.jpg", C_D)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Substraction Images D
D_A = imgSubsD - imgSubsA
D_B = imgSubsD - imgSubsB
D_C = imgSubsD - imgSubsC
D_D = imgSubsD - imgSubsD

cv2.imshow("D-A", D_A)
cv2.imshow("D-B", D_B)
cv2.imshow("D-C", D_C)
cv2.imshow("D-D", D_D)
cv2.imwrite(folderSubstractionImages + filename[:6] + "D-A-Subs.jpg", D_A)
cv2.imwrite(folderSubstractionImages + filename[:6] + "D-B-Subs.jpg", D_B)
cv2.imwrite(folderSubstractionImages + filename[:6] + "D-C-Subs.jpg", D_C)
cv2.imwrite(folderSubstractionImages + filename[:6] + "D-D-Subs.jpg", D_D)
cv2.waitKey(0)
cv2.destroyAllWindows()