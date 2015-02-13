from django import template

from .. import models

register = template.Library()

class PagerContentNode(template.Node):
    def __init__(self, slug, context_var=None):
        self.slug = slug
        self.context_var = context_var

    def render(self, context):
        pager_content = models.Pager.get(slug=self.slug)
        if not self.context_var:
            return pager_content
        else:
            context[self.context_var] = pager_content
        return ''

def do_pagercontent(parser, token):
    """
    Retrieves content from the ``Pager`` model given a slug, and
    optionally stores it in a context variable.
    
    Usage::
    
        {% pager [slug] %}

    To get the pager into a variable for later use in the template or
    with tags and filters::
    
        {% pager [slug] as [varname] %}
    
    """
    bits = token.split_contents()
    len_bits = len(bits)
    varname = None
    if len_bits not in (2, 4, 6):
        raise template.TemplateSyntaxError("The pager tag requires "
                                           "1, 3, or 5 arguments")

    try:
        context_var = bits[bits.index('as') + 1]
    except ValueError:
        context_var = None

    if len_bits > 2 and context_var is None:
        raise template.TemplateSyntaxError("The second or fourth argument should be 'as' or 'for-site'")

    return PagerContentNode(bits[1], context_var=context_var)

register.tag('pager', do_pagercontent)
