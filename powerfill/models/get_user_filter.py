from typing import Literal, cast

GetUserFilter = Literal["All", "OnlyTagsWithoutUser", "OnlyTagsWithUser"]

GET_USER_FILTER_VALUES: set[GetUserFilter] = {
    "All",
    "OnlyTagsWithoutUser",
    "OnlyTagsWithUser",
}


def check_get_user_filter(value: str) -> GetUserFilter:
    if value in GET_USER_FILTER_VALUES:
        return cast(GetUserFilter, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_USER_FILTER_VALUES!r}")
