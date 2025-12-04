from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteStartTransactionParams")


@_attrs_define
class RemoteStartTransactionParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain exactly 1 element
        id_tag (str):
        charging_profile_pk (int | Unset): PK of the charging profile to be used for the transaction.
            <code>ChargingProfilePurposeType</code> of the profile must be <code>TX_PROFILE</code>.
        connector_id (int | Unset):
    """

    charge_box_id_list: list[str]
    id_tag: str
    charging_profile_pk: int | Unset = UNSET
    connector_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        id_tag = self.id_tag

        charging_profile_pk = self.charging_profile_pk

        connector_id = self.connector_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "idTag": id_tag,
            }
        )
        if charging_profile_pk is not UNSET:
            field_dict["chargingProfilePk"] = charging_profile_pk
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        id_tag = d.pop("idTag")

        charging_profile_pk = d.pop("chargingProfilePk", UNSET)

        connector_id = d.pop("connectorId", UNSET)

        remote_start_transaction_params = cls(
            charge_box_id_list=charge_box_id_list,
            id_tag=id_tag,
            charging_profile_pk=charging_profile_pk,
            connector_id=connector_id,
        )

        remote_start_transaction_params.additional_properties = d
        return remote_start_transaction_params

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
