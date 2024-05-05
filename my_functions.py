from PIL import Image 
import numpy as np
import random

# this function receives a string filename
# and returns a 2D array of pixel values
def load_file(orig):
    im = Image.open(orig)
    # im.show() # try this!
    mat = np.array(im)
    return mat


# this function receives a 2D list of pixels and string filename
# and saves the file as an image
def save(mat, filename):
    '''
    receives np array
    saves as image file
    '''
    result = Image.fromarray(np.uint8(mat))
    result.save(filename)



# given a string
# return a list, which is 'binary' version
# ex: [1, 0, 0, 1, 0, ect]
def convert_to_list(s):
    ans = []
    # TODO
    return ans


   
# given a list of 1s and 0s
# replace the least significant bit of the red value
# with the message
# mess is a list of 0s and 1s, ex: [1,1,0,0,0,1,0,etc]
# return the new matrix
def hide_message(mat, mess):
    # TODO
    return mat



