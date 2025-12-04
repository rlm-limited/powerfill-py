from typing import Literal, cast

GetBlocked = Literal["ALL", "FALSE", "TRUE"]

GET_BLOCKED_VALUES: set[GetBlocked] = {
    "ALL",
    "FALSE",
    "TRUE",
}


def check_get_blocked(value: str) -> GetBlocked:
    if value in GET_BLOCKED_VALUES:
        return cast(GetBlocked, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_BLOCKED_VALUES!r}")
