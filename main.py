import cv2

def mouseEvents(event, mx, my, flags, param):
    global x, y
    if event == cv2.EVENT_MOUSEMOVE:
        x = mx
        y = my
        updateTemperature()

def updateTemperature():
    global gray16Img, x, y
    temp_img = gray16Img.copy()
    targetPixel = gray16Img[y, x]
    tempedPixel = targetPixel*0.1
    cv2.putText(temp_img, '{0:.1f} Celsius'.format(tempedPixel), (x - 80, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('gray16', temp_img)

gray16Img = cv2.imread("image2.tiff", cv2.IMREAD_ANYDEPTH)

cv2.namedWindow('gray16')
cv2.setMouseCallback('gray16', mouseEvents)

cv2.imshow('gray16', gray16Img)
cv2.waitKey(0)
cv2.destroyAllWindows()