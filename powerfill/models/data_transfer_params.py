from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataTransferParams")


@_attrs_define
class DataTransferParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain at least 1 element
        vendor_id (str):
        data (str | Unset):
        message_id (str | Unset):
    """

    charge_box_id_list: list[str]
    vendor_id: str
    data: str | Unset = UNSET
    message_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        vendor_id = self.vendor_id

        data = self.data

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "vendorId": vendor_id,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if message_id is not UNSET:
            field_dict["messageId"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        vendor_id = d.pop("vendorId")

        data = d.pop("data", UNSET)

        message_id = d.pop("messageId", UNSET)

        data_transfer_params = cls(
            charge_box_id_list=charge_box_id_list,
            vendor_id=vendor_id,
            data=data,
            message_id=message_id,
        )

        data_transfer_params.additional_properties = d
        return data_transfer_params

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
