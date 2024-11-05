import sys
import cv2
import numpy as np


def comprress_image(img, new_width):
    height, width = img.shape
    aspect_ratio = height/width

    new_height = int(new_width*aspect_ratio*0.5)

    scaled_image = cv2.resize(img, (new_width, new_height))

    return scaled_image


def convert_image_to_ascii(img, chars):
    ascii_art_array = np.array(["" for _ in img.flatten()])
    width = img.shape[1]

    for i, pixel in enumerate(img.flatten()):
        color_ratio = pixel/255
        ascii_art_array[i] = chars[int( color_ratio * (len(chars) - 1) )]

    ascii_str = ""
    inserted_letters = 0
    for i in ascii_art_array:
        ascii_str += i
        inserted_letters += 1

        if inserted_letters == width:
            inserted_letters = 0
            ascii_str += "\n"
        
        
    return ascii_str


def main():
    image_path = sys.argv[1]
    new_width = int(sys.argv[2])

    #ASCII charachters from least bright to most bright    
    ascii_chars = ".,:;+*?%S#@"

    #Get the image
    img = cv2.imread(image_path)
    grey_scaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    comp_img = comprress_image(grey_scaled_image, new_width)


    #Write the result
    with open("result.txt", "w") as f:
        f.write(convert_image_to_ascii(comp_img, ascii_chars))

if __name__ == '__main__':
    main()