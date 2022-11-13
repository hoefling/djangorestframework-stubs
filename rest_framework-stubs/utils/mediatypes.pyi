from typing import Any

def media_type_matches(lhs: Any, rhs: Any): ...
def order_by_precedence(media_type_lst: Any): ...

class _MediaType:
    orig: Any
    def __init__(self, media_type_str: Any) -> None: ...
    def match(self, other: Any): ...
    @property
    def precedence(self): ...
