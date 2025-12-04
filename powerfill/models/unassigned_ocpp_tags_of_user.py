from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnassignedOcppTagsOfUser")


@_attrs_define
class UnassignedOcppTagsOfUser:
    """
    Attributes:
        ocpp_tag_pks (list[int] | Unset): Ocpp Tag PKs of this user that have no permissions at all.
        user_pk (int | Unset):
    """

    ocpp_tag_pks: list[int] | Unset = UNSET
    user_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tag_pks: list[int] | Unset = UNSET
        if not isinstance(self.ocpp_tag_pks, Unset):
            ocpp_tag_pks = self.ocpp_tag_pks

        user_pk = self.user_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocpp_tag_pks is not UNSET:
            field_dict["ocppTagPks"] = ocpp_tag_pks
        if user_pk is not UNSET:
            field_dict["userPk"] = user_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ocpp_tag_pks = cast(list[int], d.pop("ocppTagPks", UNSET))

        user_pk = d.pop("userPk", UNSET)

        unassigned_ocpp_tags_of_user = cls(
            ocpp_tag_pks=ocpp_tag_pks,
            user_pk=user_pk,
        )

        unassigned_ocpp_tags_of_user.additional_properties = d
        return unassigned_ocpp_tags_of_user

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
