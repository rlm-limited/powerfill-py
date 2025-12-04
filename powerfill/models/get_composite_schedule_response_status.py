from typing import Literal, cast

GetCompositeScheduleResponseStatus = Literal["ACCEPTED", "REJECTED"]

GET_COMPOSITE_SCHEDULE_RESPONSE_STATUS_VALUES: set[GetCompositeScheduleResponseStatus] = {
    "ACCEPTED",
    "REJECTED",
}


def check_get_composite_schedule_response_status(value: str) -> GetCompositeScheduleResponseStatus:
    if value in GET_COMPOSITE_SCHEDULE_RESPONSE_STATUS_VALUES:
        return cast(GetCompositeScheduleResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_COMPOSITE_SCHEDULE_RESPONSE_STATUS_VALUES!r}")
