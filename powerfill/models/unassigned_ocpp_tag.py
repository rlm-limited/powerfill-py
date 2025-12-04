from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnassignedOcppTag")


@_attrs_define
class UnassignedOcppTag:
    """
    Attributes:
        ocpp_tag_id (str | Unset):
        ocpp_tag_pk (int | Unset):
    """

    ocpp_tag_id: str | Unset = UNSET
    ocpp_tag_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tag_id = self.ocpp_tag_id

        ocpp_tag_pk = self.ocpp_tag_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocpp_tag_id is not UNSET:
            field_dict["ocppTagId"] = ocpp_tag_id
        if ocpp_tag_pk is not UNSET:
            field_dict["ocppTagPk"] = ocpp_tag_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ocpp_tag_id = d.pop("ocppTagId", UNSET)

        ocpp_tag_pk = d.pop("ocppTagPk", UNSET)

        unassigned_ocpp_tag = cls(
            ocpp_tag_id=ocpp_tag_id,
            ocpp_tag_pk=ocpp_tag_pk,
        )

        unassigned_ocpp_tag.additional_properties = d
        return unassigned_ocpp_tag

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
