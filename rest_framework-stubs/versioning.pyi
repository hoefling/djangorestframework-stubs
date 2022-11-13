from typing import Any, Mapping, Optional, Pattern, Sequence

from rest_framework.request import Request

class BaseVersioning:
    default_version: Optional[str]
    allowed_versions: Optional[Sequence[str]]
    version_param: str
    def determine_version(self, request: Request, *args: Any, **kwargs: Any) -> str: ...
    def reverse(
        self,
        viewname: str,
        args: Optional[Sequence[Any]] = ...,
        kwargs: Optional[Mapping[str, Any]] = ...,
        request: Optional[Request] = ...,
        format: Optional[str] = ...,
        **extra: Any
    ) -> str: ...
    def is_allowed_version(self, version: Optional[str]) -> bool: ...

class AcceptHeaderVersioning(BaseVersioning):
    invalid_version_message: str

class URLPathVersioning(BaseVersioning):
    invalid_version_message: str

class NamespaceVersioning(BaseVersioning):
    invalid_version_message: str
    def get_versioned_viewname(self, viewname: str, request: Request) -> str: ...

class HostNameVersioning(BaseVersioning):
    hostname_regex: Pattern
    invalid_version_message: str

class QueryParameterVersioning(BaseVersioning):
    invalid_version_message: str
