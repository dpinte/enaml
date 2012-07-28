#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from base64 import b64encode, b64decode
from abstract_image import AbstractImage
import matplotlib.pyplot as plt
from io import BytesIO


class ImageFromXY(AbstractImage):
    """ A subclass of AbstractImage that generates a simple x-y line plot
    and returns it as an image.

    """
    _dpi = 100

    def __init__(self, x, y, dpi=None):
        """ Just need to update internal x and y

        """
        if dpi is not None:
            self._dpi = dpi
        self.update(x, y)

    def update(self, x, y, dpi=None):
        """ change the internal x and y data
        """
        self._x = x
        self._y = y
        if dpi is not None:
            self._dpi = dpi

    def as_dict(self):
        """ Return the image as a JSON-serializable dict

        """
        plt.clf()
        plt.plot(self._x, self._y)
        plt.xlim((min(self._x), max(self._x)))
        iobuffer = BytesIO()
        plt.savefig(iobuffer, bbox_inches='tight', dpi=self._dpi)
        image_dict = {
            'data' : b64encode(iobuffer.getvalue()),
            'format' : 'raw_file',
            'size' : (-1, -1)
        }
        return image_dict

    @staticmethod
    def from_dict(image_dict):
        """ Receive a JSON representation of an image and convert it into the
        appropriate Python object

        """
        data = b64decode(image_dict['data'])
        return ImageFromXY(data)
