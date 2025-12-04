from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnassignedOcppTagGroup")


@_attrs_define
class UnassignedOcppTagGroup:
    """
    Attributes:
        name (str | Unset):
        ocpp_tag_group_pk (int | Unset):
    """

    name: str | Unset = UNSET
    ocpp_tag_group_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ocpp_tag_group_pk = self.ocpp_tag_group_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ocpp_tag_group_pk is not UNSET:
            field_dict["ocppTagGroupPk"] = ocpp_tag_group_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        ocpp_tag_group_pk = d.pop("ocppTagGroupPk", UNSET)

        unassigned_ocpp_tag_group = cls(
            name=name,
            ocpp_tag_group_pk=ocpp_tag_group_pk,
        )

        unassigned_ocpp_tag_group.additional_properties = d
        return unassigned_ocpp_tag_group

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
