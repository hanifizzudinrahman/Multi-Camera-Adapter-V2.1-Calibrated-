# Crop

import numpy as np
import cv2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderCallibration = r"_Result Calibration_\\Test " + str(numberTest) + r"\\2_Calibration-Images\\"
folderCropImages = r"_Result Calibration_\\Test " + str(numberTest) + r"\\3_Crop-Images (Final)\\"

noImage = 1
anotherParams = 1
imagesName = Rotate + str(noImage) + "." + str(anotherParams)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("folderCallibration: ", folderCallibration)
print("folderCropImages: ", folderCropImages)
print("noImage: ", noImage)
print("anotherParams: ", anotherParams)
print("imagesName: ", imagesName)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Crop Rectangle
start_point = (xMinCrop, yMinCrop)
end_point = (xMaxCrop, yMaxCrop)

# Process Images
for filename in os.listdir(folderCallibration):
    if filename[:5] == imagesName:
        print(filename)
        imagePath = folderCallibration + filename
        img = cv2.imread(imagePath)
        img = img[yMinCrop:yMaxCrop+1, xMinCrop:xMaxCrop+1]
        cv2.imshow('Original Image ' + str(filename), img)
        # Crop

        cv2.imwrite(folderCropImages + filename[:7] + "-Final.jpg", img)
        
cv2.waitKey(0)
cv2.destroyAllWindows()