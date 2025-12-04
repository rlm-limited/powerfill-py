from typing import Literal, cast

ChangeConfigurationParamsKeyType = Literal["CUSTOM", "PREDEFINED"]

CHANGE_CONFIGURATION_PARAMS_KEY_TYPE_VALUES: set[ChangeConfigurationParamsKeyType] = {
    "CUSTOM",
    "PREDEFINED",
}


def check_change_configuration_params_key_type(value: str) -> ChangeConfigurationParamsKeyType:
    if value in CHANGE_CONFIGURATION_PARAMS_KEY_TYPE_VALUES:
        return cast(ChangeConfigurationParamsKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHANGE_CONFIGURATION_PARAMS_KEY_TYPE_VALUES!r}")
