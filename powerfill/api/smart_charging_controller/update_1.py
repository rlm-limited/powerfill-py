from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charging_profile_form import ChargingProfileForm
from ...types import Response


def _get_kwargs(
    charging_profile_pk: int,
    *,
    body: ChargingProfileForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/smart-charging/profiles/{charging_profile_pk}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChargingProfileForm | None:
    if response.status_code == 200:
        response_200 = ChargingProfileForm.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChargingProfileForm]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    charging_profile_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargingProfileForm,
) -> Response[ChargingProfileForm]:
    """Updates an existing charging profile with the provided parameters.

    Args:
        charging_profile_pk (int):
        body (ChargingProfileForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargingProfileForm]
    """

    kwargs = _get_kwargs(
        charging_profile_pk=charging_profile_pk,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    charging_profile_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargingProfileForm,
) -> ChargingProfileForm | None:
    """Updates an existing charging profile with the provided parameters.

    Args:
        charging_profile_pk (int):
        body (ChargingProfileForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargingProfileForm
    """

    return sync_detailed(
        charging_profile_pk=charging_profile_pk,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    charging_profile_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargingProfileForm,
) -> Response[ChargingProfileForm]:
    """Updates an existing charging profile with the provided parameters.

    Args:
        charging_profile_pk (int):
        body (ChargingProfileForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargingProfileForm]
    """

    kwargs = _get_kwargs(
        charging_profile_pk=charging_profile_pk,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    charging_profile_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargingProfileForm,
) -> ChargingProfileForm | None:
    """Updates an existing charging profile with the provided parameters.

    Args:
        charging_profile_pk (int):
        body (ChargingProfileForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargingProfileForm
    """

    return (
        await asyncio_detailed(
            charging_profile_pk=charging_profile_pk,
            client=client,
            body=body,
        )
    ).parsed
