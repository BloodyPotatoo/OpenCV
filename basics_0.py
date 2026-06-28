import cv2

image = cv2.imread('image.png')
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")

    resized_image = cv2.resize(image, (1000, 1000))
    cv2.imshow('Resized Image', resized_image)
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()