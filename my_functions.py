from PIL import Image 
import numpy as np
import random

# this function receives a string filename
# and returns a 2D array of pixel values
def load_file(orig):
    im = Image.open(orig)
    # im.show()
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
    for letter in s:
        binary = bin(ord(letter))[2:]
        for item in binary:
            ans.append(int(item))
    return ans


   
# given a list of 1s and 0s
# replace the least significant bit of the red value
# with the message
# mess is a list of 0s and 1s, ex: [1,1,0,0,0,1,0,etc]
# return the new matrix
def hide_message(mat, mess):
    count = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if count < len(mess):
                # ex: 78 replaced with 79
                if mat[r][c][0] % 2 == 0 and mess[count] %2 != 0:
                    mat[r][c][0] += 1
                # ex: 79 replaced with 78
                elif mat[r][c][0] % 2 != 0 and mess[count] %2 == 0:
                    mat[r][c][0] -= 1
            else:
                return mat
            count += 1
    return mat



