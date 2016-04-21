import sys


class HyperTrackException(Exception):
    '''
    Base exception for all exceptions raised by HyperTrack library
    '''
    def __init__(self, message=None, http_body=None, http_status=None,
                 headers=None):
        super(HyperTrackException, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except:
                http_body = ('<Could not decode body as utf-8. '
                             'Please report to support@hypertrack.io>')

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.headers = headers or {}

    def __unicode__(self):
        msg = self._message or "<empty message>"
        return u'{0}'.format(msg)

    if sys.version_info > (3, 0):
        def __str__(self):
            return self.__unicode__()
    else:
        def __str__(self):
            return unicode(self).encode('utf-8')


class APIException(HyperTrackException):
    pass


class APIConnectionException(HyperTrackException):
    pass


class InvalidRequestException(HyperTrackException):
    pass


class AuthenticationException(HyperTrackException):
    pass


class RateLimitException(HyperTrackException):
    pass
