# Get Location in New Images
import cv2
import numpy as np

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderPercobaan = r"Percobaan 2 - Atap Kamar (Vertikal)\\"
# "Percobaan 2 - Atap Kamar (Vertikal)\Final\\"
# "Percobaan 1 - Depan Kamar (Horizontal)\\"

# resultPath = folderPercobaan + r"_Result_\\"
resultPath = folderPercobaan + r"Final\_Result_\\"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("Folder Percobaan (resultPath): ", resultPath)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def mousePoints (event, x, y, flags, params):
    global counter
    #print('-event=', event,' -x,y:',x,y,'\t-flags:', flags, ' -params:', params)
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

        circles[counter] = x,y
        counter = counter + 1
        #print(circles)

counter = 0
circles = np.zeros((4,2), np.int)

# Camera A Best Coordinate
corKriAts = np.zeros((1,2), np.int)
corKanAts = np.zeros((1,2), np.int)
corKanBwh = np.zeros((1,2), np.int)
corKriBwh = np.zeros((1,2), np.int)

# Camera B Best Coordinate (Relate on Camera A)
corKriAtsB = np.zeros((1,2), np.int)
corKanAtsB = np.zeros((1,2), np.int)
corKanBwhB = np.zeros((1,2), np.int)
corKriBwhB = np.zeros((1,2), np.int)
# Camera C Best Coordinate (Relate on Camera A)
corKriAtsC = np.zeros((1,2), np.int)
corKanAtsC = np.zeros((1,2), np.int)
corKanBwhC = np.zeros((1,2), np.int)
corKriBwhC = np.zeros((1,2), np.int)
# Camera D Best Coordinate (Relate on Camera A)
corKriAtsD = np.zeros((1,2), np.int)
corKanAtsD = np.zeros((1,2), np.int)
corKanBwhD = np.zeros((1,2), np.int)
corKriBwhD = np.zeros((1,2), np.int)

