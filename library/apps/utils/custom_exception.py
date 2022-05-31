class BaseLibraryException(Exception):
    def __init__(self, status_code=None, detail=None, error_type=None, extra=None, **kwargs):

        super().__init__(self, detail)
        self.atidls_status_code = status_code
        self.extra = extra
        self.error_type = error_type

        # Parsed error message
        try:
            # if we receive str/bytes we try to convert to unicode/str to have consistent message types
            self.detail = detail.decode()
        except Exception:
            self.detail = detail
        # Easily convert a list to a string for display
        if isinstance(self.detail, list):
            self.detail = ', '.join(map(str, self.detail))

    def __str__(self):
        return f"{self.detail}"


# raise exception function
def raise_library_exception(status_code: int, detail=None, error_type=None, extra=None, **kwargs):
    raise BaseLibraryException(status_code=status_code, detail=detail, extra=extra,
                              error_type=error_type, **kwargs)