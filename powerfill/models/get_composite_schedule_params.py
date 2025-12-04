from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_composite_schedule_params_charging_rate_unit import (
    GetCompositeScheduleParamsChargingRateUnit,
    check_get_composite_schedule_params_charging_rate_unit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompositeScheduleParams")


@_attrs_define
class GetCompositeScheduleParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        connector_id (int):
        duration_in_seconds (int):
        charging_rate_unit (GetCompositeScheduleParamsChargingRateUnit | Unset):
    """

    charge_box_id_list: list[str]
    connector_id: int
    duration_in_seconds: int
    charging_rate_unit: GetCompositeScheduleParamsChargingRateUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        connector_id = self.connector_id

        duration_in_seconds = self.duration_in_seconds

        charging_rate_unit: str | Unset = UNSET
        if not isinstance(self.charging_rate_unit, Unset):
            charging_rate_unit = self.charging_rate_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "connectorId": connector_id,
                "durationInSeconds": duration_in_seconds,
            }
        )
        if charging_rate_unit is not UNSET:
            field_dict["chargingRateUnit"] = charging_rate_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        connector_id = d.pop("connectorId")

        duration_in_seconds = d.pop("durationInSeconds")

        _charging_rate_unit = d.pop("chargingRateUnit", UNSET)
        charging_rate_unit: GetCompositeScheduleParamsChargingRateUnit | Unset
        if isinstance(_charging_rate_unit, Unset):
            charging_rate_unit = UNSET
        else:
            charging_rate_unit = check_get_composite_schedule_params_charging_rate_unit(_charging_rate_unit)

        get_composite_schedule_params = cls(
            charge_box_id_list=charge_box_id_list,
            connector_id=connector_id,
            duration_in_seconds=duration_in_seconds,
            charging_rate_unit=charging_rate_unit,
        )

        get_composite_schedule_params.additional_properties = d
        return get_composite_schedule_params

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
