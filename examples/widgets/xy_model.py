import threading
import numpy as np
from traits.api import (HasTraits, Array, Int, Float, Instance,
                        on_trait_change, List, Enum, Str)
import enaml
from enaml.qt.qt_local_application import QtLocalApplication
from enaml.noncomponents.image import ImageFromXY
from IPython.frontend.terminal.embed import InteractiveShellEmbed


class XYModel(HasTraits):
    N = Int(250)
    omega = Float(4)
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

    def __init__(self):
        super(XYModel, self).__init__()
        self.update_image()

    @on_trait_change('N, xmax, omega, dpi, linetype_idx, linecolor_idx')
    def update_image(self):
        self.x = np.linspace(0, self.xmax, self.N)
        self.y = np.sin(2 * np.pi * self.omega * self.x)
        linecolor = self.linecolor_choices[self.linecolor_idx]
        linestyle = self.linetype_choices[self.linetype_idx]
        self.image = ImageFromXY(self.x, self.y, dpi=self.dpi,
                                 linecolor=linecolor, linestyle=linestyle)

    def _linetype_choices_default(self):
        # TODO: make these human readable instead of matplotlib standard
        return ['-', '--', ':', 'o']

    def _linecolor_choices_default(self):
        return ['k', 'b', 'g', 'r']

def start_ipython(model):
    shell = InteractiveShellEmbed()
    shell()

def main():
    with enaml.imports():
        from xy_view import Main
    model = XYModel()
    view = Main(model=model)
    app = QtLocalApplication()
    app.serve('main', view)
    #thread = threading.Thread(target=start_ipython, args=(model,))
    #thread.start()
    app.mainloop()

if __name__ == '__main__':
    main()
