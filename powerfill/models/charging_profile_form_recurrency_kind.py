from typing import Literal, cast

ChargingProfileFormRecurrencyKind = Literal["DAILY", "WEEKLY"]

CHARGING_PROFILE_FORM_RECURRENCY_KIND_VALUES: set[ChargingProfileFormRecurrencyKind] = {
    "DAILY",
    "WEEKLY",
}


def check_charging_profile_form_recurrency_kind(value: str) -> ChargingProfileFormRecurrencyKind:
    if value in CHARGING_PROFILE_FORM_RECURRENCY_KIND_VALUES:
        return cast(ChargingProfileFormRecurrencyKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHARGING_PROFILE_FORM_RECURRENCY_KIND_VALUES!r}")
