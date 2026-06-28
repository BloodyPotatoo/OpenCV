import cv2

image = cv2.imread('image.png')

if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")
    (h,w) = image.shape[:2]
    center = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, m, (w, h))
    cv2.imshow('Rotated Image', rotated)
    cv2.imshow('Original Image', image)

    flipped = cv2.flip(image, 1)# 0 up down , 1 left right, -1 both
    cv2.imshow("flipped", flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()