from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    """
    Attributes:
        name (str): The name of the node
        charge_box_pks (list[int] | Unset): The charge box PKs associated with the node
        children (list[Node] | Unset): The direct children of the node (if any) represented as a list of nodes
        node_id (int | Unset): The unique identifier of the node
    """

    name: str
    charge_box_pks: list[int] | Unset = UNSET
    children: list[Node] | Unset = UNSET
    node_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        charge_box_pks: list[int] | Unset = UNSET
        if not isinstance(self.charge_box_pks, Unset):
            charge_box_pks = self.charge_box_pks

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if charge_box_pks is not UNSET:
            field_dict["chargeBoxPks"] = charge_box_pks
        if children is not UNSET:
            field_dict["children"] = children
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        charge_box_pks = cast(list[int], d.pop("chargeBoxPks", UNSET))

        _children = d.pop("children", UNSET)
        children: list[Node] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = Node.from_dict(children_item_data)

                children.append(children_item)

        node_id = d.pop("nodeId", UNSET)

        node = cls(
            name=name,
            charge_box_pks=charge_box_pks,
            children=children,
            node_id=node_id,
        )

        node.additional_properties = d
        return node

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
