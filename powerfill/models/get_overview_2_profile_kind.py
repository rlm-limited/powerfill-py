from typing import Literal, cast

GetOverview2ProfileKind = Literal["ABSOLUTE", "RECURRING", "RELATIVE"]

GET_OVERVIEW_2_PROFILE_KIND_VALUES: set[GetOverview2ProfileKind] = {
    "ABSOLUTE",
    "RECURRING",
    "RELATIVE",
}


def check_get_overview_2_profile_kind(value: str) -> GetOverview2ProfileKind:
    if value in GET_OVERVIEW_2_PROFILE_KIND_VALUES:
        return cast(GetOverview2ProfileKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_OVERVIEW_2_PROFILE_KIND_VALUES!r}")
