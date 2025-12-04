from typing import Literal, cast

OcppJsonStatusVersion = Literal["V_12", "V_15", "V_16"]

OCPP_JSON_STATUS_VERSION_VALUES: set[OcppJsonStatusVersion] = {
    "V_12",
    "V_15",
    "V_16",
}


def check_ocpp_json_status_version(value: str) -> OcppJsonStatusVersion:
    if value in OCPP_JSON_STATUS_VERSION_VALUES:
        return cast(OcppJsonStatusVersion, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OCPP_JSON_STATUS_VERSION_VALUES!r}")
