# Get Location in New Images
import cv2
import numpy as np

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderCallibration = r"_Result Calibration_\\Test " + str(numberTest) + r"\\2_Calibration-Images\\"
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
print("noImage: ", noImage)
print("anotherParams: ", anotherParams)
print("imagesName: ", imagesName)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def mousePoints (event, x, y, flags, params):
    global counter
    global circles
    #print('-event=', event,' -x,y:',x,y,'\t-flags:', flags, ' -params:', params)
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

        circles[counter] = x,y
        counter = counter + 1
        #print(circles)

counter = 0
circles = np.zeros((4,2), np.int)

# Camera A Best Coordinate
corKriAtsCrop = np.zeros((2), np.int)
corKanAtsCrop = np.zeros((2), np.int)
corKanBwhCrop = np.zeros((2), np.int)
corKriBwhCrop = np.zeros((2), np.int)

# Camera B Best Coordinate (Relate on Camera A)
corKriAtsCropB = np.zeros((2), np.int)
corKanAtsCropB = np.zeros((2), np.int)
corKanBwhCropB = np.zeros((2), np.int)
corKriBwhCropB = np.zeros((2), np.int)
# Camera C Best Coordinate (Relate on Camera A)
corKriAtsCropC = np.zeros((2), np.int)
corKanAtsCropC = np.zeros((2), np.int)
corKanBwhCropC = np.zeros((2), np.int)
corKriBwhCropC = np.zeros((2), np.int)
# Camera D Best Coordinate (Relate on Camera A)
corKriAtsCropD = np.zeros((2), np.int)
corKanAtsCropD = np.zeros((2), np.int)
corKanBwhCropD = np.zeros((2), np.int)
corKriBwhCropD = np.zeros((2), np.int)

# Process Images
# resultPath = r"_Result Calibration_\Test 1\\"
#imagesName = R + str(noImage) + "." + str(anotherParams)
for filename in os.listdir(folderCallibration):
    if filename[:5] == imagesName:
        print(filename)
        imagePath = folderCallibration + filename
        img = cv2.imread(imagePath)

        while True:
            for x in range(0,4):
                cv2.circle(img,(circles[x][0], circles[x][1]), 3, (0,255,0), cv2.FILLED)
            
            cv2.imshow('Original Image ' + str(filename), img)
            cv2.setMouseCallback('Original Image ' + str(filename), mousePoints)    

            if (cv2.waitKey(1) & 0xFF == ord('q')) or counter == 4:
                break
            cv2.waitKey(1)

        # Get Coordinate Camera B
        if filename[5:7] == "-B":
            corKriAtsCropB = circles[[0]]
            corKanAtsCropB = circles[[1]]
            corKanBwhCropB = circles[[2]]
            corKriBwhCropB = circles[[3]]

        # Get Coordinate Camera C
        if filename[5:7] == "-C":
            corKriAtsCropC = circles[[0]]
            corKanAtsCropC = circles[[1]]
            corKanBwhCropC = circles[[2]]
            corKriBwhCropC = circles[[3]]

        # Get Coordinate Camera D
        if filename[5:7] == "-D":
            corKriAtsCropD = circles[[0]]
            corKanAtsCropD = circles[[1]]
            corKanBwhCropD = circles[[2]]
            corKriBwhCropD = circles[[3]]
    cv2.destroyAllWindows()
    counter = 0

print()
# Crop Coordinate
CropKriAts = np.zeros((2), np.int)
CropKanAts = np.zeros((2), np.int)
CropKanBwh = np.zeros((2), np.int)
CropKriBwh = np.zeros((2), np.int)

# ============== Optimal Crop Kiri Atas (X++, Y++)
print(corKriAtsCropB, corKriAtsCropC, corKriAtsCropD)
for i in range (0,1+1):
    # i=0 => X Coordinate, i=1 => Y Coordinate
    if corKriAtsCropB[0][i] >= corKriAtsCropC[0][i] and corKriAtsCropB[0][i] >= corKriAtsCropD[0][i]:
        CropKriAts[i] = corKriAtsCropB[0][i]
    elif corKriAtsCropC[0][i] >= corKriAtsCropB[0][i] and corKriAtsCropC[0][i] >= corKriAtsCropD[0][i]:
        CropKriAts[i] = corKriAtsCropC[0][i]
    elif corKriAtsCropD[0][i] >= corKriAtsCropB[0][i] and corKriAtsCropD[0][i] >= corKriAtsCropC[0][i]:
        CropKriAts[i] = corKriAtsCropD[0][i]
