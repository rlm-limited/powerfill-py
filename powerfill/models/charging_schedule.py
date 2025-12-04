from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.charging_schedule_charging_rate_unit import (
    ChargingScheduleChargingRateUnit,
    check_charging_schedule_charging_rate_unit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charging_schedule_period import ChargingSchedulePeriod


T = TypeVar("T", bound="ChargingSchedule")


@_attrs_define
class ChargingSchedule:
    """
    Attributes:
        charging_rate_unit (ChargingScheduleChargingRateUnit):
        charging_schedule_period (list[ChargingSchedulePeriod]):
        duration (int | Unset):
        min_charging_rate (float | Unset):
        set_charging_rate_unit (bool | Unset):
        set_charging_schedule_period (bool | Unset):
        set_duration (bool | Unset):
        set_min_charging_rate (bool | Unset):
        set_start_schedule (bool | Unset):
        start_schedule (datetime.datetime | Unset):
    """

    charging_rate_unit: ChargingScheduleChargingRateUnit
    charging_schedule_period: list[ChargingSchedulePeriod]
    duration: int | Unset = UNSET
    min_charging_rate: float | Unset = UNSET
    set_charging_rate_unit: bool | Unset = UNSET
    set_charging_schedule_period: bool | Unset = UNSET
    set_duration: bool | Unset = UNSET
    set_min_charging_rate: bool | Unset = UNSET
    set_start_schedule: bool | Unset = UNSET
    start_schedule: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charging_rate_unit: str = self.charging_rate_unit

        charging_schedule_period = []
        for charging_schedule_period_item_data in self.charging_schedule_period:
            charging_schedule_period_item = charging_schedule_period_item_data.to_dict()
            charging_schedule_period.append(charging_schedule_period_item)

        duration = self.duration

        min_charging_rate = self.min_charging_rate

        set_charging_rate_unit = self.set_charging_rate_unit

        set_charging_schedule_period = self.set_charging_schedule_period

        set_duration = self.set_duration

        set_min_charging_rate = self.set_min_charging_rate

        set_start_schedule = self.set_start_schedule

        start_schedule: str | Unset = UNSET
        if not isinstance(self.start_schedule, Unset):
            start_schedule = self.start_schedule.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargingRateUnit": charging_rate_unit,
                "chargingSchedulePeriod": charging_schedule_period,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if min_charging_rate is not UNSET:
            field_dict["minChargingRate"] = min_charging_rate
        if set_charging_rate_unit is not UNSET:
            field_dict["setChargingRateUnit"] = set_charging_rate_unit
        if set_charging_schedule_period is not UNSET:
            field_dict["setChargingSchedulePeriod"] = set_charging_schedule_period
        if set_duration is not UNSET:
            field_dict["setDuration"] = set_duration
        if set_min_charging_rate is not UNSET:
            field_dict["setMinChargingRate"] = set_min_charging_rate
        if set_start_schedule is not UNSET:
            field_dict["setStartSchedule"] = set_start_schedule
        if start_schedule is not UNSET:
            field_dict["startSchedule"] = start_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.charging_schedule_period import ChargingSchedulePeriod

        d = dict(src_dict)
        charging_rate_unit = check_charging_schedule_charging_rate_unit(d.pop("chargingRateUnit"))

        charging_schedule_period = []
        _charging_schedule_period = d.pop("chargingSchedulePeriod")
        for charging_schedule_period_item_data in _charging_schedule_period:
            charging_schedule_period_item = ChargingSchedulePeriod.from_dict(charging_schedule_period_item_data)

            charging_schedule_period.append(charging_schedule_period_item)

        duration = d.pop("duration", UNSET)

        min_charging_rate = d.pop("minChargingRate", UNSET)

        set_charging_rate_unit = d.pop("setChargingRateUnit", UNSET)

        set_charging_schedule_period = d.pop("setChargingSchedulePeriod", UNSET)

        set_duration = d.pop("setDuration", UNSET)

        set_min_charging_rate = d.pop("setMinChargingRate", UNSET)

        set_start_schedule = d.pop("setStartSchedule", UNSET)

        _start_schedule = d.pop("startSchedule", UNSET)
        start_schedule: datetime.datetime | Unset
        if isinstance(_start_schedule, Unset):
            start_schedule = UNSET
        else:
            start_schedule = isoparse(_start_schedule)

        charging_schedule = cls(
            charging_rate_unit=charging_rate_unit,
            charging_schedule_period=charging_schedule_period,
            duration=duration,
            min_charging_rate=min_charging_rate,
            set_charging_rate_unit=set_charging_rate_unit,
            set_charging_schedule_period=set_charging_schedule_period,
            set_duration=set_duration,
            set_min_charging_rate=set_min_charging_rate,
            set_start_schedule=set_start_schedule,
            start_schedule=start_schedule,
        )

        charging_schedule.additional_properties = d
        return charging_schedule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
