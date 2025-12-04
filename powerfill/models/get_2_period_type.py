from typing import Literal, cast

Get2PeriodType = Literal["ALL", "FROM_TO", "LAST_10", "LAST_30", "LAST_90", "TODAY"]

GET_2_PERIOD_TYPE_VALUES: set[Get2PeriodType] = {
    "ALL",
    "FROM_TO",
    "LAST_10",
    "LAST_30",
    "LAST_90",
    "TODAY",
}


def check_get_2_period_type(value: str) -> Get2PeriodType:
    if value in GET_2_PERIOD_TYPE_VALUES:
        return cast(Get2PeriodType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_2_PERIOD_TYPE_VALUES!r}")
