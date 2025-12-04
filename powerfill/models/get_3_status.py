from typing import Literal, cast

Get3Status = Literal["ACCEPTED", "CANCELLED", "USED", "WAITING"]

GET_3_STATUS_VALUES: set[Get3Status] = {
    "ACCEPTED",
    "CANCELLED",
    "USED",
    "WAITING",
}


def check_get_3_status(value: str) -> Get3Status:
    if value in GET_3_STATUS_VALUES:
        return cast(Get3Status, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_3_STATUS_VALUES!r}")
