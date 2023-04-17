#Converting an RGB image to grayscale and then to binary
from skimage import data, io
from skimage.color import rgb2gray
import numpy as np

#original image comes from skimage 
original_image = data.coffee()
#rgb -> grayscale
gray_image = rgb2gray(original_image)
#create an empty array with the same shape as 
#the grayscale image, to store the binary image
binary_image = np.zeros((original_image.shape[0], 
                         original_image.shape[1]), 
                         dtype='float64')

#128 is divided by 255 to normalize the pixel 
#values from 0-255 to 0-1
threshold = 128/255.0

#loop through each pixel in the grayscale image
for row in range(0, (original_image.shape[0]-1)):
    for col in range(0, (original_image.shape[1]-1)):
      #if the pixel value in the grayscale image is 
      #greater than the threshold value, 1, otherwise 0
        if(gray_image[row, col] > threshold):
            binary_image[row, col] = 1
        else:
            binary_image[row, col] = 0

#display the result
io.imshow(binary_image)
io.show()