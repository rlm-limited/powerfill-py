from typing import Literal, cast

ChangeAvailabilityParamsAvailType = Literal["INOPERATIVE", "OPERATIVE"]

CHANGE_AVAILABILITY_PARAMS_AVAIL_TYPE_VALUES: set[ChangeAvailabilityParamsAvailType] = {
    "INOPERATIVE",
    "OPERATIVE",
}


def check_change_availability_params_avail_type(value: str) -> ChangeAvailabilityParamsAvailType:
    if value in CHANGE_AVAILABILITY_PARAMS_AVAIL_TYPE_VALUES:
        return cast(ChangeAvailabilityParamsAvailType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_AVAILABILITY_PARAMS_AVAIL_TYPE_VALUES!r}")
