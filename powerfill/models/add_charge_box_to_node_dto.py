from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddChargeBoxToNodeDto")


@_attrs_define
class AddChargeBoxToNodeDto:
    """
    Attributes:
        charge_box_pks (list[int]): Charge box PKs to be added to site at node with id 'nodePk'
        node_pk (int): Identifies the node of the site at which to add charge boxes
    """

    charge_box_pks: list[int]
    node_pk: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charge_box_pks = self.charge_box_pks

        node_pk = self.node_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargeBoxPks": charge_box_pks,
                "nodePk": node_pk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        charge_box_pks = cast(list[int], d.pop("chargeBoxPks"))

        node_pk = d.pop("nodePk")

        add_charge_box_to_node_dto = cls(
            charge_box_pks=charge_box_pks,
            node_pk=node_pk,
        )

        add_charge_box_to_node_dto.additional_properties = d
        return add_charge_box_to_node_dto

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
