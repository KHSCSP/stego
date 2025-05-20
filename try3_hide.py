import my_functions as f

mat = f.load_file("stego/pic.jpg")


print("\n--- check the pixels before modification ---")
for i in range(10):
    print(mat[0][i], end=" ")


message = "TODO type a message to hide"


print("\n\n--- making a list of ASCII values ---")
enc_mess = []
# TODO
# iterate through the message
# use the ord() function on each letter, append to the list




print("\n--- check ascii message ---")
print("(this should be a list of ASCII values)")
print(enc_mess)



# 'hide' those values in the image
count = 0
# TODO
# use indexed loops to iterate through the image mat[][]
# if we have not reached the end of the message (if count < length of the message list)
# then set this image pixel red value to the item from the message list






print("\n--- check pixels after modification ---")
print("(your message should be hidden in the pixels)")
# TODO
# to check your work, loop through some pixels in the top row
# print the pixel value, make sure your message is being 'hidden'




# TODO
# save the image with a new filename