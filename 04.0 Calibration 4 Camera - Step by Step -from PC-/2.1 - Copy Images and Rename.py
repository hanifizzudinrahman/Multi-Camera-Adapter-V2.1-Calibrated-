# Copy Images and Rename
import os 
from shutil import copy2

numberTest = 1
Rotate = "R."    # if no Ratate, change to ""
folderPercobaan = r"Percobaan 2 - Atap Kamar (Vertikal)\\"
# "Percobaan 2 - Atap Kamar (Vertikal)\Final\\""
# "Percobaan 1 - Depan Kamar (Horizontal)\\"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("Number Test: ", numberTest)
if Rotate == "R.":
    print("Rotate True")
else:
    print("Rotate False")
print("Folder Percobaan: ", folderPercobaan)
print(">"*50)
print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Function to rename multiple files 
def main(): 
    a,b,c,d = 0,0,0,0

    #srcPath = folderPercobaan
    srcPath = folderPercobaan + r"Final\\"                  # "Percobaan 2 - Atap Kamar (Vertikal)\Final\\""

    #dstPath = folderPercobaan + r"_Result_\\"
    dstPath = folderPercobaan + r"Final\\_Result_\\"

    dstPath2 = r"_Result Calibration_\Test " + str(numberTest) + "\\1_Original-Images\\" + folderPercobaan
      
    for filename in os.listdir(srcPath): 
        # Copy Original Images
        oriSrc = srcPath + filename
        if filename[:10] == Rotate +"Camera_A":
            newFilename = Rotate + "A_"
            a += 1
            newDst = dstPath + newFilename + str(a) + ".jpg"
            newDst2 = dstPath2 + newFilename + str(a) + ".jpg"
        elif filename[:10] == Rotate + "Camera_B":
            newFilename = Rotate + "B_"
            b += 1
            newDst = dstPath + newFilename + str(b) + ".jpg"
            newDst2 = dstPath2 + newFilename + str(b) + ".jpg"
        elif filename[:10] == Rotate + "Camera_C":
            newFilename = Rotate + "C_"
            c += 1
            newDst = dstPath + newFilename + str(c) + ".jpg"
            newDst2 = dstPath2 + newFilename + str(c) + ".jpg"
        elif filename[:10] == Rotate + "Camera_D":
            newFilename = Rotate + "D_"
            d += 1
            newDst = dstPath + newFilename + str(d) + ".jpg"
            newDst2 = dstPath2 + newFilename + str(d) + ".jpg"

        # Copy Original Images
        print("oriSrc: ", oriSrc)
        print("newDst: ", newDst)
        print("newDst2: ", newDst2)
        print()
        copy2(oriSrc, newDst)
        copy2(oriSrc, newDst2)
          
        # rename() function will 
        # rename all the files 
        #os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()