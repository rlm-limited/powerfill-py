from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteAndNodeInfo")


@_attrs_define
class SiteAndNodeInfo:
    """
    Attributes:
        node_id (int | Unset):
        node_name (str | Unset):
        site_id (int | Unset):
        site_name (str | Unset):
    """

    node_id: int | Unset = UNSET
    node_name: str | Unset = UNSET
    site_id: int | Unset = UNSET
    site_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        node_name = self.node_name

        site_id = self.site_id

        site_name = self.site_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_id = d.pop("nodeId", UNSET)

        node_name = d.pop("nodeName", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        site_and_node_info = cls(
            node_id=node_id,
            node_name=node_name,
            site_id=site_id,
            site_name=site_name,
        )

        site_and_node_info.additional_properties = d
        return site_and_node_info

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
