from typing import Literal, cast

Get1HeartbeatPeriod = Literal["ALL", "EARLIER", "TODAY", "YESTERDAY"]

GET_1_HEARTBEAT_PERIOD_VALUES: set[Get1HeartbeatPeriod] = {
    "ALL",
    "EARLIER",
    "TODAY",
    "YESTERDAY",
}


def check_get_1_heartbeat_period(value: str) -> Get1HeartbeatPeriod:
    if value in GET_1_HEARTBEAT_PERIOD_VALUES:
        return cast(Get1HeartbeatPeriod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_1_HEARTBEAT_PERIOD_VALUES!r}")
