from colorama import Fore
import cv2 as cv
import numpy as np
from modules import serial_communication as sc


def detect(color):

    cap = cv.VideoCapture(0)

    red_range = [np.array([0, 123, 47]),    np.array([6, 255, 224])]
    blue_range = [np.array([102, 104, 106]), np.array([134 , 199, 219])]
    green_range = [(np.array([36, 108, 97])), (np.array([85, 160, 134]))]
    kernal = np.ones((5, 5), "uint8")
    # making sure and reducing the errors
    CERTAINITY = 0
    while (CERTAINITY < 50):
        ### defining video captureing ###
        rec, frame = cap.read()

        frame = cv.rectangle(frame, (324, 241), (321, 245), (255, 0, 0), 4)

        hsv = cv.cvtColor(
            frame,
            cv.COLOR_BGR2HSV
        )

        mask_green = cv.inRange(hsv, green_range[0], green_range[1])
        mask_blue = cv.inRange(hsv, blue_range[0], blue_range[1])
        mask_red = cv.inRange(hsv, red_range[0], red_range[1])
        all_masks = {
            "green": mask_green,
            "blue": mask_blue,
            "red": mask_red
        }

        mask = all_masks.get(color)
        color_mask = cv.dilate(mask, kernel=kernal)
        color_mask = cv.morphologyEx(
            color_mask, cv.MORPH_CLOSE, kernel=kernal)
        color_mask = cv.morphologyEx(
            color_mask, cv.MORPH_OPEN, kernel=kernal)
        ### finding the contours of image ###
        contours, salam = cv.findContours(
            color_mask,
            cv.RETR_TREE,
            cv.CHAIN_APPROX_NONE
        )
        ### NOW LETS DRAW THE FOUND CONTOURS with condition ###
        for contour in contours:
            area = cv.contourArea(contour)
            color_pixels = cv.countNonZero(mask)

            # print(Fore.GREEN, f"{text} pixels :", Fore.WHITE, color_pixels)
            if color_pixels >= 6000:
                if int(area) > 4000:
                    x, y, w, h = cv.boundingRect(contour)
                    frame = cv.rectangle(
                        frame, (x, y), (x + w, y + h), (255, 255, 20), 2)
                    hight = int((((x+w) - x)/2)+x)
                    width = int((((y+h) - y)/2)+y)
                    frame = cv.rectangle(
                        frame, (hight+1, width+1), (hight, width), (255, 255, 20), 2)
                    # frame = cv.putText(
                    #     frame, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 20))

                    if hight < 300:
                        sc.communicate.send("x,-0.01")
                        if sc.communicate.listener() == "ok":
                            pass

                        print(Fore.GREEN, "RIGHT", Fore.WHITE,
                              " sended to HARDWARE")
                    elif hight > 360:
                        sc.communicate.send("x,0.01")
                        if sc.communicate.listener() == "ok":
                            pass

                        print(Fore.GREEN, "LEFT", Fore.WHITE,
                              " sended to HARDWARE")
                    else:
                        CERTAINITY = CERTAINITY + 1

        cv.imshow('mask green', color_mask)

        if cv.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            break
