from django.http import HttpResponse
from django.template.loader import render_to_string


def render_to_response(template_name, data_dictionary, **kwargs):
    """
      Returns a HttpResponse whose content is filled with the result of calling
      lookup.get_template(args[0]).render with the passed arguments.
    """
    return HttpResponse(render_to_string(template_name, data_dictionary), **kwargs)
