#Import Libraries
import cv2
import numpy as np
import math

image_arr = cv2.imread('Smile.jpg')  #import the original image
gray_image_arr=cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)  #Convert image into a gray scale image, where pixel values vary from 0(dark)-255(white)

#Function Definition
def Image_intensity_level_Reduction(image, levels):
    reduced_pixel_img=np.round(image // levels) #Levels are in the power of 2
    normalized_img=reduced_pixel_img * levels   #Normalizing the image(such that values are range inbetween 0-255) with same intensity level   
    return normalized_img

#User-Friendly method to obtain the Intensity Level
print("\nHello, This is Emmanuel Hashika, Please follow the instructions below\n")
while True:
    levels_value = int(input("Enter the number of intensity levels to be reduced from Image (Possible Inputs-2,4,8,16,32,64,128,256): "))
    if levels_value > 0 and math.log2(levels_value).is_integer():
        break
    else:
        print("\nInappropriate Intensity Level Value\nPlease enter a valid number of intensity levels, that is an integer power of 2 and the Maximum is 256\n")

Reduced_IntensityLevels_Image = Image_intensity_level_Reduction(gray_image_arr, levels_value)

# Display the original and Intensity adjusted images
cv2.imshow('Original Image', image_arr)
cv2.imshow('Reduced Intensity Levels of Image by '+ str(levels_value), Reduced_IntensityLevels_Image)

cv2.waitKey(0)
cv2.destroyAllWindows()