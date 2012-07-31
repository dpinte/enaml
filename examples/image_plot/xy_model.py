#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" ImageFromXY interactive example

An interactive demo to generate X-Y plots with matplotlib and send
them as images.

"""

import numpy as np
from traits.api import (HasTraits, Array, Int, Float, Instance,
                        on_trait_change, List, Str)
import enaml
from enaml.qt.qt_local_application import QtLocalApplication
from enaml.noncomponents.image import ImageFromXY


class XYModel(HasTraits):
    N = Int(250)
    omega = Float(4)
    xmin = Float(-1)
    xmax = Float(1)
    x = Array()
    y = Array()
    # TODO: the image should really be in a plot model, not the data model
    image = Instance(ImageFromXY)
    dpi = Int(100)
    linetype_choices = List(Str)
    linetype_idx = Int(0)
    linecolor_choices = List(Str)
    linecolor_idx = Int(1)
    function_choices = List(Str)
    function_idx = Int(0)

    def __init__(self):
        super(XYModel, self).__init__()
        self.update_image()

    @on_trait_change('N, xmax, omega, function_idx, dpi, linetype_idx, linecolor_idx')
    def update_image(self):
        self.x = np.linspace(self.xmin, self.xmax, self.N)
        f = self.function()
        self.y = f(2 * np.pi * self.omega * self.x)
        linecolor = self.linecolor_choices[self.linecolor_idx]
        linestyle = self.linetype_choices[self.linetype_idx]
        self.image = ImageFromXY(self.x, self.y, dpi=self.dpi,
                                 linecolor=linecolor, linestyle=linestyle)

    def function(self):
        fname = self.function_choices[self.function_idx]
        if fname == 'sin':
            return np.sin
        if fname == 'cos':
            return np.cos
        if fname == 'sinc':
            return np.sinc

    def _linetype_choices_default(self):
        # TODO: make these human readable instead of matplotlib standard
        return ['-', '--', ':', 'o']

    def _linecolor_choices_default(self):
        return ['k', 'b', 'g', 'r']

    def _function_choices_default(self):
        return ['sin', 'cos', 'sinc']


def main():
    with enaml.imports():
        from xy_view import Main
    model = XYModel()
    view = Main(model=model)
    app = QtLocalApplication()
    app.serve('main', view)
    app.mainloop()

if __name__ == '__main__':
    main()
