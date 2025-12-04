from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ReserveNowParams")


@_attrs_define
class ReserveNowParams:
    """
    Attributes:
        charge_box_id_list (list[str]): Should contain exactly 1 element
        connector_id (int):
        expiry (datetime.datetime):
        id_tag (str):
    """

    charge_box_id_list: list[str]
    connector_id: int
    expiry: datetime.datetime
    id_tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_id_list = self.charge_box_id_list

        connector_id = self.connector_id

        expiry = self.expiry.isoformat()

        id_tag = self.id_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxIdList": charge_box_id_list,
                "connectorId": connector_id,
                "expiry": expiry,
                "idTag": id_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_id_list = cast(list[str], d.pop("chargeBoxIdList"))

        connector_id = d.pop("connectorId")

        expiry = isoparse(d.pop("expiry"))

        id_tag = d.pop("idTag")

        reserve_now_params = cls(
            charge_box_id_list=charge_box_id_list,
            connector_id=connector_id,
            expiry=expiry,
            id_tag=id_tag,
        )

        reserve_now_params.additional_properties = d
        return reserve_now_params

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
