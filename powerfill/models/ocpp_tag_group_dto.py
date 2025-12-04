from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcppTagGroupDto")


@_attrs_define
class OcppTagGroupDto:
    """
    Attributes:
        internal_name (str): Internal name of Ocpp Tag group
        name (str): Name of Ocpp Tag group
        id (int | Unset): PK of Ocpp Tag group
        ocpp_tag_ids (list[str] | Unset): Ocpp Tags associated with this group
    """

    internal_name: str
    name: str
    id: int | Unset = UNSET
    ocpp_tag_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_name = self.internal_name

        name = self.name

        id = self.id

        ocpp_tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.ocpp_tag_ids, Unset):
            ocpp_tag_ids = self.ocpp_tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalName": internal_name,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if ocpp_tag_ids is not UNSET:
            field_dict["ocppTagIds"] = ocpp_tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        internal_name = d.pop("internalName")

        name = d.pop("name")

        id = d.pop("id", UNSET)

        ocpp_tag_ids = cast(list[str], d.pop("ocppTagIds", UNSET))

        ocpp_tag_group_dto = cls(
            internal_name=internal_name,
            name=name,
            id=id,
            ocpp_tag_ids=ocpp_tag_ids,
        )

        ocpp_tag_group_dto.additional_properties = d
        return ocpp_tag_group_dto

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
