from typing import Literal, cast

UserFormNotificationFeaturesItem = Literal[
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
]

USER_FORM_NOTIFICATION_FEATURES_ITEM_VALUES: set[UserFormNotificationFeaturesItem] = {
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
}


def check_user_form_notification_features_item(value: str) -> UserFormNotificationFeaturesItem:
    if value in USER_FORM_NOTIFICATION_FEATURES_ITEM_VALUES:
        return cast(UserFormNotificationFeaturesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_FORM_NOTIFICATION_FEATURES_ITEM_VALUES!r}")
