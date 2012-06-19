# -*- coding: utf-8 -*-
"""
    A TraitAttribute Documenter
    (Subclassed extensively from the autodoc AttributeDocumenter)

    :copyright: Copyright 2012 by Enthought, Inc
"""
import inspect
import traceback
import sys

from sphinx.ext.autodoc import add_documenter, ClassLevelDocumenter

from traits.trait_handlers import TraitType
from traits.has_traits import MetaHasTraits
from traits.trait_types import BaseInstance, Undefined

def is_class_trait(name, cls):
    """ Check if the name is in the list of class traits of ``cls``."""
    return isinstance(cls, MetaHasTraits) and name in cls.__class_traits__

class TraitDocumenter(ClassLevelDocumenter):
    """ Specialized Documenter subclass for trait attributes.
    """
    objtype = 'traitattribute'
    directivetype = 'attribute'
    member_order = 60

    # must be higher than other attribute documenters
    priority = 12

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        """ Check that the document member is a trait instance.
        """
        check = (isattr and issubclass(type(member), TraitType) or
                 is_class_trait(membername, parent.object))
        return check


    def document_members(self, all_members=False):
        """ Trait attributes has no members """
        pass

    def import_object(self):
        """ Get the Trait object.

        Code adapted from autodoc.Documenter.import_object

        """
        try:
            __import__(self.modname)
            self.module = sys.modules[self.modname]
            current = self.module

            for part in self.objpath[:-1]: # the last item is the trait
                current = self.get_attr(current, part)

            name = self.objpath[-1]
            if isinstance(current, MetaHasTraits):
                # FIXME I am not sure about that need more testing
                self._is_class_trait = True
                obj = current.__class_traits__[name]
            else:
                self._is_class_trait = False
                obj = self.get_attr(current, name)

            self.object_name = name
            self.object = obj
            self.parent = current
            return True
        # this used to only catch SyntaxError, ImportError and AttributeError,
        # but importing modules with side effects can raise all kinds of errors
        except Exception, err:
            if self.env.app and not self.env.app.quiet:
                self.env.app.info(traceback.format_exc().rstrip())
            self.directive.warn(
                'autodoc can\'t import/find %s %r, it reported error: '
                '"%s", please check your spelling and sys.path' %
                (self.objtype, str(self.fullname), err))
            self.env.note_reread()
            return False

    def add_directive_header(self, sig):
        """ Add the directive header 'attribute' with the annotation
        option set to the trait name and default value of the trait.
        """
        ClassLevelDocumenter.add_directive_header(self, sig)
        if self._is_class_trait:
            # Class traits
            metatype = getattr(self.object, 'type')
            trait = self.object.trait_type
            if metatype == 'property':
                if inspect.isclass(trait):
                    value = trait.__name__
                else:
                    value = type(trait).__name__
                definition = u'= Property({0})'.format(value)
            elif metatype == 'trait':
                if isinstance(trait, BaseInstance):
                    klass = trait.klass
                    if inspect.isclass(klass):
                        klass_name = klass.__name__
                    else:
                        klass_name = repr(klass)
                    instance = type(trait).__name__
                    definition = u'= {0}({1})'.format(instance, klass_name)
                else:
                    name = type(trait).__name__
                    value = self.object.default_value()[1]
                    if value in (None, Undefined):
                        value = ''
                    else:
                        value = repr(value)
                    definition = u'= {0}({1})'.format(name, value)
            else:
                definition = u''
        else:
            name = type(self.object).__name__
            value = repr(self.object.default_value)
            definition = u'= {0}({1})'.format(name, value)

        self.add_line(u'   :annotation: ' + definition , '<autodoc>')

    def add_content(self, more_content, no_docstring=False):
        """Never try to get a docstring from the trait."""
        ClassLevelDocumenter.add_content(self, more_content, no_docstring=True)


add_documenter(TraitDocumenter)


def setup(app):
    pass