# Process Images
#resultPath = r"Percobaan 2 - Atap Kamar (Vertikal)\Final\_Result_\\"
for filename in os.listdir(resultPath):
    print()
    print(filename)
    imagePath = resultPath + filename
    img = cv2.imread(imagePath)

    while True:
        for x in range(0,4):
            cv2.circle(img,(circles[x][0], circles[x][1]), 3, (0,255,0), cv2.FILLED)
        
        cv2.imshow('Original Image ' + str(filename), img)
        cv2.setMouseCallback('Original Image ' + str(filename), mousePoints)    

        if (cv2.waitKey(1) & 0xFF == ord('q')) or counter == 4:
            break
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    counter = 0

    # Find Best Coordinate
    if filename[:3] == Rotate + "A":
        # Camera A

        # Kiri Atas (1)
        simpanX1A = circles[0][0]
        simpanY1A = circles[0][1]
        if simpanX1A <= corKriAts[0][0] or corKriAts[0][0] == 0:
            corKriAts[0][0] = simpanX1A
            # Save Name
            saveNameX1 = filename[4:5]
        if simpanY1A <= corKriAts[0][1] or corKriAts[0][1] == 0:
            corKriAts[0][1] = simpanY1A
            # Save Name
            saveNameY1 = filename[4:5]
        #print('>> x1,y1 = ', corKriAts[0][0], corKriAts[0][1], " , name: ", saveNameX1, saveNameY1)

        # Kanan Atas (2)
        simpanX2A = circles[1][0]
        simpanY2A = circles[1][1]
        if simpanX2A >= corKanAts[0][0] or corKanAts[0][0] == 0:
            corKanAts[0][0] = simpanX2A
            # Save Name
            saveNameX2 = filename[4:5]
        if simpanY2A <= corKanAts[0][1] or corKanAts[0][1] == 0:
            corKanAts[0][1] = simpanY2A
            # Save Name
            saveNameY2 = filename[4:5]
        #print('>> x2,y2 = ', corKanAts[0][0], corKanAts[0][1], " , name: ", saveNameX2, saveNameY2)

        # Kanan Bawah (3)
        simpanX3A = circles[2][0]
        simpanY3A = circles[2][1]
        if simpanX3A >= corKanBwh[0][0] or corKanBwh[0][0] == 0:
            corKanBwh[0][0] = simpanX3A
            # Save Name
            saveNameX3 = filename[4:5]
        if simpanY3A >= corKanBwh[0][1] or corKanBwh[0][1] == 0:
            corKanBwh[0][1] = simpanY3A
            # Save Name
            saveNameY3 = filename[4:5]
        #print('>> x3,y3 = ', corKanBwh[0][0], corKanBwh[0][1], " , name: ", saveNameX3, saveNameY3) 

        # Kiri Bawah (4)
        simpanX4A = circles[3][0]
        simpanY4A = circles[3][1]
        if simpanX4A <= corKriBwh[0][0] or corKriBwh[0][0] == 0:
            corKriBwh[0][0] = simpanX4A
            # Save Name
            saveNameX4 = filename[4:5]
        if simpanY4A >= corKriBwh[0][1] or corKriBwh[0][1] == 0:
            corKriBwh[0][1] = simpanY4A
            # Save Name
            saveNameY4 = filename[4:5]
        #print('>> x4,y4 = ', corKriBwh[0][0], corKriBwh[0][1], " , name: ", saveNameX4, saveNameY4) 

    # Find Best Coordinate (Relate on Coordinate A) "name"
    # Coordinate Camera B
    if filename[:3] == Rotate + "B":
        # Get Coordinate X
        if filename[4:5] == saveNameX1:
            corKriAtsB[0][0] = circles[0][0]
        if filename[4:5] == saveNameX2:
            corKanAtsB[0][0] = circles[1][0]
        if filename[4:5] == saveNameX3:
            corKanBwhB[0][0] = circles[2][0]
        if filename[4:5] == saveNameX4:
            corKriBwhB[0][0] = circles[3][0]

        # Get Coordinate Y
        if filename[4:5] == saveNameY1:
            corKriAtsB[0][1] = circles[0][1]
        if filename[4:5] == saveNameY2:
            corKanAtsB[0][1] = circles[1][1]
        if filename[4:5] == saveNameY3:
            corKanBwhB[0][1] = circles[2][1]
        if filename[4:5] == saveNameY4:
            corKriBwhB[0][1] = circles[3][1]
        
        # Final Coordinate Camera B
        """
        print('>> x1B,y1B = ', corKriAtsB[0][0], corKriAtsB[0][1])
        print('>> x2B,y2B = ', corKanAtsB[0][0], corKanAtsB[0][1])
        print('>> x3B,y3B = ', corKanBwhB[0][0], corKanBwhB[0][1])
        print('>> x4B,y4B = ', corKriBwhB[0][0], corKriBwhB[0][1])
        """

    # Coordinate Camera C
    if filename[:3] == Rotate + "C":
        # Get Coordinate X
        if filename[4:5] == saveNameX1:
            corKriAtsC[0][0] = circles[0][0]
        if filename[4:5] == saveNameX2:
            corKanAtsC[0][0] = circles[1][0]
        if filename[4:5] == saveNameX3:
            corKanBwhC[0][0] = circles[2][0]
        if filename[4:5] == saveNameX4:
            corKriBwhC[0][0] = circles[3][0]

        # Get Coordinate Y
        if filename[4:5] == saveNameY1:
            corKriAtsC[0][1] = circles[0][1]
        if filename[4:5] == saveNameY2:
            corKanAtsC[0][1] = circles[1][1]
        if filename[4:5] == saveNameY3:
            corKanBwhC[0][1] = circles[2][1]
        if filename[4:5] == saveNameY4:
            corKriBwhC[0][1] = circles[3][1]
        
        # Final Coordinate Camera C
        """
        print('>> x1C,y1C = ', corKriAtsC[0][0], corKriAtsC[0][1])
        print('>> x2C,y2C = ', corKanAtsC[0][0], corKanAtsC[0][1])
        print('>> x3C,y3C = ', corKanBwhC[0][0], corKanBwhC[0][1])
        print('>> x4C,y4C = ', corKriBwhC[0][0], corKriBwhC[0][1])
        """

    # Coordinate Camera D
    if filename[:3] == Rotate + "D":
        # Get Coordinate X
        if filename[4:5] == saveNameX1:
            corKriAtsD[0][0] = circles[0][0]
        if filename[4:5] == saveNameX2:
            corKanAtsD[0][0] = circles[1][0]
        if filename[4:5] == saveNameX3:
            corKanBwhD[0][0] = circles[2][0]
        if filename[4:5] == saveNameX4:
            corKriBwhD[0][0] = circles[3][0]

        # Get Coordinate Y
        if filename[4:5] == saveNameY1:
            corKriAtsD[0][1] = circles[0][1]
        if filename[4:5] == saveNameY2:
            corKanAtsD[0][1] = circles[1][1]
        if filename[4:5] == saveNameY3:
            corKanBwhD[0][1] = circles[2][1]
        if filename[4:5] == saveNameY4:
            corKriBwhD[0][1] = circles[3][1]
        
        # Final Coordinate Camera B
        """
        print('>> x1D,y1D = ', corKriAtsD[0][0], corKriAtsD[0][1])
        print('>> x2D,y2D = ', corKanAtsD[0][0], corKanAtsD[0][1])
        print('>> x3D,y3D = ', corKanBwhD[0][0], corKanBwhD[0][1])
        print('>> x4D,y4D = ', corKriBwhD[0][0], corKriBwhD[0][1])
        """

#====================================================================================
# FINAL
print("FINAL Best Coordinate")
print("~"*50)
print()

# Coordinate Kiri Atas
print("Coordinate Kiri Atas")
print("Take from Camera A, X1 = ", saveNameX1, " and Y1 = ", saveNameY1)
print("=-"*25)
print('x1A,y1A = ', corKriAts)
print('x1B,y1B = ', corKriAtsB)
print('x1C,y1C = ', corKriAtsC)
print('x1D,y1D = ', corKriAtsD)
print()

# Coordinate Kanan Atas
print("Coordinate Kanan Atas")
print("Take from Camera A, X2 = ", saveNameX2, " and Y2 = ", saveNameY2)
print("=-"*25)
print('x2A,y2A = ', corKanAts)
print('x2B,y2B = ', corKanAtsB)
print('x2C,y2C = ', corKanAtsC)
print('x2D,y2D = ', corKanAtsD)
print()

# Coordinate Kanan Bawah
print("Coordinate Kanan Bawah")
print("Take from Camera A, X3 = ", saveNameX3, " and Y3 = ", saveNameY3)
print("=-"*25)
print('x3A,y3A = ', corKanBwh)
print('x3B,y3B = ', corKanBwhB)
print('x3C,y3C = ', corKanBwhC)
print('x3D,y3D = ', corKanBwhD)
print()

# Coordinate Kiri Bawah
print("Coordinate Kiri Bawah")
print("Take from Camera A, X4 = ", saveNameX4, " and Y4 = ", saveNameY4)
print("=-"*25)
print('x4A,y4A = ', corKriBwh)
print('x4B,y4B = ', corKriBwhB)
print('x4C,y4C = ', corKriBwhC)
print('x4D,y4D = ', corKriBwhD)
print()