from typing import Literal, cast

ResetParamsResetType = Literal["HARD", "SOFT"]

RESET_PARAMS_RESET_TYPE_VALUES: set[ResetParamsResetType] = {
    "HARD",
    "SOFT",
}


def check_reset_params_reset_type(value: str) -> ResetParamsResetType:
    if value in RESET_PARAMS_RESET_TYPE_VALUES:
        return cast(ResetParamsResetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESET_PARAMS_RESET_TYPE_VALUES!r}")
