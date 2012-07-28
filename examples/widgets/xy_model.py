import threading
import numpy as np
from traits.api import HasTraits, Array, Int, Float, Instance, on_trait_change, Property
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

    def __init__(self):
        super(XYModel, self).__init__()
        self.update_image()

    @on_trait_change('N, xmax, omega')
    def update_image(self):
        self.x = np.linspace(0, self.xmax, self.N)
        self.y = np.sin(2 * np.pi * self.omega * self.x)
        self.image = ImageFromXY(self.x, self.y)


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
