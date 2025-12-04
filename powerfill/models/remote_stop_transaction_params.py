from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoteStopTransactionParams")


@_attrs_define
class RemoteStopTransactionParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain exactly 1 element
        transaction_id (int):
    """

    charge_box_id_list: list[str]
    transaction_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "transactionId": transaction_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        transaction_id = d.pop("transactionId")

        remote_stop_transaction_params = cls(
            charge_box_id_list=charge_box_id_list,
            transaction_id=transaction_id,
        )

        remote_stop_transaction_params.additional_properties = d
        return remote_stop_transaction_params

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
