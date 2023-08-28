import sys
from PIL import Image


try:
    image_path = sys.argv[1]
    image = Image.open(image_path)

    width, height = image.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    image = image.resize((int(new_width), int(new_height)))

    img = image.convert('L')

    pixels = img.getdata()

    ASCII_CHARS = ['`', '^', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+', '_', '-', '?', ']', '[', '}',
                   '{', '1', ')', '(', '|', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U',
                   'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#',
                   'M', 'W', '&', '8', '%', 'B', '@', '$']

    new_pixels = [ASCII_CHARS[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)

except:
    print(f"{image_path} image path not found, please check and try again")
