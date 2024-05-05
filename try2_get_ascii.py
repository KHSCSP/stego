# ---- what is this picture saying?? ----

import my_functions as f

mat = f.load_file("u15_SOLNS/stego/pic.jpg")
print("\ncheck a slice original")
print(mat[0][:5])


# get each (r,g,b) value into one long list
nums = []
for r in range(len(mat)):
    for c in range(len(mat[0])):
        nums.append(mat[r][c][0])
        nums.append(mat[r][c][1])
        nums.append(mat[r][c][2])
print("\ncheck a slice nums list")
print(nums[0:5])



# convert to ascii list
letters = []
for item in nums:
    letters.append(chr(item))
print("\ncheck a slice of ascii list")
print(letters[0:5])
