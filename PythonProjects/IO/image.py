from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out2.jpg")
        ...
    


main()