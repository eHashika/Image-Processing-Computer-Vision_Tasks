# Importing Libraries
import cv2

def rotate_image(img, angle):

    rows, cols = img.shape[:2]  # Extract tuple containing the height(row) and width(column) of the image

    Rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)     # Arguments of getRotationMatrix2D(Rotation Matrix) will be explain below
    #Arguments(1) meaning -> (cols / 2, rows / 2) refers to the center point from which the image should rotate
    #Arguments(2,3) meaning -> angle refers to the degree of rotation that image should rotate, Final argument(=1) represents the scale factor of the image

    return cv2.warpAffine(img, Rotation_matrix, (cols, rows))# Arguments of warpAffine(Affine transfrmation) will explain below
    #Arguments(1,3) meaning -> Input Image, Output image size
    #Arguments(2) meaning -> Applying the affine transformation to the Matrix such that output image will be in the specified size

# Importing the image
image_arr = cv2.imread('Smile.jpg')  #import the original image

# Rotating the image by 45 & 90 degrees, by appling the above defined function
Img_rotated_45 = rotate_image(image_arr, 45)
Img_rotated_90 = rotate_image(image_arr, 90)

# Displaying Original Image
cv2.imshow('Original Image', image_arr)

# Displaying Rotated Image
cv2.imshow('Original Image is Rotated by 45 Degrees Anticlockwise', Img_rotated_45)
cv2.imshow('Original Image is Rotated by 90 Degrees Anticlockwise', Img_rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()