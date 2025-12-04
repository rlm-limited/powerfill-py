from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unidentified_incoming_object import UnidentifiedIncomingObject


T = TypeVar("T", bound="UnknownOcppTagsDto")


@_attrs_define
class UnknownOcppTagsDto:
    """
    Attributes:
        unknown_tags (list[UnidentifiedIncomingObject] | Unset):
    """

    unknown_tags: list[UnidentifiedIncomingObject] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unknown_tags, Unset):
            unknown_tags = []
            for unknown_tags_item_data in self.unknown_tags:
                unknown_tags_item = unknown_tags_item_data.to_dict()
                unknown_tags.append(unknown_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_tags is not UNSET:
            field_dict["unknownTags"] = unknown_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unidentified_incoming_object import UnidentifiedIncomingObject

        d = dict(src_dict)
        _unknown_tags = d.pop("unknownTags", UNSET)
        unknown_tags: list[UnidentifiedIncomingObject] | Unset = UNSET
        if _unknown_tags is not UNSET:
            unknown_tags = []
            for unknown_tags_item_data in _unknown_tags:
                unknown_tags_item = UnidentifiedIncomingObject.from_dict(unknown_tags_item_data)

                unknown_tags.append(unknown_tags_item)

        unknown_ocpp_tags_dto = cls(
            unknown_tags=unknown_tags,
        )

        unknown_ocpp_tags_dto.additional_properties = d
        return unknown_ocpp_tags_dto

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
