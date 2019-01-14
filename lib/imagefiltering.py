import scipy.ndimage

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
