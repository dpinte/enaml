#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import Instance
from enable.component import Component as EnableComponent

from .constraints_widget import ConstraintsWidget


class EnableCanvas(ConstraintsWidget):
    """ An Enable canvas widget that will draw any Enable Component
    object.
    
    """
    #: The enable.component.Component instance to draw.
    component = Instance(EnableComponent)

    #: An EnableCanvas ignores its hug_width by default, so that it
    #: expands freely in width.
    hug_width = 'ignore'
    
    #: An Enable Canvas ignore its hug_height by default, so that it
    #: expands freely in height.
    hug_height = 'ignore'


    #--------------------------------------------------------------------------
    # Initialization
    #--------------------------------------------------------------------------
    def snapshot(self):
        """ Returns the dict of creation attributes for the combo box.

        """
        snap = super(EnableCanvas, self).snapshot()
        snap['component'] = self.component
        return snap

    def bind(self):
        """ A method called after initialization which allows the widget
        to bind any event handlers necessary.

        """
        super(EnableCanvas, self).bind()
        self.publish_attributes('component')



