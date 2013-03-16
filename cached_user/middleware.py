try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

class ThreadLocals(object):
    """ Middleware that gets various objects from the request object and saves
    them in thread local storage.
    """
    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)
