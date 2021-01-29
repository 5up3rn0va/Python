from PIL import Image

im1 = Image.open("flag.png")
pim1 = im1.load()
im2 = Image.open("lemur.png")
pim2 = im2.load()
width, height = im1.size

for i in range(width):
    for j in range(height):
        r1, g1, b1 = pim1[i, j]
        r2, g2, b2 = pim2[i, j]
        pim1[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

im1.show()