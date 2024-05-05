import my_functions as f

mat = f.load_file("u15_SOLNS/stego/pic.jpg")
print("\ncheck before")
for i in range(25):
    print(mat[0][i][0], end=" ")


message = "if we heard mortar shells / we'd curse more in our songs / and cut down the guitar solos"

# make a list of ascii values
enc_mess = []
for letter in message:
    enc_mess.append(ord(letter))
print("\ncheck encrypted message")
print(enc_mess)


# 'hide' those values in the image
count = 0
for r in range(len(mat)):
    for c in range(len(mat[0])):
        if count < len(enc_mess):
            mat[r][c][0] = enc_mess[count]
        count += 1


print("\ncheck after")
for i in range(25):
    print(mat[0][i][0], end=" ")


f.save(mat, "u15_SOLNS/stego/pic_mod3.jpg")