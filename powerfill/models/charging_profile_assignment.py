from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargingProfileAssignment")


@_attrs_define
class ChargingProfileAssignment:
    """
    Attributes:
        charge_box_id (str | Unset):
        charge_box_pk (int | Unset):
        charging_profile_description (str | Unset):
        charging_profile_pk (int | Unset):
        connector_id (int | Unset):
    """

    charge_box_id: str | Unset = UNSET
    charge_box_pk: int | Unset = UNSET
    charging_profile_description: str | Unset = UNSET
    charging_profile_pk: int | Unset = UNSET
    connector_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id = self.charge_box_id

        charge_box_pk = self.charge_box_pk

        charging_profile_description = self.charging_profile_description

        charging_profile_pk = self.charging_profile_pk

        connector_id = self.connector_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charge_box_id is not UNSET:
            field_dict["chargeBoxId"] = charge_box_id
        if charge_box_pk is not UNSET:
            field_dict["chargeBoxPk"] = charge_box_pk
        if charging_profile_description is not UNSET:
            field_dict["chargingProfileDescription"] = charging_profile_description
        if charging_profile_pk is not UNSET:
            field_dict["chargingProfilePk"] = charging_profile_pk
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id = d.pop("chargeBoxId", UNSET)

        charge_box_pk = d.pop("chargeBoxPk", UNSET)

        charging_profile_description = d.pop("chargingProfileDescription", UNSET)

        charging_profile_pk = d.pop("chargingProfilePk", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        charging_profile_assignment = cls(
            charge_box_id=charge_box_id,
            charge_box_pk=charge_box_pk,
            charging_profile_description=charging_profile_description,
            charging_profile_pk=charging_profile_pk,
            connector_id=connector_id,
        )

        charging_profile_assignment.additional_properties = d
        return charging_profile_assignment

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
