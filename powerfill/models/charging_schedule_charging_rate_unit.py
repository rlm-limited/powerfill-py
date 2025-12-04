from typing import Literal, cast

ChargingScheduleChargingRateUnit = Literal["A", "W"]

CHARGING_SCHEDULE_CHARGING_RATE_UNIT_VALUES: set[ChargingScheduleChargingRateUnit] = {
    "A",
    "W",
}


def check_charging_schedule_charging_rate_unit(value: str) -> ChargingScheduleChargingRateUnit:
    if value in CHARGING_SCHEDULE_CHARGING_RATE_UNIT_VALUES:
        return cast(ChargingScheduleChargingRateUnit, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHARGING_SCHEDULE_CHARGING_RATE_UNIT_VALUES!r}")
