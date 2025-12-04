from typing import Literal, cast

Get2Type = Literal["ACTIVE", "ALL", "STOPPED"]

GET_2_TYPE_VALUES: set[Get2Type] = {
    "ACTIVE",
    "ALL",
    "STOPPED",
}


def check_get_2_type(value: str) -> Get2Type:
    if value in GET_2_TYPE_VALUES:
        return cast(Get2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_2_TYPE_VALUES!r}")
