from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InfoReply(_message.Message):
    __slots__ = ["company", "made_in", "price", "res_name"]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    MADE_IN_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    RES_NAME_FIELD_NUMBER: _ClassVar[int]
    company: str
    made_in: str
    price: int
    res_name: str
    def __init__(self, res_name: _Optional[str] = ..., price: _Optional[int] = ..., company: _Optional[str] = ..., made_in: _Optional[str] = ...) -> None: ...

class InfoRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
