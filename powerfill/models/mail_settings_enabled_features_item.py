from typing import Literal, cast

MailSettingsEnabledFeaturesItem = Literal[
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
]

MAIL_SETTINGS_ENABLED_FEATURES_ITEM_VALUES: set[MailSettingsEnabledFeaturesItem] = {
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
}


def check_mail_settings_enabled_features_item(value: str) -> MailSettingsEnabledFeaturesItem:
    if value in MAIL_SETTINGS_ENABLED_FEATURES_ITEM_VALUES:
        return cast(MailSettingsEnabledFeaturesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAIL_SETTINGS_ENABLED_FEATURES_ITEM_VALUES!r}")
