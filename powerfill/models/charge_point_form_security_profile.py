from typing import Literal, cast

ChargePointFormSecurityProfile = Literal["Profile_0", "Profile_1", "Profile_2", "Profile_3"]

CHARGE_POINT_FORM_SECURITY_PROFILE_VALUES: set[ChargePointFormSecurityProfile] = {
    "Profile_0",
    "Profile_1",
    "Profile_2",
    "Profile_3",
}


def check_charge_point_form_security_profile(value: str) -> ChargePointFormSecurityProfile:
    if value in CHARGE_POINT_FORM_SECURITY_PROFILE_VALUES:
        return cast(ChargePointFormSecurityProfile, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHARGE_POINT_FORM_SECURITY_PROFILE_VALUES!r}")
