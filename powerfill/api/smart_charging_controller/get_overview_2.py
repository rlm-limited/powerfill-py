import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charging_profile_overview import ChargingProfileOverview
from ...models.get_overview_2_profile_kind import GetOverview2ProfileKind
from ...models.get_overview_2_profile_purpose import GetOverview2ProfilePurpose
from ...models.get_overview_2_recurrency_kind import GetOverview2RecurrencyKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    charging_profile_pk: int | Unset = UNSET,
    stack_level: int | Unset = UNSET,
    description: str | Unset = UNSET,
    profile_purpose: GetOverview2ProfilePurpose | Unset = UNSET,
    profile_kind: GetOverview2ProfileKind | Unset = UNSET,
    recurrency_kind: GetOverview2RecurrencyKind | Unset = UNSET,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chargingProfilePk"] = charging_profile_pk

    params["stackLevel"] = stack_level

    params["description"] = description

    json_profile_purpose: str | Unset = UNSET
    if not isinstance(profile_purpose, Unset):
        json_profile_purpose = profile_purpose

    params["profilePurpose"] = json_profile_purpose

    json_profile_kind: str | Unset = UNSET
    if not isinstance(profile_kind, Unset):
        json_profile_kind = profile_kind

    params["profileKind"] = json_profile_kind

    json_recurrency_kind: str | Unset = UNSET
    if not isinstance(recurrency_kind, Unset):
        json_recurrency_kind = recurrency_kind

    params["recurrencyKind"] = json_recurrency_kind

    json_valid_from: str | Unset = UNSET
    if not isinstance(valid_from, Unset):
        json_valid_from = valid_from.isoformat()
    params["validFrom"] = json_valid_from

    json_valid_to: str | Unset = UNSET
    if not isinstance(valid_to, Unset):
        json_valid_to = valid_to.isoformat()
    params["validTo"] = json_valid_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/smart-charging/profiles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ChargingProfileOverview] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChargingProfileOverview.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ChargingProfileOverview]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    charging_profile_pk: int | Unset = UNSET,
    stack_level: int | Unset = UNSET,
    description: str | Unset = UNSET,
    profile_purpose: GetOverview2ProfilePurpose | Unset = UNSET,
    profile_kind: GetOverview2ProfileKind | Unset = UNSET,
    recurrency_kind: GetOverview2RecurrencyKind | Unset = UNSET,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> Response[list[ChargingProfileOverview]]:
    """Returns a list of charging profiles based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        charging_profile_pk (int | Unset):
        stack_level (int | Unset):
        description (str | Unset):
        profile_purpose (GetOverview2ProfilePurpose | Unset):
        profile_kind (GetOverview2ProfileKind | Unset):
        recurrency_kind (GetOverview2RecurrencyKind | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargingProfileOverview]]
    """

    kwargs = _get_kwargs(
        charging_profile_pk=charging_profile_pk,
        stack_level=stack_level,
        description=description,
        profile_purpose=profile_purpose,
        profile_kind=profile_kind,
        recurrency_kind=recurrency_kind,
        valid_from=valid_from,
        valid_to=valid_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    charging_profile_pk: int | Unset = UNSET,
    stack_level: int | Unset = UNSET,
    description: str | Unset = UNSET,
    profile_purpose: GetOverview2ProfilePurpose | Unset = UNSET,
    profile_kind: GetOverview2ProfileKind | Unset = UNSET,
    recurrency_kind: GetOverview2RecurrencyKind | Unset = UNSET,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> list[ChargingProfileOverview] | None:
    """Returns a list of charging profiles based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        charging_profile_pk (int | Unset):
        stack_level (int | Unset):
        description (str | Unset):
        profile_purpose (GetOverview2ProfilePurpose | Unset):
        profile_kind (GetOverview2ProfileKind | Unset):
        recurrency_kind (GetOverview2RecurrencyKind | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargingProfileOverview]
    """

    return sync_detailed(
        client=client,
        charging_profile_pk=charging_profile_pk,
        stack_level=stack_level,
        description=description,
        profile_purpose=profile_purpose,
        profile_kind=profile_kind,
        recurrency_kind=recurrency_kind,
        valid_from=valid_from,
        valid_to=valid_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    charging_profile_pk: int | Unset = UNSET,
    stack_level: int | Unset = UNSET,
    description: str | Unset = UNSET,
    profile_purpose: GetOverview2ProfilePurpose | Unset = UNSET,
    profile_kind: GetOverview2ProfileKind | Unset = UNSET,
    recurrency_kind: GetOverview2RecurrencyKind | Unset = UNSET,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> Response[list[ChargingProfileOverview]]:
    """Returns a list of charging profiles based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        charging_profile_pk (int | Unset):
        stack_level (int | Unset):
        description (str | Unset):
        profile_purpose (GetOverview2ProfilePurpose | Unset):
        profile_kind (GetOverview2ProfileKind | Unset):
        recurrency_kind (GetOverview2RecurrencyKind | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargingProfileOverview]]
    """

    kwargs = _get_kwargs(
        charging_profile_pk=charging_profile_pk,
        stack_level=stack_level,
        description=description,
        profile_purpose=profile_purpose,
        profile_kind=profile_kind,
        recurrency_kind=recurrency_kind,
        valid_from=valid_from,
        valid_to=valid_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    charging_profile_pk: int | Unset = UNSET,
    stack_level: int | Unset = UNSET,
    description: str | Unset = UNSET,
    profile_purpose: GetOverview2ProfilePurpose | Unset = UNSET,
    profile_kind: GetOverview2ProfileKind | Unset = UNSET,
    recurrency_kind: GetOverview2RecurrencyKind | Unset = UNSET,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> list[ChargingProfileOverview] | None:
    """Returns a list of charging profiles based on the query parameters.
    The query parameters can be used to filter the results.

    Args:
        charging_profile_pk (int | Unset):
        stack_level (int | Unset):
        description (str | Unset):
        profile_purpose (GetOverview2ProfilePurpose | Unset):
        profile_kind (GetOverview2ProfileKind | Unset):
        recurrency_kind (GetOverview2RecurrencyKind | Unset):
        valid_from (datetime.datetime | Unset):
        valid_to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargingProfileOverview]
    """

    return (
        await asyncio_detailed(
            client=client,
            charging_profile_pk=charging_profile_pk,
            stack_level=stack_level,
            description=description,
            profile_purpose=profile_purpose,
            profile_kind=profile_kind,
            recurrency_kind=recurrency_kind,
            valid_from=valid_from,
            valid_to=valid_to,
        )
    ).parsed
