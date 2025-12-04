from typing import Literal, cast

ChargingProfileFormChargingProfilePurpose = Literal["CHARGE_POINT_MAX_PROFILE", "TX_DEFAULT_PROFILE", "TX_PROFILE"]

CHARGING_PROFILE_FORM_CHARGING_PROFILE_PURPOSE_VALUES: set[ChargingProfileFormChargingProfilePurpose] = {
    "CHARGE_POINT_MAX_PROFILE",
    "TX_DEFAULT_PROFILE",
    "TX_PROFILE",
}


def check_charging_profile_form_charging_profile_purpose(value: str) -> ChargingProfileFormChargingProfilePurpose:
    if value in CHARGING_PROFILE_FORM_CHARGING_PROFILE_PURPOSE_VALUES:
        return cast(ChargingProfileFormChargingProfilePurpose, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHARGING_PROFILE_FORM_CHARGING_PROFILE_PURPOSE_VALUES!r}"
    )
