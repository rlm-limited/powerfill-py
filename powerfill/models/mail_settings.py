from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mail_settings_enabled_features_item import (
    MailSettingsEnabledFeaturesItem,
    check_mail_settings_enabled_features_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MailSettings")


@_attrs_define
class MailSettings:
    """
    Attributes:
        enabled (bool):
        enabled_features (list[MailSettingsEnabledFeaturesItem] | Unset):
        recipients (list[str] | Unset): List of recipient e-mail addresses
    """

    enabled: bool
    enabled_features: list[MailSettingsEnabledFeaturesItem] | Unset = UNSET
    recipients: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enabled_features: list[str] | Unset = UNSET
        if not isinstance(self.enabled_features, Unset):
            enabled_features = []
            for enabled_features_item_data in self.enabled_features:
                enabled_features_item: str = enabled_features_item_data
                enabled_features.append(enabled_features_item)

        recipients: list[str] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if enabled_features is not UNSET:
            field_dict["enabledFeatures"] = enabled_features
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        _enabled_features = d.pop("enabledFeatures", UNSET)
        enabled_features: list[MailSettingsEnabledFeaturesItem] | Unset = UNSET
        if _enabled_features is not UNSET:
            enabled_features = []
            for enabled_features_item_data in _enabled_features:
                enabled_features_item = check_mail_settings_enabled_features_item(enabled_features_item_data)

                enabled_features.append(enabled_features_item)

        recipients = cast(list[str], d.pop("recipients", UNSET))

        mail_settings = cls(
            enabled=enabled,
            enabled_features=enabled_features,
            recipients=recipients,
        )

        mail_settings.additional_properties = d
        return mail_settings

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
