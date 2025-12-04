from typing import Literal, cast

ChargingProfileFormChargingRateUnit = Literal["A", "W"]

CHARGING_PROFILE_FORM_CHARGING_RATE_UNIT_VALUES: set[ChargingProfileFormChargingRateUnit] = {
    "A",
    "W",
}


def check_charging_profile_form_charging_rate_unit(value: str) -> ChargingProfileFormChargingRateUnit:
    if value in CHARGING_PROFILE_FORM_CHARGING_RATE_UNIT_VALUES:
        return cast(ChargingProfileFormChargingRateUnit, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHARGING_PROFILE_FORM_CHARGING_RATE_UNIT_VALUES!r}")
