import numpy as np

class ImageFilter:
    def __init__(self):
        self.name = "ImageFilter"

    def mean_filter(self, row, col):
        return np.ones((row, col))/(row * col)
    
    

    
