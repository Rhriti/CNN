import cv2

# Load an image in grayscale
image = cv2.imread('2.png', cv2.IMREAD_GRAYSCALE)

# Convert the image to binary representation
binary_image = [[bin(pixel)[2:].zfill(8) for pixel in row] for row in image]

# Print the binary representation
for row in binary_image:
    print(' '.join(row))
