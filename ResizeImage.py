from PIL import Image


def resize(imagePath, typeofimage, width, height):
    img = Image.open(imagePath)
    new_img = img.resize((width, height))
    new_img.save(imagePath, typeofimage, optimize=True)
