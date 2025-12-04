from typing import Literal, cast

GetExpired = Literal["ALL", "FALSE", "TRUE"]

GET_EXPIRED_VALUES: set[GetExpired] = {
    "ALL",
    "FALSE",
    "TRUE",
}


def check_get_expired(value: str) -> GetExpired:
    if value in GET_EXPIRED_VALUES:
        return cast(GetExpired, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_EXPIRED_VALUES!r}")
