from typing import Literal, cast

GetCompositeScheduleParamsChargingRateUnit = Literal["A", "W"]

GET_COMPOSITE_SCHEDULE_PARAMS_CHARGING_RATE_UNIT_VALUES: set[GetCompositeScheduleParamsChargingRateUnit] = {
    "A",
    "W",
}


def check_get_composite_schedule_params_charging_rate_unit(value: str) -> GetCompositeScheduleParamsChargingRateUnit:
    if value in GET_COMPOSITE_SCHEDULE_PARAMS_CHARGING_RATE_UNIT_VALUES:
        return cast(GetCompositeScheduleParamsChargingRateUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_COMPOSITE_SCHEDULE_PARAMS_CHARGING_RATE_UNIT_VALUES!r}"
    )
