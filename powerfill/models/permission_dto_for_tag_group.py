from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_entry import NodeEntry


T = TypeVar("T", bound="PermissionDtoForTagGroup")


@_attrs_define
class PermissionDtoForTagGroup:
    """
    Attributes:
        ocpp_tag_group_pk (int | Unset): PK of Ocpp Tag group with the associated permissions
        permissions (list[NodeEntry] | Unset): List of permissions for the Ocpp Tag group
    """

    ocpp_tag_group_pk: int | Unset = UNSET
    permissions: list[NodeEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ocpp_tag_group_pk = self.ocpp_tag_group_pk

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ocpp_tag_group_pk is not UNSET:
            field_dict["ocppTagGroupPk"] = ocpp_tag_group_pk
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_entry import NodeEntry

        d = dict(src_dict)
        ocpp_tag_group_pk = d.pop("ocppTagGroupPk", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[NodeEntry] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = NodeEntry.from_dict(permissions_item_data)

                permissions.append(permissions_item)

        permission_dto_for_tag_group = cls(
            ocpp_tag_group_pk=ocpp_tag_group_pk,
            permissions=permissions,
        )

        permission_dto_for_tag_group.additional_properties = d
        return permission_dto_for_tag_group

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
