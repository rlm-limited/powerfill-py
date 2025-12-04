from typing import Literal, cast

TriggerMessageParamsTriggerMessage = Literal[
    "BootNotification",
    "DiagnosticsStatusNotification",
    "FirmwareStatusNotification",
    "Heartbeat",
    "MeterValues",
    "StatusNotification",
]

TRIGGER_MESSAGE_PARAMS_TRIGGER_MESSAGE_VALUES: set[TriggerMessageParamsTriggerMessage] = {
    "BootNotification",
    "DiagnosticsStatusNotification",
    "FirmwareStatusNotification",
    "Heartbeat",
    "MeterValues",
    "StatusNotification",
}


def check_trigger_message_params_trigger_message(value: str) -> TriggerMessageParamsTriggerMessage:
    if value in TRIGGER_MESSAGE_PARAMS_TRIGGER_MESSAGE_VALUES:
        return cast(TriggerMessageParamsTriggerMessage, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_MESSAGE_PARAMS_TRIGGER_MESSAGE_VALUES!r}")
