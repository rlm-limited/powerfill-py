from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcppTagForm")


@_attrs_define
class OcppTagForm:
    """
    Attributes:
        id_tag (str):     This field is set when adding an OCPP Tag, and cannot be changed later.
                Will be used in create/insert flows. Will be ignored in update flows.
        expiry_date (datetime.datetime | Unset): ISO 8601 date/time with timezone. Example: `2024-08-25T14:30:00.000Z`
        max_active_transaction_count (int | Unset): Set to 0 to block this tag.
            Set to a negative value to disable concurrent transaction checks (i.e. every transaction will be allowed).
            Set to a positive value to control the number of active transactions that is allowed.
        note (str | Unset):
        parent_id_tag (str | Unset):
    """

    id_tag: str
    expiry_date: datetime.datetime | Unset = UNSET
    max_active_transaction_count: int | Unset = UNSET
    note: str | Unset = UNSET
    parent_id_tag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_tag = self.id_tag

        expiry_date: str | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        max_active_transaction_count = self.max_active_transaction_count

        note = self.note

        parent_id_tag = self.parent_id_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idTag": id_tag,
            }
        )
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if max_active_transaction_count is not UNSET:
            field_dict["maxActiveTransactionCount"] = max_active_transaction_count
        if note is not UNSET:
            field_dict["note"] = note
        if parent_id_tag is not UNSET:
            field_dict["parentIdTag"] = parent_id_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id_tag = d.pop("idTag")

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: datetime.datetime | Unset
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        max_active_transaction_count = d.pop("maxActiveTransactionCount", UNSET)

        note = d.pop("note", UNSET)

        parent_id_tag = d.pop("parentIdTag", UNSET)

        ocpp_tag_form = cls(
            id_tag=id_tag,
            expiry_date=expiry_date,
            max_active_transaction_count=max_active_transaction_count,
            note=note,
            parent_id_tag=parent_id_tag,
        )

        ocpp_tag_form.additional_properties = d
        return ocpp_tag_form

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
