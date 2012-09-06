#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from enable.api import Window as EnableWindow

from .qt_constraints_widget import QtConstraintsWidget


class QtEnableCanvas(QtConstraintsWidget):
    """ A Qt implementation of EnableCanvas

    FIXME: how do I prevent this to be used with a non local server?

    """
    window = None

    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create_widget(self, parent, tree):
        """ Create the underlying Enable widget.

        """
        self.window = EnableWindow(parent, component=None)
        widget = self.window.control
        # XXX Enable window doesn't parent on Qt (this is already fixed in Enable trunk)
        widget.setParent(parent)

        return widget

    def create(self, tree):
        """ Create and initialize the underlying widget.

        """
        super(QtEnableCanvas, self).create(tree)
        self.set_component(tree['component'])


    def set_component(self, component):
        self.window.component = component
        #self.window.redraw()
