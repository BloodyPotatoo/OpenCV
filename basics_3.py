import cv2

image = cv2.imread('image.png')

if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")
    p1 = (50, 100)
    p2 = (100, 200)
    color = (0,0,0)
    thickness = 2
    radius = 50
    center = (280,100)
    text = "Hi, its just a trial"
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.line(image, p1, p2, color, thickness)
    cv2.rectangle(image,p1 , p2, color, thickness)
    cv2.circle(image, center, radius, color, thickness) # thickness = -1 to fill
    cv2.putText(image, text, (50, 50), font, 1.2, color, thickness)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()