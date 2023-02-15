def color(INPUT):

    import cv2 as cv
    import numpy as np

    cap = cv.VideoCapture(1)
    kernel = np.ones((6, 6), np.uint8)

    yellow_range = [np.array([10, 134, 123]), np.array([59, 243, 255])]
    red_range = [np.array([0, 50, 50]),    np.array([10, 255, 255])]
    blue_range = [np.array([95, 100, 55]), np.array([133, 255, 255])]
    green_range = [(np.array([50, 100, 100])), (np.array([70, 255, 255]))]

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
    while(timer < 50):
        ### defining video captureing ###
        rec, frame = cap.read()

        blurred_frame = cv.GaussianBlur(
            frame,
            (5, 5),
            0
            )
        
        hsv = cv.cvtColor(
            blurred_frame,
            cv.COLOR_BGR2HSV
            )
        
        delatedImage = cv.dilate(
            hsv,
            kernel=kernel,
            iterations=1
            )
        
        mask_yellow = cv.inRange(delatedImage,
            lower,
            upper
            )

        closing_morph_image = cv.morphologyEx(
            mask_yellow,
            cv.MORPH_CLOSE, 
            kernel,
            iterations=1
            )

        ### finding the contours of image ###
        contours, salam = cv.findContours(
            closing_morph_image,
            cv.RETR_TREE,
            cv.CHAIN_APPROX_NONE
        )

        ### NOW LETS DRAW THE FOUND CONTOURS with condition ###
        for contour in contours:
            cv.drawContours(frame, contour, -1, (0, 255, 0), 3)

        ### mixing the main frame with binary image ###
        frame_masked = cv.bitwise_and(frame, frame, mask=mask_yellow)

        color_pixels = cv.countNonZero(mask_yellow)
        print("pixels :", color_pixels)

        if color_pixels > 10000:
            CERTAINITY = CERTAINITY + 1

        # DONE !

        cv.imshow('frame', frame_masked)


        timer = timer + 1
        keyexit = cv.waitKey(5) & 0xFF
        if keyexit == 27:
            break
        if CERTAINITY >= 30:
            return True
            
    if CERTAINITY <= 30:
        return False
    
    cv.destroyAllWindows()
    cap.release()