from typing import Literal, cast

ClearChargingProfileParamsChargingProfilePurpose = Literal[
    "CHARGE_POINT_MAX_PROFILE", "TX_DEFAULT_PROFILE", "TX_PROFILE"
]

CLEAR_CHARGING_PROFILE_PARAMS_CHARGING_PROFILE_PURPOSE_VALUES: set[ClearChargingProfileParamsChargingProfilePurpose] = {
    "CHARGE_POINT_MAX_PROFILE",
    "TX_DEFAULT_PROFILE",
    "TX_PROFILE",
}


def check_clear_charging_profile_params_charging_profile_purpose(
    value: str,
) -> ClearChargingProfileParamsChargingProfilePurpose:
    if value in CLEAR_CHARGING_PROFILE_PARAMS_CHARGING_PROFILE_PURPOSE_VALUES:
        return cast(ClearChargingProfileParamsChargingProfilePurpose, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLEAR_CHARGING_PROFILE_PARAMS_CHARGING_PROFILE_PURPOSE_VALUES!r}"
    )
