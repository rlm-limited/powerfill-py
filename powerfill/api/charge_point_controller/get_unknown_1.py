from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unknown_charge_points_dto import UnknownChargePointsDto
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chargePoints/unknown",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UnknownChargePointsDto | None:
    if response.status_code == 200:
        response_200 = UnknownChargePointsDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UnknownChargePointsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[UnknownChargePointsDto]:
    """Returns a list of unknown Charge Points.
    These have attempted to connect and send a boot notification but were not present in database.
    <code>key</code> field in response payload is the chargeBoxId of the Charge Point.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnknownChargePointsDto]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> UnknownChargePointsDto | None:
    """Returns a list of unknown Charge Points.
    These have attempted to connect and send a boot notification but were not present in database.
    <code>key</code> field in response payload is the chargeBoxId of the Charge Point.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnknownChargePointsDto
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[UnknownChargePointsDto]:
    """Returns a list of unknown Charge Points.
    These have attempted to connect and send a boot notification but were not present in database.
    <code>key</code> field in response payload is the chargeBoxId of the Charge Point.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnknownChargePointsDto]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> UnknownChargePointsDto | None:
    """Returns a list of unknown Charge Points.
    These have attempted to connect and send a boot notification but were not present in database.
    <code>key</code> field in response payload is the chargeBoxId of the Charge Point.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnknownChargePointsDto
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
