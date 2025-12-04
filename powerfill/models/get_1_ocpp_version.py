from typing import Literal, cast

Get1OcppVersion = Literal["V_12", "V_15", "V_16"]

GET_1_OCPP_VERSION_VALUES: set[Get1OcppVersion] = {
    "V_12",
    "V_15",
    "V_16",
}


def check_get_1_ocpp_version(value: str) -> Get1OcppVersion:
    if value in GET_1_OCPP_VERSION_VALUES:
        return cast(Get1OcppVersion, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_1_OCPP_VERSION_VALUES!r}")
