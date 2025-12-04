from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_form_notification_features_item import (
    UserFormNotificationFeaturesItem,
    check_user_form_notification_features_item,
)
from ..models.user_form_sex import UserFormSex, check_user_form_sex
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.ocpp_tag_entry import OcppTagEntry


T = TypeVar("T", bound="UserForm")


@_attrs_define
class UserForm:
    """
    Attributes:
        address (Address | Unset):
        birth_day (datetime.date | Unset):
        email (str | Unset):
        first_name (str | Unset):
        id_tag_list (list[str] | Unset):
        last_name (str | Unset):
        note (str | Unset):
        notification_features (list[UserFormNotificationFeaturesItem] | Unset): Only the following values are valid:
            OcppStationStatusFailure, OcppTransactionStarted, OcppStationStatusSuspendedEV, OcppTransactionEnded
        ocpp_tag_entries (list[OcppTagEntry] | Unset):
        phone (str | Unset):
        sex (UserFormSex | Unset):
        user_pk (int | Unset):
    """

    address: Address | Unset = UNSET
    birth_day: datetime.date | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    id_tag_list: list[str] | Unset = UNSET
    last_name: str | Unset = UNSET
    note: str | Unset = UNSET
    notification_features: list[UserFormNotificationFeaturesItem] | Unset = UNSET
    ocpp_tag_entries: list[OcppTagEntry] | Unset = UNSET
    phone: str | Unset = UNSET
    sex: UserFormSex | Unset = UNSET
    user_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        birth_day: str | Unset = UNSET
        if not isinstance(self.birth_day, Unset):
            birth_day = self.birth_day.isoformat()

        email = self.email

        first_name = self.first_name

        id_tag_list: list[str] | Unset = UNSET
        if not isinstance(self.id_tag_list, Unset):
            id_tag_list = self.id_tag_list

        last_name = self.last_name

        note = self.note

        notification_features: list[str] | Unset = UNSET
        if not isinstance(self.notification_features, Unset):
            notification_features = []
            for notification_features_item_data in self.notification_features:
                notification_features_item: str = notification_features_item_data
                notification_features.append(notification_features_item)

        ocpp_tag_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ocpp_tag_entries, Unset):
            ocpp_tag_entries = []
            for ocpp_tag_entries_item_data in self.ocpp_tag_entries:
                ocpp_tag_entries_item = ocpp_tag_entries_item_data.to_dict()
                ocpp_tag_entries.append(ocpp_tag_entries_item)

        phone = self.phone

        sex: str | Unset = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex

        user_pk = self.user_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if birth_day is not UNSET:
            field_dict["birthDay"] = birth_day
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id_tag_list is not UNSET:
            field_dict["idTagList"] = id_tag_list
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if note is not UNSET:
            field_dict["note"] = note
        if notification_features is not UNSET:
            field_dict["notificationFeatures"] = notification_features
        if ocpp_tag_entries is not UNSET:
            field_dict["ocppTagEntries"] = ocpp_tag_entries
        if phone is not UNSET:
            field_dict["phone"] = phone
        if sex is not UNSET:
            field_dict["sex"] = sex
        if user_pk is not UNSET:
            field_dict["userPk"] = user_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.ocpp_tag_entry import OcppTagEntry

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _birth_day = d.pop("birthDay", UNSET)
        birth_day: datetime.date | Unset
        if isinstance(_birth_day, Unset):
            birth_day = UNSET
        else:
            birth_day = isoparse(_birth_day).date()

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        id_tag_list = cast(list[str], d.pop("idTagList", UNSET))

        last_name = d.pop("lastName", UNSET)

        note = d.pop("note", UNSET)

        _notification_features = d.pop("notificationFeatures", UNSET)
        notification_features: list[UserFormNotificationFeaturesItem] | Unset = UNSET
        if _notification_features is not UNSET:
            notification_features = []
            for notification_features_item_data in _notification_features:
                notification_features_item = check_user_form_notification_features_item(notification_features_item_data)

                notification_features.append(notification_features_item)

        _ocpp_tag_entries = d.pop("ocppTagEntries", UNSET)
        ocpp_tag_entries: list[OcppTagEntry] | Unset = UNSET
        if _ocpp_tag_entries is not UNSET:
            ocpp_tag_entries = []
            for ocpp_tag_entries_item_data in _ocpp_tag_entries:
                ocpp_tag_entries_item = OcppTagEntry.from_dict(ocpp_tag_entries_item_data)

                ocpp_tag_entries.append(ocpp_tag_entries_item)

        phone = d.pop("phone", UNSET)

        _sex = d.pop("sex", UNSET)
        sex: UserFormSex | Unset
        if isinstance(_sex, Unset):
            sex = UNSET
        else:
            sex = check_user_form_sex(_sex)

        user_pk = d.pop("userPk", UNSET)

        user_form = cls(
            address=address,
            birth_day=birth_day,
            email=email,
            first_name=first_name,
            id_tag_list=id_tag_list,
            last_name=last_name,
            note=note,
            notification_features=notification_features,
            ocpp_tag_entries=ocpp_tag_entries,
            phone=phone,
            sex=sex,
            user_pk=user_pk,
        )

        user_form.additional_properties = d
        return user_form

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
