import wx

from traits.api import implements, Bool

from .wx_control import WXControl
from ..line_edit import ILineEditImpl


class WXLineEdit(WXControl):
    """ A wxPython implementation of a LineEdit.

    The LineEdit uses a wx.TextCtrl and provides a single line of
    editable text.

    See Also
    --------
    LineEdit

    """
    implements(ILineEditImpl)

    #---------------------------------------------------------------------------
    # ILineEditImpl interface
    #---------------------------------------------------------------------------
    def create_widget(self):
        """ Creates the underlying wx.TextCtrl.

        """
        self.widget = wx.TextCtrl(parent=self.parent_widget(),
                                  style=wx.TE_PROCESS_ENTER)

    def initialize_widget(self):
        """ Initializes the attributes of the wx.TextCtrl.

        """
        parent = self.parent
        self.set_max_length(parent.max_length)
        self.set_read_only(parent.read_only)
        if not parent.text:
            self.change_text(parent.placeholder_text)
        else:
            self.change_text(parent.text)
        parent._modified = False
        self.set_cursor_position(parent.cursor_position)
        self.bind()

    def parent_max_length_changed(self, max_length):
        """ The change handler for the 'max_length' attribute on the 
        parent.

        """
        self.set_max_length(max_length)

    def parent_read_only_changed(self, read_only):
        """ The change handler for the 'read_only' attribute on the
        parent.

        """
        self.set_read_only(read_only)

    def parent_cursor_position_changed(self, cursor_position):
        """ The change handler for the 'cursor_position' attribute on 
        the parent.

        """
        if not self.setting_value:
            self.set_cursor_position(cursor_position)

    def parent_text_changed(self, text):
        """ The change handler for the 'text' attribute on the parent.

        """
        if not self.setting_value:
            self.change_text(text)
            self.parent._modified = False

    def set_selection(self, start, end):
        """ Sets the selection in the widget between the start and 
        end positions, inclusive.

        """
        self.widget.SetSelection(start, end)
        self.update_parent_selection()

    def select_all(self):
        """ Select all the text in the line edit.

        If there is no text in the line edit, the selection will be
        empty.

        """
        self.widget.SetSelection(-1, -1)
        self.update_parent_selection()

    def deselect(self):
        """ Deselect any selected text.

        Sets a selection with start == stop to deselect the current
        selection. The cursor is placed at the beginning of selection.

        """
        widget = self.widget
        start, end = widget.GetSelection()
        widget.SetSelection(start, start)
        self.update_parent_selection()

    def clear(self):
        """ Clear the line edit of all text.

        """
        self.widget.Clear()
        self.update_parent_selection()

    def backspace(self):
        """ Simple backspace functionality.

        If no text is selected, deletes the character to the left
        of the cursor. Otherwise, it deletes the selected text.

        """
        widget = self.widget
        start, end = widget.GetSelection()
        if start == end:
            start = end - 1
        widget.Remove(start, end)
        self.update_parent_selection()

    def delete(self):
        """ Simple delete functionality.

        If no text is selected, deletes the character to the right
        of the cursor. Otherwise, it deletes the selected text.

        """
        widget = self.widget
        start, end = widget.GetSelection()
        if start == end:
            end = end + 1
        widget.Remove(start, end)
        self.update_parent_selection()

    def end(self, mark=False):
        """ Moves the cursor to the end of the line.

        Arguments
        ---------
        mark : bool, optional
            If True, select the text from the current position to the end of
            the line edit. Defaults to False.

        """
        widget = self.widget
        if mark:
            start = widget.GetInsertionPoint()
            end = widget.GetLastPosition()
            widget.SetSelection(start, end)
        else:
            widget.SetInsertionPointEnd()
        self.update_parent_selection()

    def home(self, mark=False):
        """ Moves the cursor to the beginning of the line.

        Arguments
        ---------
        mark : bool, optional
            If True, select the text from the current position to
            the beginning of the line edit. Defaults to False.

        """
        widget = self.widget
        if mark:
            start = 0
            end = widget.GetInsertionPoint()
            widget.SetSelection(start, end)
        else:
            widget.SetInsertionPoint(0)
        self.update_parent_selection()

    def cut(self):
        """ Cuts the selected text from the line edit.

        Copies the selected text to the clipboard then deletes the selected
        text from the line edit.

        """
        self.widget.Cut()
        self.update_parent_selection()

    def copy(self):
        """ Copies the selected text to the clipboard.

        """
        self.widget.Copy()
        self.update_parent_selection()

    def paste(self):
        """ Paste the contents of the clipboard into the line edit.

        Inserts the contents of the clipboard into the line edit at
        the current cursor position, replacing any selected text.

        """
        self.widget.Paste()
        self.update_parent_selection()

    def insert(self, text):
        """ Insert the text into the line edit.

        Inserts the given text at the current cursor position,
        replacing any selected text.

        Arguments
        ---------
        text : str
            The text to insert into the line edit.

        """
        self.widget.WriteText(text)
        self.update_parent_selection()

    def undo(self):
        """ Undoes the last operation.

        """
        self.widget.Undo()
        self.update_parent_selection()

    def redo(self):
        """ Redoes the last operation

        """
        self.widget.Redo()
        self.update_parent_selection()

    #---------------------------------------------------------------------------
    # Implementation
    #---------------------------------------------------------------------------
    # A flag which set to True when we're applying updates to the 
    # model. Allows us to avoid unnecessary notification recursion.
    setting_value = Bool(False)

    def bind(self):
        """ Binds the event handlers for the wx.TextCtrl.

        """
        widget = self.widget
        widget.Bind(wx.EVT_TEXT_MAXLEN, self.on_max_length)
        widget.Bind(wx.EVT_TEXT, self.on_text_updated)
        widget.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter)
        widget.Bind(wx.EVT_LEFT_UP, self.on_selection)

    def on_text_updated(self, event):
        """ The event handler for the text update event.

        """
        widget = self.widget
        parent = self.parent
        self.setting_value = True
        parent.text = text = widget.GetValue()
        self.setting_value = False
        self.update_parent_selection()
        parent.text_edited = text
        parent._modified = True
        parent.text_changed = text

    def on_text_enter(self, event):
        """ The event handler for the return pressed event.

        """
        self.parent.return_pressed = True

    def on_max_length(self, event):
        """ The event handler for the max length event.

        """
        self.parent.max_length_reached = True

    def on_selection(self, event):
        """ The event handler for a selection (really a left up) event.

        """
        self.update_parent_selection()
        event.Skip()

    def update_parent_selection(self):
        """ Updates the selection and cursor position of the parent
        to reflect the current state of the widget.

        """
        parent = self.parent
        widget = self.widget
        parent._selected_text = widget.GetStringSelection()
        self.setting_value = True
        parent.cursor_position = widget.GetInsertionPoint()
        self.setting_value = False

    def change_text(self, text):
        """ Changes the text in the widget without emitted a text 
        updated event. This should be called when the text is changed
        programmatically.

        """
        self.widget.ChangeValue(text)

    def set_max_length(self, max_length):
        """ Sets the max length of the widget to max_length.

        """
        self.widget.SetMaxLength(max_length)
    
    def set_read_only(self, read_only):
        """ Sets read only state of the widget.

        """
        # XXX this may require some trickery in Windows to change
        # this value properly on the fly.
        self.widget.SetEditable(not read_only)

    def set_cursor_position(self, cursor_position):
        """ Sets the cursor position of the widget.

        """
        self.widget.SetInsertionPoint(cursor_position)

