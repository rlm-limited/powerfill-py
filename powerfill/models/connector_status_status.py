from typing import Literal, cast

ConnectorStatusStatus = Literal[
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

CONNECTOR_STATUS_STATUS_VALUES: set[ConnectorStatusStatus] = {
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


def check_connector_status_status(value: str) -> ConnectorStatusStatus:
    if value in CONNECTOR_STATUS_STATUS_VALUES:
        return cast(ConnectorStatusStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_STATUS_STATUS_VALUES!r}")
