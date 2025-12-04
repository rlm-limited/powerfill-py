from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clear_charging_profile_params_charging_profile_purpose import (
    ClearChargingProfileParamsChargingProfilePurpose,
    check_clear_charging_profile_params_charging_profile_purpose,
)
from ..models.clear_charging_profile_params_filter_type import (
    ClearChargingProfileParamsFilterType,
    check_clear_charging_profile_params_filter_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClearChargingProfileParams")


@_attrs_define
class ClearChargingProfileParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        filter_type (ClearChargingProfileParamsFilterType):
        charging_profile_pk (int | Unset):
        charging_profile_purpose (ClearChargingProfileParamsChargingProfilePurpose | Unset):
        connector_id (int | Unset):
        stack_level (int | Unset):
    """

    charge_box_id_list: list[str]
    filter_type: ClearChargingProfileParamsFilterType
    charging_profile_pk: int | Unset = UNSET
    charging_profile_purpose: ClearChargingProfileParamsChargingProfilePurpose | Unset = UNSET
    connector_id: int | Unset = UNSET
    stack_level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        filter_type: str = self.filter_type

        charging_profile_pk = self.charging_profile_pk

        charging_profile_purpose: str | Unset = UNSET
        if not isinstance(self.charging_profile_purpose, Unset):
            charging_profile_purpose = self.charging_profile_purpose

        connector_id = self.connector_id

        stack_level = self.stack_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "filterType": filter_type,
            }
        )
        if charging_profile_pk is not UNSET:
            field_dict["chargingProfilePk"] = charging_profile_pk
        if charging_profile_purpose is not UNSET:
            field_dict["chargingProfilePurpose"] = charging_profile_purpose
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if stack_level is not UNSET:
            field_dict["stackLevel"] = stack_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        filter_type = check_clear_charging_profile_params_filter_type(d.pop("filterType"))

        charging_profile_pk = d.pop("chargingProfilePk", UNSET)

        _charging_profile_purpose = d.pop("chargingProfilePurpose", UNSET)
        charging_profile_purpose: ClearChargingProfileParamsChargingProfilePurpose | Unset
        if isinstance(_charging_profile_purpose, Unset):
            charging_profile_purpose = UNSET
        else:
            charging_profile_purpose = check_clear_charging_profile_params_charging_profile_purpose(
                _charging_profile_purpose
            )

        connector_id = d.pop("connectorId", UNSET)

        stack_level = d.pop("stackLevel", UNSET)

        clear_charging_profile_params = cls(
            charge_box_id_list=charge_box_id_list,
            filter_type=filter_type,
            charging_profile_pk=charging_profile_pk,
            charging_profile_purpose=charging_profile_purpose,
            connector_id=connector_id,
            stack_level=stack_level,
        )

        clear_charging_profile_params.additional_properties = d
        return clear_charging_profile_params

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
