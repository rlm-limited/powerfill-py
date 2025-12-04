from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_availability_params_avail_type import (
    ChangeAvailabilityParamsAvailType,
    check_change_availability_params_avail_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeAvailabilityParams")


@_attrs_define
class ChangeAvailabilityParams:
    """
    Attributes:
        avail_type (ChangeAvailabilityParamsAvailType):
        charge_box_id_list (list[str]): Should contain at least 1 element
        connector_id (int | Unset):
    """

    avail_type: ChangeAvailabilityParamsAvailType
    charge_box_id_list: list[str]
    connector_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avail_type: str = self.avail_type

        charge_box_id_list = self.charge_box_id_list

        connector_id = self.connector_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availType": avail_type,
                "chargeBoxIdList": charge_box_id_list,
            }
        )
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avail_type = check_change_availability_params_avail_type(d.pop("availType"))

        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        connector_id = d.pop("connectorId", UNSET)

        change_availability_params = cls(
            avail_type=avail_type,
            charge_box_id_list=charge_box_id_list,
            connector_id=connector_id,
        )

        change_availability_params.additional_properties = d
        return change_availability_params

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
