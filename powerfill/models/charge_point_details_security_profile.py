from typing import Literal, cast

ChargePointDetailsSecurityProfile = Literal["Profile_0", "Profile_1", "Profile_2", "Profile_3"]

CHARGE_POINT_DETAILS_SECURITY_PROFILE_VALUES: set[ChargePointDetailsSecurityProfile] = {
    "Profile_0",
    "Profile_1",
    "Profile_2",
    "Profile_3",
}


def check_charge_point_details_security_profile(value: str) -> ChargePointDetailsSecurityProfile:
    if value in CHARGE_POINT_DETAILS_SECURITY_PROFILE_VALUES:
        return cast(ChargePointDetailsSecurityProfile, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHARGE_POINT_DETAILS_SECURITY_PROFILE_VALUES!r}")
