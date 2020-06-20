import PIL
from PIL import Image

def grayScale(image):
    width, height = image.size
    rgb_image = image.convert('RGB')
    for y in range(0, height):
        for x in range(0, width):
            red, green, blue = rgb_image.getpixel((x, y))
            red *= 0.299
            green *= 0.587
            blue *= 0.144
            sum = int (red + green + blue)
            image.putpixel((x, y), (sum, sum, sum))

    return image


def main():
    image = PIL.Image.open("ba.jpg")
    gray = grayScale(image)
    gray.show()


main()
