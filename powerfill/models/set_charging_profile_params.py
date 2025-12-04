from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetChargingProfileParams")


@_attrs_define
class SetChargingProfileParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        charging_profile_pk (int):
        connector_id (int):
        transaction_id (int | Unset): Apply the profile to the transaction with this ID.
            <code>ChargingProfilePurposeType</code> of the profile must be <code>TX_PROFILE</code>.
    """

    charge_box_id_list: list[str]
    charging_profile_pk: int
    connector_id: int
    transaction_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        charging_profile_pk = self.charging_profile_pk

        connector_id = self.connector_id

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "chargingProfilePk": charging_profile_pk,
                "connectorId": connector_id,
            }
        )
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        charging_profile_pk = d.pop("chargingProfilePk")

        connector_id = d.pop("connectorId")

        transaction_id = d.pop("transactionId", UNSET)

        set_charging_profile_params = cls(
            charge_box_id_list=charge_box_id_list,
            charging_profile_pk=charging_profile_pk,
            connector_id=connector_id,
            transaction_id=transaction_id,
        )

        set_charging_profile_params.additional_properties = d
        return set_charging_profile_params

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
