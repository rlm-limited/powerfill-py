from typing import Literal, cast

GetOverview1OcppTagFilter = Literal["All", "OnlyUsersWithoutTags", "OnlyUsersWithTags"]

GET_OVERVIEW_1_OCPP_TAG_FILTER_VALUES: set[GetOverview1OcppTagFilter] = {
    "All",
    "OnlyUsersWithoutTags",
    "OnlyUsersWithTags",
}


def check_get_overview_1_ocpp_tag_filter(value: str) -> GetOverview1OcppTagFilter:
    if value in GET_OVERVIEW_1_OCPP_TAG_FILTER_VALUES:
        return cast(GetOverview1OcppTagFilter, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_OVERVIEW_1_OCPP_TAG_FILTER_VALUES!r}")
