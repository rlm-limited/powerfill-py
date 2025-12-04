from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargingSchedulePeriod")


@_attrs_define
class ChargingSchedulePeriod:
    """
    Attributes:
        limit (float):
        number_phases (int | Unset):
        set_limit (bool | Unset):
        set_number_phases (bool | Unset):
        set_start_period (bool | Unset):
        start_period (int | Unset):
    """

    limit: float
    number_phases: int | Unset = UNSET
    set_limit: bool | Unset = UNSET
    set_number_phases: bool | Unset = UNSET
    set_start_period: bool | Unset = UNSET
    start_period: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        number_phases = self.number_phases

        set_limit = self.set_limit

        set_number_phases = self.set_number_phases

        set_start_period = self.set_start_period

        start_period = self.start_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
            }
        )
        if number_phases is not UNSET:
            field_dict["numberPhases"] = number_phases
        if set_limit is not UNSET:
            field_dict["setLimit"] = set_limit
        if set_number_phases is not UNSET:
            field_dict["setNumberPhases"] = set_number_phases
        if set_start_period is not UNSET:
            field_dict["setStartPeriod"] = set_start_period
        if start_period is not UNSET:
            field_dict["startPeriod"] = start_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        number_phases = d.pop("numberPhases", UNSET)

        set_limit = d.pop("setLimit", UNSET)

        set_number_phases = d.pop("setNumberPhases", UNSET)

        set_start_period = d.pop("setStartPeriod", UNSET)

        start_period = d.pop("startPeriod", UNSET)

        charging_schedule_period = cls(
            limit=limit,
            number_phases=number_phases,
            set_limit=set_limit,
            set_number_phases=set_number_phases,
            set_start_period=set_start_period,
            start_period=start_period,
        )

        charging_schedule_period.additional_properties = d
        return charging_schedule_period

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
