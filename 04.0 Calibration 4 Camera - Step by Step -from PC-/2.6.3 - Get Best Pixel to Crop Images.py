# Get Best Pixel to Crop Images

print("Get Best Pixel to Crop Images")
print("="*50)
# Start (Kiri Atas)
#== Longest X
if CropKriAts[0] >= CropKriBwh[0]:
    xMinCrop = CropKriAts[0]
else:
    xMinCrop = CropKriBwh[0]
#==  Longest Y
if CropKriAts[1] >= CropKanAts[1]:
    yMinCrop = CropKriAts[1]
else:
    yMinCrop = CropKanAts[1]

# End (Kanan Bawah)
#====== Short X
if CropKanAts[0] <= CropKanBwh[0]:
    xMaxCrop = CropKanAts[0]
else:
    xMaxCrop = CropKanBwh[0]
#====== Short Y
if CropKriBwh[1] <= CropKanBwh[1]:
    yMaxCrop = CropKriBwh[1]
else:
    yMaxCrop = CropKanBwh[1]
pixelXCrop = xMaxCrop - xMinCrop
pixelYCrop = yMaxCrop - yMinCrop
print("Coordinate Start = (", xMinCrop, yMinCrop, ") and End = (", xMaxCrop, yMaxCrop, ")")
print("Pixel = ", pixelXCrop, "x", pixelYCrop)
print()