from typing import Literal, cast

UserFormSex = Literal["FEMALE", "MALE", "OTHER"]

USER_FORM_SEX_VALUES: set[UserFormSex] = {
    "FEMALE",
    "MALE",
    "OTHER",
}


def check_user_form_sex(value: str) -> UserFormSex:
    if value in USER_FORM_SEX_VALUES:
        return cast(UserFormSex, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_FORM_SEX_VALUES!r}")
