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
    # output_filename = "data/minimum_lena_10x10.png"
    # image_obj = imagefiltering.min_filtering(imagemgr.read_image(input_filename), 10)

    # mean filter
    # output_filename = "mean_lena_zero.png"
    # image_obj = imagefiltering.mean_filtering(imagemgr.read_image(input_filename), imagefilter.mean_filter(5, 5))
    
    # 2019-01-21 Python Image Processing Study
    # sobel filter
    # output_filename = "data/sobel_lena.png"
    # image_obj = imagefiltering.sobel_filtering(imagemgr.read_image(input_filename))

    # prewitt filter
    # output_filename = "data/prewitt_lena.png"
    # image_obj = imagefiltering.prewitt_filtering(imagemgr.read_image(input_filename))

    # horizontal prewitt filter
    # output_filename = "data/horizontal_prewitt_lena.png"
    # image_obj = imagefiltering.horizontal_prewitt_filtering(imagemgr.read_image(input_filename))

    # vertical prewitt filter
    # output_filename = "data/vertical_prewitt_lena.png"
    # image_obj = imagefiltering.vertical_prewitt_filtering(imagemgr.read_image(input_filename))

    # canny filter
    # output_filename = "data/canny_3.0_lena.png"
    # image_obj = imagefiltering.canny_filtering(imagemgr.read_image(input_filename), sigma=3.0)
    
    # gaussian filter
    output_filename = "data/gaussian_3.0_lena.png"
    image_obj = imagefiltering.gaussian_filtering(imagemgr.read_image(input_filename), sigma=3.0)

    # Laplace filter
    # output_filename = "data/laplace_lena.png"
    # image_obj = imagefiltering.laplace_filtering(imagemgr.read_image(input_filename))

    # Gaussian Laplace filter
    # output_filename = "data/gaussian_laplace_lena_sigma_3.png"
    # image_obj = imagefiltering.gaussian_laplace_filtering(imagemgr.read_image(input_filename), sigma=3)
    imagemgr.write_image(image_obj, output_filename)

main()
