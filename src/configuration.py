class Configuration(object):

    def __init__(self,
                 base_url,
                 timeout,
                 window_width,
                 window_height):

        self._base_url = base_url
        self._timeout = timeout
        self._window_width = window_width
        self._window_height = window_height

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def timeout(self) -> int:
        return self._timeout

    @property
    def window_width(self) -> int:
        return self._window_width

    @property
    def window_height(self) -> int:
        return self._window_height

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @window_width.setter
    def window_width(self, value):
        self._window_width = value

    @window_height.setter
    def window_height(self, value):
        self._window_height = value

