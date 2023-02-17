def detect():
    from colorama import Fore
    import cv2 as cv
    import numpy as np

    cap = cv.VideoCapture(0)

    yellow_range = [np.array([0, 167, 117]), np.array([30, 227, 241])]
    red_range = [np.array([0, 145, 170]),    np.array([10, 255, 255])]
    blue_range = [np.array([110, 155, 95]), np.array([125, 255, 255])]
    green_range = [(np.array([45, 100, 55])), (np.array([105, 255, 255]))]
    kernal = np.ones((5, 5), "uint8")
    # making sure and reducing the errors

    while (True):
        ### defining video captureing ###
        rec, frame = cap.read()

        frame = cv.rectangle(frame, (324, 241), (321, 245), (255, 0, 0), 4)

        hsv = cv.cvtColor(
            frame,
            cv.COLOR_BGR2HSV
        )

        mask_yellow = cv.inRange(hsv, yellow_range[0], yellow_range[1])
        mask_green = cv.inRange(hsv, green_range[0], green_range[1])
        mask_blue = cv.inRange(hsv, blue_range[0], blue_range[1])
        mask_red = cv.inRange(hsv, red_range[0], red_range[1])
        all_masks = {
            "yellow": mask_yellow,
            "green": mask_green,
            "blue": mask_blue,
            "red": mask_red
        }

        for text, mask in all_masks.items():
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
                print(Fore.GREEN, f"{text} pixels :", Fore.WHITE, color_pixels)

                if int(area) > 1000:
                    x, y, w, h = cv.boundingRect(contour)

                    frame = cv.rectangle(
                        frame, (x, y), (x + w, y + h), (255, 255, 20), 2)
                    frame = cv.putText(
                        frame, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 20))

                    
                    

        

        cv.imshow('mask green', color_mask)
        cv.imshow('resault', frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            break


print(detect())
