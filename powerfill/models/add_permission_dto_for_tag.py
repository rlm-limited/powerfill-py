from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddPermissionDtoForTag")


@_attrs_define
class AddPermissionDtoForTag:
    """
    Attributes:
        applies_to_all_children (bool): Should this permission apply only to this particular node (then set to false),
            or to all its children in site tree as well (then set to true)
        node_pk (int): Identifies the node of the site at which to add permission for the respective Ocpp Tags
        ocpp_tag_pks (list[int]): PKs of Ocpp Tags to configure permissions for
    """

    applies_to_all_children: bool
    node_pk: int
    ocpp_tag_pks: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applies_to_all_children = self.applies_to_all_children

        node_pk = self.node_pk

        ocpp_tag_pks = self.ocpp_tag_pks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appliesToAllChildren": applies_to_all_children,
                "nodePk": node_pk,
                "ocppTagPks": ocpp_tag_pks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applies_to_all_children = d.pop("appliesToAllChildren")

        node_pk = d.pop("nodePk")

        ocpp_tag_pks = cast(list[int], d.pop("ocppTagPks"))

        add_permission_dto_for_tag = cls(
            applies_to_all_children=applies_to_all_children,
            node_pk=node_pk,
            ocpp_tag_pks=ocpp_tag_pks,
        )

        add_permission_dto_for_tag.additional_properties = d
        return add_permission_dto_for_tag

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
