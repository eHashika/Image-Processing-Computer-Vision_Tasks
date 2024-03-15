import cv2
import numpy as np

def resolution_reduction(img, block_size):
    rows, cols = img.shape[:2]  # Extract tuple containing the height(row) and width(column) of the image

    for row in range(0, rows, block_size):  # Iterate over rows(height) with step block_size
        for col in range(0, cols, block_size):  # Iterate over columns(width) with step block_size

            current_block = img[row:row+block_size, col:col+block_size] # Extract the current block of pixels from the image
            avg = np.mean(current_block)    # Calculate the average intensity of the block
            img[row:row+block_size, col:col+block_size] = avg # Replace the pixel values in the current block(or image) with the average intensity of that block

    return img

# Importing the image
image_arr = cv2.imread('Smile.jpg')

# Reduce resolution with different block sizes filters for the gray scale images(since the function is a 2D operation, applicable for gray scale)
resolution_reduced_3x3_block = resolution_reduction(cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY), 3)
resolution_reduced_5x5_block = resolution_reduction(cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY), 5)
resolution_reduced_7x7_block = resolution_reduction(cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY), 7)

# Display the original Image
cv2.imshow('Gray Scale of Original Image', cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY))

# Display images after applying different block size filters
cv2.imshow('Applying 3x3 Block Resolution Reduced Filter', resolution_reduced_3x3_block)
cv2.imshow('Applying 5x5 Block Resolution Reduced Filter', resolution_reduced_5x5_block)
cv2.imshow('Applying 7x7 Block Resolution Reduced Filter', resolution_reduced_7x7_block)

cv2.waitKey(0)
cv2.destroyAllWindows()