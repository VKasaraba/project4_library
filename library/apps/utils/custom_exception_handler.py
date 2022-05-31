from rest_framework.response import Response
from library.apps.utils.custom_exception import BaseLibraryException, raise_library_exception


def _handle_library_exceptions(func):
    ''' Decorator for functions to catch library exceptions and return proper responses '''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseLibraryException as e:
            error_body = {
                'detail': e.detail,
                'extra': e.extra,
                'error_type': e.error_type,
            }
            return Response(error_body, e.library_status_code)
    return wrapper


def handle_library_exceptions(cls):
    class NewCls(cls):
        ''' Decorator for view classed to manage allowed and not allowed methods and return proper responses '''
        METHODS = {'get', 'post', 'put', 'patch', 'delete'}

        def __init__(self, *args, **kwargs):
            super(cls, self).__init__(*args, **kwargs)  # init parent class

            @_handle_library_exceptions  # decorator to catch thrown library exception and return proper response
            def raise_method_not_allowed_exception(self, request):  # will be called for not allowed methods
                raise_library_exception(405, 'Cannot perform this action', 'method_not_allowed')

            self.included_methods = {
                method for method in self.METHODS if method in dir(self) and callable(getattr(self, method))
            }   # set of methods allowed in this view
            self.excluded_methods = self.METHODS - self.included_methods  # set of methods not allowed in this view

            for method in self.included_methods:    # for each allowed method catch library exceptions
                if callable(getattr(self, method)):
                    setattr(self, method, _handle_library_exceptions(getattr(self, method)))

            for excluded_method in self.excluded_methods:  # for each not allowed method throw library exception
                setattr(cls, excluded_method, raise_method_not_allowed_exception)

    return NewCls
