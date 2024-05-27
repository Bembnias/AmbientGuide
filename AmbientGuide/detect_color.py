import cv2

def determine_traffic_light_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = (0, 0, 200)
    upper_red = (10, 255, 255)
    lower_yellow = (20, 50, 100)
    upper_yellow = (30, 255, 255)
    lower_green = (40, 50, 50)
    upper_green = (80, 255, 255)

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    red_pixels = cv2.countNonZero(red_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    green_pixels = cv2.countNonZero(green_mask)

    if red_pixels > yellow_pixels and red_pixels > green_pixels:
        return 'czerwony'
    elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
        return 'żółty'
    elif green_pixels > red_pixels and green_pixels > yellow_pixels:
        return 'zielony'
    else:
        return 'nie rozpoznany'