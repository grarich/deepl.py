import aiohttp
import requests

__all__ = [
    'DeepLException',
    'HTTPException',
    'BadRequest',
    'Forbidden',
    'NotFound',
    'PayloadTooLarge',
    'URITooLong',
    'TooManyRequests',
    'QuotaExceeded',
    'ServiceUnavailable',
    'InternalServerError'
]


class DeepLException(Exception):
    pass


class HTTPException(DeepLException):
    """Exception raised when an HTTP request fails.
    Attributes
    ------------
    response: Union[:class:`aiohttp.ClientResponse`, :class:`requests.Response`]
        If you are using the RequestsAdapter,
        :class:`requests.Response`.
        If you are using the AiohttpAdapter,
        :class:`aiohttp.ClientResponse`.
    message: :class:`str`
        The Messages returned by DeepL API.
    status: :class:`int`
        The status code of the HTTP request.
    """

    def __init__(self, response, messega) -> None:
        self.response = response
        self.message = messega or 'No error message was sent from the DeepL API.'
        if isinstance(response, aiohttp.ClientResponse):
            self.status = response.status
        elif isinstance(response, requests.Response):
            self.status = response.status_code

        super().__init__(f'{self.status} {response.reason}: {self.message}')


class BadRequest(HTTPException):
    """Bad request. Please check error message and your parameters.

    Subclass of :exc:`HTTPException`
    """
    pass


class Forbidden(HTTPException):
    """Authorization failed. Please supply a valid auth_key parameter.

    Subclass of :exc:`HTTPException`
    """
    pass


class NotFound(HTTPException):
    """The requested resource could not be found.

    Subclass of :exc:`HTTPException`
    """
    pass


class PayloadTooLarge(HTTPException):
    """The request size exceeds the limit.

    Subclass of :exc:`HTTPException`
    """
    pass


class URITooLong(HTTPException):
    """The request URL is too long.
    You can avoid this error by using a POST request instead of a GET request.

    Subclass of :exc:`HTTPException`
    """
    pass


class TooManyRequests(HTTPException):
    """Too many requests. Please wait and resend your request.

    Subclass of :exc:`HTTPException`
    """
    pass


class QuotaExceeded(HTTPException):
    """Quota exceeded. The character limit has been reached.

    Subclass of :exc:`HTTPException`
    """
    pass


class ServiceUnavailable(HTTPException):
    """Resource currently unavailable. Try again later.

    Subclass of :exc:`HTTPException`
    """
    pass


class InternalServerError(HTTPException):
    """	Internal error

    Subclass of :exc:`HTTPException`
    """
    pass
