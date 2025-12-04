from typing import Literal, cast

GetConnectorStatusStatus = Literal[
    "Available",
    "Charging",
    "Faulted",
    "Finishing",
    "Occupied",
    "Preparing",
    "Reserved",
    "SuspendedEV",
    "SuspendedEVSE",
    "Unavailable",
]

GET_CONNECTOR_STATUS_STATUS_VALUES: set[GetConnectorStatusStatus] = {
    "Available",
    "Charging",
    "Faulted",
    "Finishing",
    "Occupied",
    "Preparing",
    "Reserved",
    "SuspendedEV",
    "SuspendedEVSE",
    "Unavailable",
}


def check_get_connector_status_status(value: str) -> GetConnectorStatusStatus:
    if value in GET_CONNECTOR_STATUS_STATUS_VALUES:
        return cast(GetConnectorStatusStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONNECTOR_STATUS_STATUS_VALUES!r}")
