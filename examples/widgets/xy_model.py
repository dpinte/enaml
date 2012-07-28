import threading
import numpy as np
from traits.api import HasTraits, Array, Int, Float, Instance, on_trait_change
import enaml
from enaml.qt.qt_local_application import QtLocalApplication
from enaml.noncomponents.image import ImageFromXY
from IPython.frontend.terminal.embed import InteractiveShellEmbed


class XYModel(HasTraits):
    N = Int(100)
    x = Array()
    y = Array()
    # TODO: the image should really be in a plot model, not the data model
    image = Instance(ImageFromXY)

    def __init__(self):
        self.update_image()

    @on_trait_change('N')
    def update_image(self):
        self.x = np.linspace(0, 4 * np.pi, self.N)
        self.y = np.sin(self.x)
        self.image = ImageFromXY(self.x, self.y)

    def set_view(self, view):
        self.view = view
        container = view.children[0]
        #self.plot = container.plot

    def _N_changed(self):
        self.update_image()


def start_ipython(model):
    shell = InteractiveShellEmbed()
    shell()

def main():
    with enaml.imports():
        from xy_view import Main
    model = XYModel()
    view = Main(model=model)
    model.set_view(view)
    app = QtLocalApplication()
    app.serve('main', view)
    thread = threading.Thread(target=start_ipython, args=(model,))
    thread.start()
    app.mainloop()

if __name__ == '__main__':
    main()
