def color(INPUT):

    import cv2 as cv
    import numpy as np

    cap = cv.VideoCapture(1)
    kernal = np.ones((5, 5), "uint8")

    yellow_range = [np.array([0, 167, 117]), np.array([30, 227, 241])]
    red_range = [np.array([0, 145, 170]),    np.array([10, 255, 255])]
    blue_range = [np.array([110, 155, 95]), np.array([125, 255, 255])]
    green_range = [(np.array([45, 100, 55])), (np.array([105, 255, 255]))]

    # For red color

    if INPUT == 'y':
        INPUT = yellow_range
    elif INPUT == 'r':
        INPUT = red_range
    elif INPUT == 'b':
        INPUT = blue_range
    elif INPUT == 'g':
        INPUT = green_range

    lower = INPUT[0]
    upper = INPUT[1]
    kernel = np.ones((6, 6), np.uint8)

    # making sure and reducing the errors
    CERTAINITY = 0
    timer = 0

    while (timer < 50):
        ### defining video captureing ###
        rec, frame = cap.read()

        hsv = cv.cvtColor(
            frame,
            cv.COLOR_BGR2HSV
        )

        mask_yellow = cv.inRange(
            hsv,
            lower,
            upper
        )

        color_mask = cv.dilate(mask_yellow, kernel)
        color_mask = cv.morphologyEx(color_mask, cv.MORPH_CLOSE, kernel)
        color_mask = cv.morphologyEx(color_mask, cv.MORPH_OPEN, kernel)

        ### finding the contours of image ###
        contours, salam = cv.findContours(
            color_mask,
            cv.RETR_TREE,
            cv.CHAIN_APPROX_NONE
        )

        ### NOW LETS DRAW THE FOUND CONTOURS with condition ###
        for contour in contours:
            cv.drawContours(frame, contour, -1, (0, 255, 0), 3)
            area = cv.contourArea(contour)

            if int(area) > 1000:
                x, y, w, h = cv.boundingRect(contour)

                frame = cv.rectangle(
                    frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

        # cv.imshow('mask green', color_mask)
        # cv.imshow('resault', frame)

        color_pixels = cv.countNonZero(mask_yellow)
        print("pixels :", color_pixels)

        if color_pixels > 10000:
            CERTAINITY = CERTAINITY + 1

        timer = timer + 1

        if CERTAINITY >= 30:
            return True

        # if cv.waitKey(10) & 0xFF == ord('q'):
        #     cap.release()
        #     cv.destroyAllWindows()
        #     break

    if CERTAINITY <= 30:
        return False


print(color('b'))
