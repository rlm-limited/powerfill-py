from typing import Literal, cast

ChargingProfileFormChargingProfileKind = Literal["ABSOLUTE", "RECURRING", "RELATIVE"]

CHARGING_PROFILE_FORM_CHARGING_PROFILE_KIND_VALUES: set[ChargingProfileFormChargingProfileKind] = {
    "ABSOLUTE",
    "RECURRING",
    "RELATIVE",
}


def check_charging_profile_form_charging_profile_kind(value: str) -> ChargingProfileFormChargingProfileKind:
    if value in CHARGING_PROFILE_FORM_CHARGING_PROFILE_KIND_VALUES:
        return cast(ChargingProfileFormChargingProfileKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHARGING_PROFILE_FORM_CHARGING_PROFILE_KIND_VALUES!r}"
    )
