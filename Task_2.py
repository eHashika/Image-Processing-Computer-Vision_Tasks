# Importing Libaries
import cv2
import numpy as np

image_arr = cv2.imread('Smile.jpg')  #import the original image

def average_filtering(image, kernel_size):
    height, width, channels = image.shape   #Get the dimensions of the input image
    filtered_image = np.zeros((height, width, channels), dtype=np.uint8)    #Create an empty array to store the filtered image

    # Define the padding size based on the kernel size
    padding = kernel_size // 2

    # Apply the filter to each pixel in the image
    for i in range(padding, height - padding):  # Iterate over rows
        for j in range(padding, width - padding):   # Iterate over columns
            
            neighborhood = image[i - padding:i + padding + 1, j - padding:j + padding + 1, :]   # Extract the neighborhood around the current pixel for each color channel
            average = np.mean(neighborhood, axis=(0, 1))    # Calculate the average of the neighborhood pixels for each color channel
            filtered_image[i, j, :] = average   # Set the filtered pixel value to the average for each color channel

    return filtered_image

# Applying average Filtering with different sizes of kernels of 3x3, 10x10, and 20x20
filtered_image_3x3 = average_filtering(image_arr, 3)
filtered_image_10x10 = average_filtering(image_arr, 10)
filtered_image_20x20 = average_filtering(image_arr, 20)

# Displaying the averagely filtered image
cv2.imshow('Original Image', image_arr)
cv2.imshow('3x3 Average Filter Applied', filtered_image_3x3)
cv2.imshow('10x10 Average Filter Applied', filtered_image_10x10)
cv2.imshow('20x20 Average Filter Applied', filtered_image_20x20)

cv2.waitKey(0)
cv2.destroyAllWindows()