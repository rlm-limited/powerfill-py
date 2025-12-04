from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagGroupEntry")


@_attrs_define
class TagGroupEntry:
    """
    Attributes:
        applies_to_all_children (bool | Unset): Does this permission apply only to this particular node (then set to
            false), or to all its children as well (then set to true)
        ocpp_tag_group_pk (int | Unset): PK of Ocpp Tag group
    """

    applies_to_all_children: bool | Unset = UNSET
    ocpp_tag_group_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applies_to_all_children = self.applies_to_all_children

        ocpp_tag_group_pk = self.ocpp_tag_group_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applies_to_all_children is not UNSET:
            field_dict["appliesToAllChildren"] = applies_to_all_children
        if ocpp_tag_group_pk is not UNSET:
            field_dict["ocppTagGroupPk"] = ocpp_tag_group_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applies_to_all_children = d.pop("appliesToAllChildren", UNSET)

        ocpp_tag_group_pk = d.pop("ocppTagGroupPk", UNSET)

        tag_group_entry = cls(
            applies_to_all_children=applies_to_all_children,
            ocpp_tag_group_pk=ocpp_tag_group_pk,
        )

        tag_group_entry.additional_properties = d
        return tag_group_entry

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
