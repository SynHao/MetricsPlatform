# Values for template_lib parameter
from django.template import RequestContext
from django.template.context_processors import csrf
from django.shortcuts import render as django_render

from Sql.lib import django_mako

DJANGO = 'django'
MAKO = 'mako'


def is_jframe_request(request):
    """
      The JFrame container uses ?format=embed to request
      embeddable contents, and expects an HTTP response
      with some extra headers set in return.
      The extra headers are set in JFrameMiddleware.
      See also Hue.JFrame.js.
    """
    return request.META.get('HTTP_X_HUE_JFRAME') or \
           request.GET.get('format') == 'embed'


def _get_template_lib(template, kwargs):
    template_lib = kwargs.get('template_lib')
    if 'template_lib' in kwargs:
        del kwargs['template_lib']

    # Default based on file extension
    if template_lib is None:
        if template.endswith('.mako'):
            return MAKO
        else:
            return DJANGO
    return template_lib


def _render_to_response(template, request, *args, **kwargs):
    template_lib = _get_template_lib(template, kwargs)
    if template_lib == DJANGO:
        kwargs.update(csrf(request))
        return django_render(request, template, *args, **kwargs)
    elif template_lib == MAKO:
        return django_mako.render_to_response(template, *args, **kwargs)
    else:
        raise Exception("Bad template lib: %s" % template_lib)


def render(template, request, data, json=None, template_lib=None, force_template=False, status=200, **kwargs):
    """
      Render() is the main shortcut/workhorse for rendering view responses.
      It takes a template (either ".mako" or ".html", or influenced by
      template_lib), as well as as arbitrary data.

      It typically renders to an HttpResponse.  If the request is a non-JFrame
      AJAX request (or if data is None), it renders into JSON.

      if force-template is True, will render the non-AJAX template response even if the
      request is via AJAX. This is to facilitate fetching HTML fragments.
    """
    # request.ajax is defined in the AjaxMiddleware. But we might hit
    # errors before getting to that point.
    is_ajax = getattr(request, "ajax", False)
    if data is None:
        data = {}

    if not force_template and not is_jframe_request(request) and (is_ajax or template is None):
        if json is not None:
            print('json is not none')
            # return render_json(json, request.GET.get("callback"), status=status)
        else:
            print('json is none')
    else:
        data.update({'user': 'SynHao'})
        return _render_to_response(template,
                                   request,
                                   RequestContext(request, data),
                                   template_lib=template_lib,
                                   status=status,
                                   **kwargs)
