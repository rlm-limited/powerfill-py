from typing import Literal, cast

GetOverview2ProfilePurpose = Literal["CHARGE_POINT_MAX_PROFILE", "TX_DEFAULT_PROFILE", "TX_PROFILE"]

GET_OVERVIEW_2_PROFILE_PURPOSE_VALUES: set[GetOverview2ProfilePurpose] = {
    "CHARGE_POINT_MAX_PROFILE",
    "TX_DEFAULT_PROFILE",
    "TX_PROFILE",
}


def check_get_overview_2_profile_purpose(value: str) -> GetOverview2ProfilePurpose:
    if value in GET_OVERVIEW_2_PROFILE_PURPOSE_VALUES:
        return cast(GetOverview2ProfilePurpose, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_OVERVIEW_2_PROFILE_PURPOSE_VALUES!r}")
