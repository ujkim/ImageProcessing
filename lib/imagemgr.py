from scipy.misc.pilutil import Image

class ImageManager:
    def __init__(self):
        self.name = ""

    def read_image(self, path):
        print('call read_image')
        return Image.open(path).convert('L')

    def write_image(self, image_object, filename):
        image_object.save(filename)
        print("%s filename save success" % filename)