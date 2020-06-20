import PIL
from PIL import Image

def grayScale(image):
    width, height = image.size # get the Width and heigth of image
    rgb_image = image.convert('RGB') # convert the image to RGB
    for y in range(0, height):
        for x in range(0, width):
            red, green, blue = rgb_image.getpixel((x, y)) # get Red, Green , Blue of each pixel
            red *= 0.299  #Used 30% of Red
            green *= 0.587 #Used 59% of Green
            blue *= 0.144 # used 11% of Blue
            sum = int (red + green + blue)  #Sum all these three values of color
            image.putpixel((x, y), (sum, sum, sum)) #set it again to the corresponding pixel value

    return image


def main():
    image = PIL.Image.open("minion.jpg") # Open method used to open different extension image file
    gray = grayScale(image)
    gray.show() # This method will show image in any image viewer


main()
