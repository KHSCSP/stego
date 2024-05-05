import my_functions as f

mat = f.load_file("u15_SOLNS/stego/pic.jpg")

# --- what do we have? ---
print("\nitem[0], this accesses one row of the image")
print(mat[0])

print("\nitem[0][0], this accesses one RGB pixel")
print(mat[0][0])

print("\nitem[0][0][0], this accesses Red for one pixel")
print(mat[0][0][0])



# --- how can we change it? ---
for r in range(len(mat)):
    for c in range(len(mat[0])):
        # set red pixel to zero
        mat[r][c][0] = 0

print("\nsaving pic with all pixels red = 0")
f.save(mat, "u15_SOLNS/stego/pic_mod1.jpg")


