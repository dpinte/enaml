import wx

from traits.api import implements

from .wx_container import WXContainer
from .util import compute_sizer_flags

from ..group import IGroupImpl

from ...enums import Direction

            
class WXGroup(WXContainer):
    """ A wxPython implementation of IGroup.

    The WXGroup uses a wxBoxSizer to arrange its child components.

    See Also
    --------
    IGroup

    """
    implements(IGroupImpl)

    #---------------------------------------------------------------------------
    # IGroupImpl interface
    #---------------------------------------------------------------------------
    def create_widget(self):
        """ Creates the underlying sizer for the group. 

        """
        self.widget = self.make_sizer(self.parent.direction)
        
    def initialize_widget(self):
        """ Nothing to initialize on a group.

        """
        pass

    def layout_child_widgets(self):
        """ Adds the children of this container to the sizer.

        """
        sizer = self.widget
        for child in self.parent.children:
            flags = compute_sizer_flags(child.style)
            sizer.AddF(child.toolkit_impl.widget, flags)
        sizer.Layout()

    def parent_direction_changed(self, direction):
        """ The change handler for the 'direction' attribute on the 
        parent.

        """
        pass
    
    #---------------------------------------------------------------------------
    # Implementation
    #---------------------------------------------------------------------------
    def make_sizer(self, direction):
        """ Creates a wxBoxSizer for the given direction value. Not
        meant for public consumption.

        """
        dirs = (Direction.LEFT_TO_RIGHT, Direction.RIGHT_TO_LEFT)
        if direction in dirs:
            sizer = wx.BoxSizer(wx.HORIZONTAL)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
        return sizer
        
    def is_reverse_direction(self, direction):
        """ Returns True or False depending on if the given direction
        is reversed from normal. Not meant for public consumption.

        """
        dirs = (Direction.RIGHT_TO_LEFT, Direction.BOTTOM_TO_TOP)
        return direction in dirs

