from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OcppTagIdListDto")


@_attrs_define
class OcppTagIdListDto:
    """
    Attributes:
        ocpp_tag_ids (list[str]): List of Ocpp Tag IDs
    """

    ocpp_tag_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tag_ids = self.ocpp_tag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ocppTagIds": ocpp_tag_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ocpp_tag_ids = cast(list[str], d.pop("ocppTagIds"))

        ocpp_tag_id_list_dto = cls(
            ocpp_tag_ids=ocpp_tag_ids,
        )

        ocpp_tag_id_list_dto.additional_properties = d
        return ocpp_tag_id_list_dto

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
