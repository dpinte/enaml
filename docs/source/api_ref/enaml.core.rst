enaml.core
==========

The :py:mod:`enaml.core` package contains all of the core functionality of the
|Enaml|.

:mod:`base_component` Module
----------------------------

.. automodule:: enaml.core.base_component

:mod: `constructor` Module

.. automodule:: enaml.core.constructor


:mod:`enaml_ast` Module
-----------------------

.. inheritance-diagram:: enaml.core.enaml_ast
    :parts: 1

.. automodule:: enaml.core.enaml_ast

:mod:`enaml_compiler` Module
----------------------------

.. automodule:: enaml.core.enaml_compiler


:mod:`expressions` Module
-------------------------

.. inheritance-diagram::
    enaml.core.expressions
    :parts: 1

.. automodule:: enaml.core.expressions
    :special-members:
    :no-undoc-members:

:mod:`factory` Module
---------------------

.. automodule:: enaml.core.factory


:mod:`import_hooks` Module
--------------------------

.. automodule:: enaml.core.import_hooks


:mod:`inverters` Module
-----------------------

.. automodule:: enaml.core.inverters


:mod:`item_model` Module
------------------------

.. currentmodule:: enaml.core.item_model

.. Sphinx has problems with the Singal class and the attributeinstance
   directive cannot regognaze the Signal() type. so we have to manually
   describe the attributes and specifically request to document the
   methods.

.. autoclass:: AbstractItemModel
    :no-members:
    :members: begin_insert_columns,
      begin_move_columns,
      begin_remove_columns,
      end_insert_columns,
      end_move_columns,
      end_remove_columns,
      begin_insert_rows,
      begin_move_rows,
      begin_remove_rows,
      end_insert_rows,
      end_move_rows,
      end_remove_rows,
      begin_change_layout,
      end_change_layout,
      begin_reset_model,
      end_reset_model,
      notify_data_changed,
      notify_horizontal_header_data_changed,
      notify_vertical_header_data_changed,
      sibling,
      buddy,
      can_fetch_more,
      fetch_more,
      has_index,
      has_children,
      create_index,
      flags,
      column_count,
      row_count,
      index,
      parent,
      data,
      decoration,
      edit_data,
      tool_tip,
      status_tip,
      whats_this,
      font,
      alignment,
      background,
      foreground,
      check_state,
      set_data,
      set_check_state,
      horizontal_header_data,
      vertical_header_data,
      horizontal_header_decoration,
      vertical_header_decoration,
      horizontal_header_tool_tip,
      vertical_header_tool_tip,
      horizontal_header_status_tip,
      vertical_header_status_tip,
      horizontal_header_whats_this,
      vertical_header_whats_this,
      horizontal_header_font,
      vertical_header_font,
      horizontal_header_alignment,
      vertical_header_alignment,
      horizontal_header_background,
      vertical_header_background,
      horizontal_header_foreground,
      vertical_header_foreground,
      horizontal_header_size_hint,
      vertical_header_size_hint

    **Signals**
    .. autoinstanceattribute:: columns_about_to_be_inserted
    .. autoinstanceattribute:: columns_about_to_be_moved
    .. autoinstanceattribute:: columns_about_to_be_removed
    .. autoinstanceattribute:: columns_inserted
    .. autoinstanceattribute:: columns_moved
    .. autoinstanceattribute:: columns_removed
    .. autoinstanceattribute:: rows_about_to_be_inserted
    .. autoinstanceattribute:: rows_about_to_be_moved
    .. autoinstanceattribute:: rows_about_to_be_removed
    .. autoinstanceattribute:: rows_inserted
    .. autoinstanceattribute:: rows_moved
    .. autoinstanceattribute:: rows_removed
    .. autoinstanceattribute:: layout_about_to_be_changed
    .. autoinstanceattribute:: layout_changed
    .. autoinstanceattribute:: model_about_to_be_reset
    .. autoinstanceattribute:: model_reset
    .. autoinstanceattribute:: data_changed
    .. autoinstanceattribute:: horizontal_header_data_changed
    .. autoinstanceattribute:: vertical_header_data_changed

.. autoclass:: AbstractTableModel

.. autoclass:: AbstractListModel

.. autoclass:: ModelIndex

:mod:`lexer` Module
-------------------

.. currentmodule:: enaml.core.lexer

.. EnamlLexer has too many small methods that generate tokens but are consufed
   by autodoc as docstrings. So we only document the normal functions. A better
   solution would be to use the skip-members hook of autodoc.

.. autoclass:: EnamlLexer
    :no-members:
    :members: __init__,  input, token, dedent, indent,
        make_token_stream, create_strings, annotate_indentation_state,
        synthesize_indentation_tokens, add_endmarker


:mod:`monitors` Module
----------------------

.. automodule:: enaml.core.monitors


:mod:`operators` Module
-----------------------

.. automodule:: enaml.core.operators


:mod:`parser` Module
--------------------

.. automodule:: enaml.core.parser


:mod:`signaling` Module
-----------------------

.. automodule:: enaml.core.signaling

:mod:`toolkit` Module
---------------------

.. automodule:: enaml.core.toolkit

:mod:`trait_types` Module
-------------------------

.. automodule:: enaml.core.trait_types


Sub-packages
-----------------------

.. toctree::

        enaml.core.parse_tab

