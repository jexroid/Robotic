import cv2
import numpy as np



def detect_color(image):
    # Define ranges of color in HSV
    blue_range = [np.array([110,50,50]), np.array([130,255,255])]
    green_range = [np.array([50, 100, 100]), np.array([70, 255, 255])]
    red_range = [np.array([0,50,50]), np.array([10,255,255])]
    yellow_range = [np.array([20,100,100]), np.array([30,255,255])]
    color_ranges = [('blue', blue_range), ('green', green_range),('red', red_range), ('yellow', yellow_range)]

    kernel = np.ones((6,6), np.uint8)
    blurred_frame =cv2.GaussianBlur(image , (5 ,5) , 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    
    ### delation for better recegnization ###
    delatedImage = cv2.dilate(hsv, kernel=kernel, iterations=1)

    ### closing morphology for reducing noise ###
    closing_morph_image = cv2.morphologyEx(delatedImage,cv2.MORPH_CLOSE, kernel, iterations=1)
    

    # Initialize the count of each color
    color_count = {'blue': 0, 'green':0 , 'red': 0, 'yellow': 0}

    # Iterate over all color ranges
    for color_name, (lower, upper) in color_ranges:
        # Threshold the HSV image to get only the desired color
        mask = cv2.inRange(closing_morph_image, lower, upper)

        # Count the number of pixels in the mask
        color_count[color_name] = cv2.countNonZero(mask)

    # Return the name of the most dominant color
    return max(color_count, key=color_count.get)