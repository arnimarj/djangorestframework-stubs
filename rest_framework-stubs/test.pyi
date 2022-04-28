from typing import Any, Dict, Optional, Union

import coreapi
import requests
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.test import testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
import urllib3

def force_authenticate(
    request: HttpRequest, user: Optional[Union[AnonymousUser, AbstractBaseUser]] = ..., token: Optional[Token] = ...
) -> None: ...

class HeaderDict(urllib3._collections.HTTPHeaderDict):
    def get_all(self, key: Any, default: Any): ...

class MockOriginalResponse:
    msg: Any = ...
    closed: bool = ...
    def __init__(self, headers: Any) -> None: ...
    def isclosed(self): ...
    def close(self) -> None: ...

class DjangoTestAdapter(requests.adapters.HTTPAdapter):
    app: Any = ...
    factory: Any = ...
    def __init__(self) -> None: ...
    def get_environ(self, request: Request): ...
    def send(self, request: Request, *args: Any, **kwargs: Any) -> requests.Response: ...  # type: ignore[override]
    def close(self) -> None: ...

class RequestsClient(requests.Session): ...

class CoreAPIClient(coreapi.Client):
    def __init__(self, *args: Any, **kwargs: Any): ...
    @property
    def session(self): ...

class APIRequestFactory(DjangoRequestFactory):
    renderer_classes_list: Any = ...
    default_format: Any = ...
    enforce_csrf_checks: Any = ...
    renderer_classes: Any = ...
    def __init__(self, enforce_csrf_checks: bool = ..., **defaults: Any) -> None: ...
    def request(self, **kwargs: Any) -> Request: ...  # type: ignore[override]
    def get(self, path: str, data: Optional[Union[Dict[str, Any], str]] = ..., follow: bool = ..., **extra: Any): ...  # type: ignore[override]
    def post(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def put(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def patch(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def delete(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def options(self, path: str, data: Union[Dict[str, str], str] = ..., format: Optional[str] = ..., content_type: Optional[Any] = ..., follow: bool = ..., **extra: Any) -> Request: ...  # type: ignore[override]
    def generic(  # type: ignore[override]
        self, method: str, path: str, data: str = ..., content_type: str = ..., secure: bool = ..., **extra: Any
    ) -> Request: ...

class ForceAuthClientHandler(ClientHandler):
    def __init__(self, *args: Any, **kwargs: Any): ...
    def get_response(self, request: Request) -> Response: ...  # type: ignore[override]

class APIClient(APIRequestFactory, DjangoClient):
    handler: Any = ...
    def credentials(self, **kwargs: Any): ...
    def force_authenticate(
        self, user: Union[AnonymousUser, AbstractBaseUser] = ..., token: Optional[Token] = ...
    ) -> None: ...
    def request(self, **kwargs: Any) -> Response: ...  # type: ignore[override]
    def get(self, path: str, data: Optional[Union[Dict[str, Any], str]] = ..., follow: bool = ..., **extra: Any): ...  # type: ignore[override]
    def post(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Response: ...  # type: ignore[override]
    def put(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Response: ...  # type: ignore[override]
    def patch(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Response: ...  # type: ignore[override]
    def delete(self, path: str, data: Optional[Any] = ..., format: Optional[str] = ..., content_type: Optional[str] = ..., follow: bool = ..., **extra: Any) -> Response: ...  # type: ignore[override]
    def options(self, path: str, data: Union[Dict[str, str], str] = ..., format: Optional[str] = ..., content_type: Optional[Any] = ..., follow: bool = ..., **extra: Any) -> Response: ...  # type: ignore[override]
    def logout(self) -> None: ...

class APITransactionTestCase(testcases.TransactionTestCase):
    client_class: type[APIClient] = ...

class APITestCase(testcases.TestCase):
    client_class: type[APIClient] = ...

class APISimpleTestCase(testcases.SimpleTestCase):
    client_class: type[APIClient] = ...

class APILiveServerTestCase(testcases.LiveServerTestCase):
    client_class: type[APIClient] = ...

class URLPatternsTestCase(testcases.SimpleTestCase): ...
