from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_entry import TagEntry
    from ..models.tag_group_entry import TagGroupEntry


T = TypeVar("T", bound="PermissionDtoForNode")


@_attrs_define
class PermissionDtoForNode:
    """
    Attributes:
        node_pk (int | Unset): PK of the node with the associated permissions
        tag_group_permissions (list[TagGroupEntry] | Unset): Ocpp Tag group permissions for the node
        tag_permissions (list[TagEntry] | Unset): Ocpp Tag permissions for the node
    """

    node_pk: int | Unset = UNSET
    tag_group_permissions: list[TagGroupEntry] | Unset = UNSET
    tag_permissions: list[TagEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_pk = self.node_pk

        tag_group_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tag_group_permissions, Unset):
            tag_group_permissions = []
            for tag_group_permissions_item_data in self.tag_group_permissions:
                tag_group_permissions_item = tag_group_permissions_item_data.to_dict()
                tag_group_permissions.append(tag_group_permissions_item)

        tag_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tag_permissions, Unset):
            tag_permissions = []
            for tag_permissions_item_data in self.tag_permissions:
                tag_permissions_item = tag_permissions_item_data.to_dict()
                tag_permissions.append(tag_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_pk is not UNSET:
            field_dict["nodePk"] = node_pk
        if tag_group_permissions is not UNSET:
            field_dict["tagGroupPermissions"] = tag_group_permissions
        if tag_permissions is not UNSET:
            field_dict["tagPermissions"] = tag_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_entry import TagEntry
        from ..models.tag_group_entry import TagGroupEntry

        d = dict(src_dict)
        node_pk = d.pop("nodePk", UNSET)

        _tag_group_permissions = d.pop("tagGroupPermissions", UNSET)
        tag_group_permissions: list[TagGroupEntry] | Unset = UNSET
        if _tag_group_permissions is not UNSET:
            tag_group_permissions = []
            for tag_group_permissions_item_data in _tag_group_permissions:
                tag_group_permissions_item = TagGroupEntry.from_dict(tag_group_permissions_item_data)

                tag_group_permissions.append(tag_group_permissions_item)

        _tag_permissions = d.pop("tagPermissions", UNSET)
        tag_permissions: list[TagEntry] | Unset = UNSET
        if _tag_permissions is not UNSET:
            tag_permissions = []
            for tag_permissions_item_data in _tag_permissions:
                tag_permissions_item = TagEntry.from_dict(tag_permissions_item_data)

                tag_permissions.append(tag_permissions_item)

        permission_dto_for_node = cls(
            node_pk=node_pk,
            tag_group_permissions=tag_group_permissions,
            tag_permissions=tag_permissions,
        )

        permission_dto_for_node.additional_properties = d
        return permission_dto_for_node

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
