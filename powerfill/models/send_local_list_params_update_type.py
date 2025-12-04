from typing import Literal, cast

SendLocalListParamsUpdateType = Literal["DIFFERENTIAL", "FULL"]

SEND_LOCAL_LIST_PARAMS_UPDATE_TYPE_VALUES: set[SendLocalListParamsUpdateType] = {
    "DIFFERENTIAL",
    "FULL",
}


def check_send_local_list_params_update_type(value: str) -> SendLocalListParamsUpdateType:
    if value in SEND_LOCAL_LIST_PARAMS_UPDATE_TYPE_VALUES:
        return cast(SendLocalListParamsUpdateType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEND_LOCAL_LIST_PARAMS_UPDATE_TYPE_VALUES!r}")
