from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocpp_tag_group_dto import OcppTagGroupDto


T = TypeVar("T", bound="OcppTagGroupDtoList")


@_attrs_define
class OcppTagGroupDtoList:
    """
    Attributes:
        ocpp_tag_groups (list[OcppTagGroupDto] | Unset):
    """

    ocpp_tag_groups: list[OcppTagGroupDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tag_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ocpp_tag_groups, Unset):
            ocpp_tag_groups = []
            for ocpp_tag_groups_item_data in self.ocpp_tag_groups:
                ocpp_tag_groups_item = ocpp_tag_groups_item_data.to_dict()
                ocpp_tag_groups.append(ocpp_tag_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocpp_tag_groups is not UNSET:
            field_dict["ocppTagGroups"] = ocpp_tag_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ocpp_tag_group_dto import OcppTagGroupDto

        d = dict(src_dict)
        _ocpp_tag_groups = d.pop("ocppTagGroups", UNSET)
        ocpp_tag_groups: list[OcppTagGroupDto] | Unset = UNSET
        if _ocpp_tag_groups is not UNSET:
            ocpp_tag_groups = []
            for ocpp_tag_groups_item_data in _ocpp_tag_groups:
                ocpp_tag_groups_item = OcppTagGroupDto.from_dict(ocpp_tag_groups_item_data)

                ocpp_tag_groups.append(ocpp_tag_groups_item)

        ocpp_tag_group_dto_list = cls(
            ocpp_tag_groups=ocpp_tag_groups,
        )

        ocpp_tag_group_dto_list.additional_properties = d
        return ocpp_tag_group_dto_list

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
