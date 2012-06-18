Built-in Widgets
================

.. _built-ins-ref:

An Enaml widget is a toolkit-independent abstraction.
Each GUI toolkit that Enaml supports is a set of widgets that
have been implemented and exist in the :mod:`enaml.components` submodule.
A widget interface is not tied to any particular implementation.

Interface
---------

An Enaml widget's interface describes the attributes and events that the
widget exposes as its API. Enaml orchestrates communication between
user-facing views and the underlying graphical toolkits.

.. rubric:: Standard interfaces

.. currentmodule:: enaml.components

.. inheritance-diagram::
    abstract_item_view.AbstractItemView
    action.Action
    base_selection_model.BaseSelectionModel
    base_widget_component.BaseWidgetComponent
    bounded_date.BoundedDate
    bounded_datetime.BoundedDatetime
    calendar.Calendar
    check_box.CheckBox
    combo_box.ComboBox
    constraints_widget.ConstraintsWidget
    container.Container
    control.Control
    date_edit.DateEdit
    datetime_edit.DatetimeEdit
    dialog.Dialog
    directory_dialog.DirectoryDialog
    dock_pane.DockPane
    enable_canvas.EnableCanvas
    field.Field
    float_slider.FloatSlider
    file_dialog.FileDialog
    form.Form
    group_box.GroupBox
    html.Html
    image_view.ImageView
    include.Include
    inline.Inline
    label.Label
    list_view.ListView
    main_window.MainWindow
    menu_bar.MenuBar
    menu.Menu
    progress_bar.ProgressBar
    push_button.PushButton
    radio_button.RadioButton
    row_selection_model.RowSelectionModel
    scroll_area.ScrollArea
    slider.Slider
    spin_box.SpinBox
    splitter.Splitter
    tab_group.TabGroup
    table_view.TableView
    tab.Tab
    text_editor.TextEditor
    thumbnail_view.ThumbnailView
    toggle_button.ToggleButton
    toggle_control.ToggleControl
    tool_bar.ToolBar
    traitsui_item.TraitsUIItem
    tree_view.TreeView
    widger_component.WidgetComponent
    window.Window
    :parts: 1

Implementation
--------------

The available backends provide concrete versions of Enaml widget
interfaces. An interface utilizes an implementation-specific
class, which wraps an actual toolkit widget.

*Standard Implementations*

.. inheritance-diagram::
    abstract_item_view.AbstractTkItemView
    action.AbstractTkAction
    base_selection_model.AbstractTkBaseSelectionModel
    base_widget_component.AbstractTkBaseWidgetComponent
    bounded_date.AbstractTkBoundedDate
    bounded_datetime.AbstractTkBoundedDatetime
    calendar.AbstractTkCalendar
    check_box.AbstractTkCheckBox
    combo_box.AbstractTkComboBox
    constraints_widget.AbstractTkConstraintsWidget
    container.AbstractTkContainer
    control.AbstractTkControl
    date_edit.AbstractTkDateEdit
    datetime_edit.AbstractTkDatetimeEdit
    dialog.AbstractTkDialog
    directory_dialog.AbstractTkDirectoryDialog
    dock_pane.AbstractTkDockPane
    enable_canvas.AbstractTkEnableCanvas
    field.AbstractTkField
    float_slider.AbstractTkFloatSlider
    file_dialog.AbstractTkFileDialog
    form.AbstractTkForm
    group_box.AbstractTkGroupBox
    html.AbstractTkHtml
    image_view.AbstractTkImageView
    include.AbstractTkInclude
    inline.AbstractTkInline
    label.AbstractTkLabel
    list_view.AbstractTkListView
    main_window.AbstractTkMainWindow
    menu_bar.AbstractTkMenuBar
    menu.AbstractTkMenu
    progress_bar.AbstractTkProgressBar
    push_button.AbstractTkPushButton
    radio_button.AbstractTkRadioButton
    row_selection_model.AbstractTkRowSelectionModel
    scroll_area.AbstractTkScrollArea
    slider.AbstractTkSlider
    spin_box.AbstractTkSpinBox
    splitter.AbstractTkSplitter
    tab_group.AbstractTkTabGroup
    table_view.AbstractTkTableView
    tab.AbstractTkTab
    text_editor.AbstractTkTextEditor
    thumbnail_view.AbstractTkThumbnailView
    toggle_button.AbstractTkToggleButton
    toggle_control.AbstractTkToggleControl
    tool_bar.AbstractTkToolBar
    traitsui_item.AbstractTkTraitsUIItem
    tree_view.AbstractTkTreeView
    widger_component.AbstractTkWidgetComponent
    window.AbstractTkWindow
    :parts: 1

Standard Widgets
----------------

Abstract base widgets
^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    base_widget_component.BaseWidgetComponent
    widget_component.WidgetComponent
    constraints_widget.ConstraintsWidget
    control.Control
    toggle_control.ToggleControl
    bounded_date.BoundedDate
    abstract_item_view.AbstractItemView
    base_selection_model.BaseSelectionModel

Standard control widgets
^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    calendar.Calendar
    check_box.CheckBox
    combo_box.ComboBox
    push_button.PushButton
    radio_button.RadioButton
    field.Field
    image_view.ImageView
    label.Label
    slider.Slider
    spin_box.SpinBox
    datetime_edit.DatetimeEdit
    date_edit.DateEdit
    progress_bar.ProgressBar

Advanced widgets
^^^^^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    html.Html
    text_editor.TextEditor
    image_view.ImageView
    traitsui_item.TraitsUIItem
    enable_canvas.EnableCanvas

Window widgets
^^^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    window.Window
    main_window.MainWindow
    dialog.Dialog
    directory_dialog.DirectoryDialog
    file_dialog.FileDialog

Container and Layout widgets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    container.Container
    form.Form
    group_box.GroupBox
    tab.Tab
    splitter.Splitter
    scroll_area.ScrollArea
    tab_group.TabGroup
    dock_pane.DockPane


Item views
^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    list_view.ListView
    table_view.TableView
    tree_view.TreeView

Menu widgets
^^^^^^^^^^^^

.. autosummary::
    :toctree: widgets
    :template: widget.rst

    menu_bar.MenuBar
    menu.Menu

Standard library
^^^^^^^^^^^^^^^^

A number of additional widget types are available in the standard widget
library.  These are not top-level classes implemented in Python, but are instead
|Enaml| widgets implemented using ``enamldef`` declarations.

.. toctree::
   :maxdepth: 2

    Standard Widget Library <std_library_ref>