print("CropKriAts: ", CropKriAts)
print()

# ============== Optimal Crop Kanan Atas (X--, Y++)
print(corKanAtsCropB, corKanAtsCropC, corKanAtsCropD)
for i in range (0,1+1):
    # i=0 => X Coordinate, i=1 => Y Coordinate
    if i == 0:
        if corKanAtsCropB[0][i] <= corKanAtsCropC[0][i] and corKanAtsCropB[0][i] <= corKanAtsCropD[0][i]:
            CropKanAts[i] = corKanAtsCropB[0][i]
        elif corKanAtsCropC[0][i] <= corKanAtsCropB[0][i] and corKanAtsCropC[0][i] <= corKanAtsCropD[0][i]:
            CropKanAts[i] = corKanAtsCropC[0][i]
        elif corKanAtsCropD[0][i] <= corKanAtsCropB[0][i] and corKanAtsCropD[0][i] <= corKanAtsCropC[0][i]:
            CropKanAts[i] = corKanAtsCropD[0][i]
    else:
        if corKanAtsCropB[0][i] >= corKanAtsCropC[0][i] and corKanAtsCropB[0][i] >= corKanAtsCropD[0][i]:
            CropKanAts[i] = corKanAtsCropB[0][i]
        elif corKanAtsCropC[0][i] >= corKanAtsCropB[0][i] and corKanAtsCropC[0][i] >= corKanAtsCropD[0][i]:
            CropKanAts[i] = corKanAtsCropC[0][i]
        elif corKanAtsCropD[0][i] >= corKanAtsCropB[0][i] and corKanAtsCropD[0][i] >= corKanAtsCropC[0][i]:
            CropKanAts[i] = corKanAtsCropD[0][i]
print("CropKanAts: ", CropKanAts)
print()

# ============== Optimal Crop Kanan Bawah (X--, Y--)
print(corKanBwhCropB, corKanBwhCropC, corKanBwhCropD)
for i in range (0,1+1):
    # i=0 => X Coordinate, i=1 => Y Coordinate
    if corKanBwhCropB[0][i] <= corKanBwhCropC[0][i] and corKanBwhCropB[0][i] <= corKanBwhCropD[0][i]:
        CropKanBwh[i] = corKanBwhCropB[0][i]
    elif corKanBwhCropC[0][i] <= corKanBwhCropB[0][i] and corKanBwhCropC[0][i] <= corKanBwhCropD[0][i]:
        CropKanBwh[i] = corKanBwhCropC[0][i]
    elif corKanBwhCropD[0][i] <= corKanBwhCropB[0][i] and corKanBwhCropD[0][i] <= corKanBwhCropC[0][i]:
        CropKanBwh[i] = corKanBwhCropD[0][i]
print("CropKanBwh: ", CropKanBwh)
print()

# ============== Optimal Crop Kiri Bawah (X++, Y--)
print(corKriBwhCropB, corKriBwhCropC, corKriBwhCropD)
for i in range (0,1+1):
    # i=0 => X Coordinate, i=1 => Y Coordinate
    if i == 1:
        if corKriBwhCropB[0][i] <= corKriBwhCropC[0][i] and corKriBwhCropB[0][i] <= corKriBwhCropD[0][i]:
            CropKriBwh[i] = corKriBwhCropB[0][i]
        elif corKriBwhCropC[0][i]<= corKriBwhCropB[0][i] and corKriBwhCropC[0][i] <= corKriBwhCropD[0][i]:
            CropKriBwh[i] = corKriBwhCropC[0][i]
        elif corKriBwhCropD[0][i] <= corKriBwhCropB[0][i] and corKriBwhCropD[0][i] <= corKriBwhCropC[0][i]:
            CropKriBwh[i] = corKriBwhCropD[0][i]
    else:
        if corKriBwhCropB[0][i] >= corKriBwhCropC[0][i] and corKriBwhCropB[0][i] >= corKriBwhCropD[0][i]:
            CropKriBwh[i] = corKriBwhCropB[0][i]
        elif corKriBwhCropC[0][i] >= corKriBwhCropB[0][i] and corKriBwhCropC[0][i] >= corKriBwhCropD[0][i]:
            CropKriBwh[i] = corKriBwhCropC[0][i]
        elif corKriBwhCropD[0][i] >= corKriBwhCropB[0][i] and corKriBwhCropD[0][i] >= corKriBwhCropC[0][i]:
            CropKriBwh[i] = corKriBwhCropD[0][i]
print("CropKriBwh: ", CropKriBwh)
print()