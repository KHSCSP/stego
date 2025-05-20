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




