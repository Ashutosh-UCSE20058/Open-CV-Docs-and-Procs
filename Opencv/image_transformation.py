import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpg')
cv.imshow('Cat', img)
# translation of image

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x ==> left
# -y ==> up
# x ==> right
# y ==> down

translated = translate(img, 100, -100)
cv.imshow('Translated', translated)

# rotation of image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img , -45)
cv.imshow('Rotate', rotated)

# resizing the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image ', resized)


# flipping
flip = cv.flip(img, -1)
cv.imshow('Flipped Image',flip)

#cropping the image
cropped = img[200:300, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)