import numpy as np
import cv2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderCallibration = r"_Result Calibration_\\Test " + str(numberTest) + r"\\2_Calibration-Images\\"
folderRectangleCrop = r"_Result Calibration_\\Test " + str(numberTest) + r"\\3.0_Rectangle Crop\\"

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
print("folderRectangleCrop: ", folderRectangleCrop)
print("noImage: ", noImage)
print("anotherParams: ", anotherParams)
print("imagesName: ", imagesName)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Draw Rectangle
start_point = (xMinCrop, yMinCrop)
end_point = (xMaxCrop, yMaxCrop)
color = (0, 255, 0)
thickness = 2

# Process Images
for filename in os.listdir(folderCallibration):
    if filename[:5] == imagesName:
        print(filename)
        imagePath = folderCallibration + filename
        img = cv2.imread(imagePath)
        # Rectangle
        img = cv2.rectangle(img, start_point, end_point, color, thickness)
        cv2.imshow('Original Image ' + str(filename), img)

        cv2.imwrite(folderRectangleCrop + filename[:7] + "-Rectangle.jpg", img)
        
cv2.waitKey(0)
cv2.destroyAllWindows()