from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_dto_for_tag import PermissionDtoForTag


T = TypeVar("T", bound="PermissionDtoForTagList")


@_attrs_define
class PermissionDtoForTagList:
    """
    Attributes:
        ocpp_tags (list[PermissionDtoForTag] | Unset):
    """

    ocpp_tags: list[PermissionDtoForTag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ocpp_tags, Unset):
            ocpp_tags = []
            for ocpp_tags_item_data in self.ocpp_tags:
                ocpp_tags_item = ocpp_tags_item_data.to_dict()
                ocpp_tags.append(ocpp_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocpp_tags is not UNSET:
            field_dict["ocppTags"] = ocpp_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_dto_for_tag import PermissionDtoForTag

        d = dict(src_dict)
        _ocpp_tags = d.pop("ocppTags", UNSET)
        ocpp_tags: list[PermissionDtoForTag] | Unset = UNSET
        if _ocpp_tags is not UNSET:
            ocpp_tags = []
            for ocpp_tags_item_data in _ocpp_tags:
                ocpp_tags_item = PermissionDtoForTag.from_dict(ocpp_tags_item_data)

                ocpp_tags.append(ocpp_tags_item)

        permission_dto_for_tag_list = cls(
            ocpp_tags=ocpp_tags,
        )

        permission_dto_for_tag_list.additional_properties = d
        return permission_dto_for_tag_list

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
