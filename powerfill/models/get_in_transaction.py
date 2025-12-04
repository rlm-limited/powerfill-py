from typing import Literal, cast

GetInTransaction = Literal["ALL", "FALSE", "TRUE"]

GET_IN_TRANSACTION_VALUES: set[GetInTransaction] = {
    "ALL",
    "FALSE",
    "TRUE",
}


def check_get_in_transaction(value: str) -> GetInTransaction:
    if value in GET_IN_TRANSACTION_VALUES:
        return cast(GetInTransaction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_IN_TRANSACTION_VALUES!r}")
