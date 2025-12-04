from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_overview_notification_features_item import (
    UserOverviewNotificationFeaturesItem,
    check_user_overview_notification_features_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocpp_tag_entry import OcppTagEntry


T = TypeVar("T", bound="UserOverview")


@_attrs_define
class UserOverview:
    """
    Attributes:
        email (str | Unset):
        first_name (str | Unset):
        full_name (str | Unset):
        last_name (str | Unset):
        notification_features (list[UserOverviewNotificationFeaturesItem] | Unset): Only the following values are valid:
            OcppStationStatusFailure, OcppTransactionStarted, OcppStationStatusSuspendedEV, OcppTransactionEnded
        ocpp_tag_entries (list[OcppTagEntry] | Unset):
        phone (str | Unset):
        user_pk (int | Unset):
    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    full_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    notification_features: list[UserOverviewNotificationFeaturesItem] | Unset = UNSET
    ocpp_tag_entries: list[OcppTagEntry] | Unset = UNSET
    phone: str | Unset = UNSET
    user_pk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        full_name = self.full_name

        last_name = self.last_name

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

        user_pk = self.user_pk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if notification_features is not UNSET:
            field_dict["notificationFeatures"] = notification_features
        if ocpp_tag_entries is not UNSET:
            field_dict["ocppTagEntries"] = ocpp_tag_entries
        if phone is not UNSET:
            field_dict["phone"] = phone
        if user_pk is not UNSET:
            field_dict["userPk"] = user_pk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ocpp_tag_entry import OcppTagEntry

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        full_name = d.pop("fullName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _notification_features = d.pop("notificationFeatures", UNSET)
        notification_features: list[UserOverviewNotificationFeaturesItem] | Unset = UNSET
        if _notification_features is not UNSET:
            notification_features = []
            for notification_features_item_data in _notification_features:
                notification_features_item = check_user_overview_notification_features_item(
                    notification_features_item_data
                )

                notification_features.append(notification_features_item)

        _ocpp_tag_entries = d.pop("ocppTagEntries", UNSET)
        ocpp_tag_entries: list[OcppTagEntry] | Unset = UNSET
        if _ocpp_tag_entries is not UNSET:
            ocpp_tag_entries = []
            for ocpp_tag_entries_item_data in _ocpp_tag_entries:
                ocpp_tag_entries_item = OcppTagEntry.from_dict(ocpp_tag_entries_item_data)

                ocpp_tag_entries.append(ocpp_tag_entries_item)

        phone = d.pop("phone", UNSET)

        user_pk = d.pop("userPk", UNSET)

        user_overview = cls(
            email=email,
            first_name=first_name,
            full_name=full_name,
            last_name=last_name,
            notification_features=notification_features,
            ocpp_tag_entries=ocpp_tag_entries,
            phone=phone,
            user_pk=user_pk,
        )

        user_overview.additional_properties = d
        return user_overview

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
