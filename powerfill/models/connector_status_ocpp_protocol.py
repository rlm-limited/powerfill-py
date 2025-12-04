from typing import Literal, cast

ConnectorStatusOcppProtocol = Literal["V_12_JSON", "V_12_SOAP", "V_15_JSON", "V_15_SOAP", "V_16_JSON", "V_16_SOAP"]

CONNECTOR_STATUS_OCPP_PROTOCOL_VALUES: set[ConnectorStatusOcppProtocol] = {
    "V_12_JSON",
    "V_12_SOAP",
    "V_15_JSON",
    "V_15_SOAP",
    "V_16_JSON",
    "V_16_SOAP",
}


def check_connector_status_ocpp_protocol(value: str) -> ConnectorStatusOcppProtocol:
    if value in CONNECTOR_STATUS_OCPP_PROTOCOL_VALUES:
        return cast(ConnectorStatusOcppProtocol, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONNECTOR_STATUS_OCPP_PROTOCOL_VALUES!r}")
