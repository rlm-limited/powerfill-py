from typing import Literal, cast

UserOverviewNotificationFeaturesItem = Literal[
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
]

USER_OVERVIEW_NOTIFICATION_FEATURES_ITEM_VALUES: set[UserOverviewNotificationFeaturesItem] = {
    "OcppStationBooted",
    "OcppStationStatusFailure",
    "OcppStationStatusSuspendedEV",
    "OcppStationWebSocketConnected",
    "OcppStationWebSocketDisconnected",
    "OcppTransactionEnded",
    "OcppTransactionStarted",
}


def check_user_overview_notification_features_item(value: str) -> UserOverviewNotificationFeaturesItem:
    if value in USER_OVERVIEW_NOTIFICATION_FEATURES_ITEM_VALUES:
        return cast(UserOverviewNotificationFeaturesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_OVERVIEW_NOTIFICATION_FEATURES_ITEM_VALUES!r}")
