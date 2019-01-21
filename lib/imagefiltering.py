import numpy as np
import scipy.ndimage
from skimage import filters
from skimage import feature
import matplotlib.pyplot as plt

class ImageFiltering:
    def __init__(self):
        self.name = ""

    def mean_filtering(self, image_object, image_filter):
        return scipy.misc.toimage(scipy.ndimage.filters.convolve(image_object, image_filter))

    def max_filtering(self, image_object, filter_size):
        return scipy.misc.toimage(scipy.ndimage.filters.maximum_filter(image_object, filter_size))
    
    def min_filtering(self, image_object, filter_size):
        return scipy.misc.toimage(scipy.ndimage.filters.minimum_filter(image_object, filter_size))

    def median_filtering(self, image_object, filter_size):
        return scipy.misc.toimage(scipy.ndimage.filters.median_filter(image_object, filter_size))

    def sobel_filtering(self, image_object):
        return scipy.misc.toimage(filters.sobel(image_object))

    def prewitt_filtering(self, image_object):
        return scipy.misc.toimage(filters.prewitt(image_object))

    def horizontal_prewitt_filtering(self, image_object):
        return scipy.misc.toimage(filters.prewitt_h(image_object))
    
    def vertical_prewitt_filtering(self, image_object):
        return scipy.misc.toimage(filters.prewitt_v(image_object))

    def laplace_filtering(self, image_object):
        return scipy.misc.toimage(scipy.ndimage.filters.laplace(image_object))

    def gaussian_filtering(self, image_object, sigma):
        return scipy.misc.toimage(scipy.ndimage.filters.gaussian_filter(image_object, sigma))

    def gaussian_laplace_filtering(self, image_object, sigma):
        return scipy.misc.toimage(scipy.ndimage.filters.gaussian_laplace(image_object, sigma))

    def canny_filtering(self, image_object, sigma):
        return scipy.misc.toimage(feature.canny(scipy.misc.fromimage(image_object), sigma).astype(np.float32))

