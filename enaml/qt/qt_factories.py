#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
def calendar_factory():
    from .qt_calendar import QtCalendar
    return QtCalendar


def check_box_factory():
    from .qt_check_box import QtCheckBox
    return QtCheckBox


def combo_box_factory():
    from .qt_combo_box import QtComboBox
    return QtComboBox


def container_factory():
    from .qt_container import QtContainer
    return QtContainer


def date_edit_factory():
    from .qt_date_edit import QtDateEdit
    return QtDateEdit


def datetime_edit_factory():
    from .qt_datetime_edit import QtDatetimeEdit
    return QtDatetimeEdit


def dialog_factory():
    from .qt_dialog import QtDialog
    return QtDialog


def field_factory():
    from .qt_field import QtField
    return QtField


def html_factory():
    from .qt_html import QtHtml
    return QtHtml


def image_view_factory():
    from .qt_image_view import QtImageView
    return QtImageView


def label_factory():
    from .qt_label import QtLabel
    return QtLabel


def push_button_factory():
    from .qt_push_button import QtPushButton
    return QtPushButton


def progress_bar_factory():
    from .qt_progress_bar import QtProgressBar
    return QtProgressBar


def radio_button_factory():
    from .qt_radio_button import QtRadioButton
    return QtRadioButton


def slider_factory():
    from .qt_slider import QtSlider
    return QtSlider


def spin_box_factory():
    from .qt_spin_box import QtSpinBox
    return QtSpinBox


def window_factory():
    from .qt_window import QtWindow
    return QtWindow


QT_FACTORIES = {
    'Calendar': calendar_factory,
    'CheckBox': check_box_factory,
    'ComboBox': combo_box_factory,
    'Container': container_factory,
    'DateEdit': date_edit_factory,
    'DatetimeEdit': datetime_edit_factory,
    'Dialog': dialog_factory,
    'Field': field_factory,
    'Html': html_factory,
    'ImageView': image_view_factory,
    'Label': label_factory,
    'PushButton': push_button_factory,
    'ProgressBar': progress_bar_factory,
    'RadioButton': radio_button_factory,
    'Slider': slider_factory,
    'SpinBox': spin_box_factory,
    'Window': window_factory,
}
