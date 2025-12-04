from typing import Literal, cast

ClearChargingProfileParamsFilterType = Literal["ChargingProfileId", "OtherParameters"]

CLEAR_CHARGING_PROFILE_PARAMS_FILTER_TYPE_VALUES: set[ClearChargingProfileParamsFilterType] = {
    "ChargingProfileId",
    "OtherParameters",
}


def check_clear_charging_profile_params_filter_type(value: str) -> ClearChargingProfileParamsFilterType:
    if value in CLEAR_CHARGING_PROFILE_PARAMS_FILTER_TYPE_VALUES:
        return cast(ClearChargingProfileParamsFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLEAR_CHARGING_PROFILE_PARAMS_FILTER_TYPE_VALUES!r}")
