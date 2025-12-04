from typing import Literal, cast

TransactionStopEventActor = Literal["manual", "station"]

TRANSACTION_STOP_EVENT_ACTOR_VALUES: set[TransactionStopEventActor] = {
    "manual",
    "station",
}


def check_transaction_stop_event_actor(value: str) -> TransactionStopEventActor:
    if value in TRANSACTION_STOP_EVENT_ACTOR_VALUES:
        return cast(TransactionStopEventActor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSACTION_STOP_EVENT_ACTOR_VALUES!r}")
