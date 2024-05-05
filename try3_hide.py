import my_functions as f

mat = f.load_file("u15_SOLNS/stego/pic.jpg")
print("\ncheck before")
for i in range(10):
    print(mat[0][i], end=" ")


message = "if we heard mortar shells / we'd curse more in our songs / and cut down the guitar solos"

# make a list of ascii values
enc_mess = []
# TODO
# iterate through the message
# use the ord() function on each letter, append to the list

print("\ncheck encrypted message")
print(enc_mess)



# 'hide' those values in the image
count = 0
# TODO
# use indexed loops to iterate through the image mat[][]
# if we have not reached the end of the message (if count < length of the message list)
# then set this image pixel red value to the item from the message list






print("\ncheck after")
# TODO
# to check your work, loop through some pixels in the top row
# print the pixel value




# TODO
# save the image with a new filename