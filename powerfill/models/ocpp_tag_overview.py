from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OcppTagOverview")


@_attrs_define
class OcppTagOverview:
    """
    Attributes:
        active_transaction_count (int | Unset): The number of currently active transactions for this OCPP tag
        blocked (bool | Unset): Is the OCPP tag blocked?
        expiry_date (datetime.datetime | Unset): The date/time at which the OCPP tag will expire (if set)
        id_tag (str | Unset): The OCPP tag
        in_transaction (bool | Unset): Has the OCPP tag active transactions (i.e. ongoing charging sessions)?
        max_active_transaction_count (int | Unset): The maximum number of active transactions allowed for this OCPP tag
        note (str | Unset): An additional note
        ocpp_tag_pk (int | Unset): PK of the OCPP tag
        parent_id_tag (str | Unset): The parent OCPP tag of this OCPP tag
        parent_ocpp_tag_pk (int | Unset): PK of the parent OCPP tag of this OCPP tag
        user_pk (int | Unset): PK of the user this OCPP tag belongs to (if any)
    """

    active_transaction_count: int | Unset = UNSET
    blocked: bool | Unset = UNSET
    expiry_date: datetime.datetime | Unset = UNSET
    id_tag: str | Unset = UNSET
    in_transaction: bool | Unset = UNSET
    max_active_transaction_count: int | Unset = UNSET
    note: str | Unset = UNSET
    ocpp_tag_pk: int | Unset = UNSET
    parent_id_tag: str | Unset = UNSET
    parent_ocpp_tag_pk: int | Unset = UNSET
    user_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_transaction_count = self.active_transaction_count

        blocked = self.blocked

        expiry_date: str | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat()

        id_tag = self.id_tag

        in_transaction = self.in_transaction

        max_active_transaction_count = self.max_active_transaction_count

        note = self.note

        ocpp_tag_pk = self.ocpp_tag_pk

        parent_id_tag = self.parent_id_tag

        parent_ocpp_tag_pk = self.parent_ocpp_tag_pk

        user_pk = self.user_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_transaction_count is not UNSET:
            field_dict["activeTransactionCount"] = active_transaction_count
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if id_tag is not UNSET:
            field_dict["idTag"] = id_tag
        if in_transaction is not UNSET:
            field_dict["inTransaction"] = in_transaction
        if max_active_transaction_count is not UNSET:
            field_dict["maxActiveTransactionCount"] = max_active_transaction_count
        if note is not UNSET:
            field_dict["note"] = note
        if ocpp_tag_pk is not UNSET:
            field_dict["ocppTagPk"] = ocpp_tag_pk
        if parent_id_tag is not UNSET:
            field_dict["parentIdTag"] = parent_id_tag
        if parent_ocpp_tag_pk is not UNSET:
            field_dict["parentOcppTagPk"] = parent_ocpp_tag_pk
        if user_pk is not UNSET:
            field_dict["userPk"] = user_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_transaction_count = d.pop("activeTransactionCount", UNSET)

        blocked = d.pop("blocked", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: datetime.datetime | Unset
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        id_tag = d.pop("idTag", UNSET)

        in_transaction = d.pop("inTransaction", UNSET)

        max_active_transaction_count = d.pop("maxActiveTransactionCount", UNSET)

        note = d.pop("note", UNSET)

        ocpp_tag_pk = d.pop("ocppTagPk", UNSET)

        parent_id_tag = d.pop("parentIdTag", UNSET)

        parent_ocpp_tag_pk = d.pop("parentOcppTagPk", UNSET)

        user_pk = d.pop("userPk", UNSET)

        ocpp_tag_overview = cls(
            active_transaction_count=active_transaction_count,
            blocked=blocked,
            expiry_date=expiry_date,
            id_tag=id_tag,
            in_transaction=in_transaction,
            max_active_transaction_count=max_active_transaction_count,
            note=note,
            ocpp_tag_pk=ocpp_tag_pk,
            parent_id_tag=parent_id_tag,
            parent_ocpp_tag_pk=parent_ocpp_tag_pk,
            user_pk=user_pk,
        )

        ocpp_tag_overview.additional_properties = d
        return ocpp_tag_overview

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
