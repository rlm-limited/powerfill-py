from typing import Literal, cast

Get3PeriodType = Literal["ACTIVE", "FROM_TO"]

GET_3_PERIOD_TYPE_VALUES: set[Get3PeriodType] = {
    "ACTIVE",
    "FROM_TO",
}


def check_get_3_period_type(value: str) -> Get3PeriodType:
    if value in GET_3_PERIOD_TYPE_VALUES:
        return cast(Get3PeriodType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_3_PERIOD_TYPE_VALUES!r}")
