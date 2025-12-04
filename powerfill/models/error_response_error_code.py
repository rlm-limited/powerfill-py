from typing import Literal, cast

ErrorResponseErrorCode = Literal[
    "FormationViolation",
    "GenericError",
    "InternalError",
    "NotImplemented",
    "NotSupported",
    "OccurenceConstraintViolation",
    "PropertyConstraintViolation",
    "ProtocolError",
    "SecurityError",
    "TypeConstraintViolation",
]

ERROR_RESPONSE_ERROR_CODE_VALUES: set[ErrorResponseErrorCode] = {
    "FormationViolation",
    "GenericError",
    "InternalError",
    "NotImplemented",
    "NotSupported",
    "OccurenceConstraintViolation",
    "PropertyConstraintViolation",
    "ProtocolError",
    "SecurityError",
    "TypeConstraintViolation",
}


def check_error_response_error_code(value: str) -> ErrorResponseErrorCode:
    if value in ERROR_RESPONSE_ERROR_CODE_VALUES:
        return cast(ErrorResponseErrorCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_RESPONSE_ERROR_CODE_VALUES!r}")
