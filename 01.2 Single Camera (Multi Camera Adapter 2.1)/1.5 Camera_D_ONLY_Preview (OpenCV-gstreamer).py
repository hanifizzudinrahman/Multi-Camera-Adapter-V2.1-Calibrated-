import RPi.GPIO as gp
from datetime import datetime as dtm
import cv2
import time
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
    
def main():

    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string
    
    print("Start testing the Camera D")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    captureCamera(4)     # Camera D
    
def captureCamera(cam):
    saat_ini = dtm.now() #tgl dan jam saat ini
    now = dtm.strftime(saat_ini, '%d-%b-%Y_%H:%M:%S') # tpye = string

    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=0))
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    if cap.isOpened():
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        
        # Window
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            cv2.imshow("CSI Camera", img)
            # This also acts as
            key = cv2.waitKey(30) & 0xFF
            # Stop the program on the ESC key
            if key == ord("q"):
                break
            elif key == ord("s"):
                cv2.imwrite("Hasil_Gambar/Camera_D_ %s.jpg" % now, img)
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)

