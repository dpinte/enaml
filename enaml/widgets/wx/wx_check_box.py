import wx

from traits.api import implements

from .wx_toggle_control import WXToggleControl

from ..check_box import ICheckBoxImpl


class WXCheckBox(WXToggleControl):
    """ A wxPython implementation of CheckBox.

    A Checkbox provides a toggleable control using a wx.CheckBox.

    See Also
    --------
    CheckBox

    """
    implements(ICheckBoxImpl)

    #---------------------------------------------------------------------------
    # ICheckBoxImpl interface
    #---------------------------------------------------------------------------
    def create_widget(self):
        """ Creates and the wx.CheckBox.

        """
        self.widget = wx.CheckBox(self.parent_widget())
        
    #---------------------------------------------------------------------------
    # Implementation
    #---------------------------------------------------------------------------
    def bind(self):
        """ Binds the event handlers for the check box. Not meant for
        public consumption.

        """
        widget = self.widget
        widget.Bind(wx.EVT_CHECKBOX, self.on_toggled)
        widget.Bind(wx.EVT_LEFT_DOWN, self.on_pressed)
        widget.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave_window)  

