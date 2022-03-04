
init -2 python:
    import os

    class ImageBuilder(object):
        def __init__(self):
            self.data = {}

        def getFillSize(self, image, screen):
            image_size = renpy.image_size(image)
            ratio = min(screen[0], screen[1]) / float(min(image_size[0], image_size[1]))
            return (image_size[0] * ratio, image_size[1] * ratio)

        def getFullWidth(self,image,width):
            image_size = renpy.image_size(image)
            ratio = width / float(image_size[0])
            return (image_size[0] * ratio, image_size[1] * ratio)

    imagebuilder = ImageBuilder()
