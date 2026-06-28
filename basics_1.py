import cv2

image = cv2.imread('image.png')

if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")
    cropped = image[100:400, 100:500]  # Crop the image to a specific region
    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()