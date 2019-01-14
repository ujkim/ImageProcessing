import os
from lib.imagemgr import ImageManager as IMGR
from lib.imagefilter import ImageFilter as IMGF
from lib.imagefiltering import ImageFiltering as IMGFL

# Execution of Our Image Processing Library
def main():
    input_filename = "data/lena.png"
    output_filename = ""
    imagemgr = IMGR()
    imagefilter = IMGF()
    imagefiltering = IMGFL()

    # median filter
    # output_filename = "median_lena_2.png"
    # image_obj = imagefiltering.median_filtering(imagemgr.read_image(input_filename), 10)
    
    # maximum filter
    # output_filename = "maximum_lena_5x5.png"
    # image_obj = imagefiltering.max_filtering(imagemgr.read_image(input_filename), 5)

    # minimum filter
    output_filename = "data/minimum_lena_10x10.png"
    image_obj = imagefiltering.min_filtering(imagemgr.read_image(input_filename), 10)

    # mean filter
    # output_filename = "mean_lena_zero.png"
    # image_obj = imagefiltering.mean_filtering(imagemgr.read_image(input_filename), imagefilter.mean_filter(5, 5))
    imagemgr.write_image(image_obj, output_filename)

main()
