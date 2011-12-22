from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.decorators import available_attrs
from django.utils.functional import wraps

def my_decorator(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if bongo:
            return HttpResponsePermanentRedirect(url)
        return view_func(request, *args, **kwargs)
    return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)
