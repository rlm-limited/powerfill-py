from typing import Literal, cast

GetOverview2RecurrencyKind = Literal["DAILY", "WEEKLY"]

GET_OVERVIEW_2_RECURRENCY_KIND_VALUES: set[GetOverview2RecurrencyKind] = {
    "DAILY",
    "WEEKLY",
}


def check_get_overview_2_recurrency_kind(value: str) -> GetOverview2RecurrencyKind:
    if value in GET_OVERVIEW_2_RECURRENCY_KIND_VALUES:
        return cast(GetOverview2RecurrencyKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_OVERVIEW_2_RECURRENCY_KIND_VALUES!r}")
