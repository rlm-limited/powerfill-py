from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    charge_box_pk: int,
    ocpp_tag_pk: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chargeBoxPk"] = charge_box_pk

    params["ocppTagPk"] = ocpp_tag_pk

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/permissions/isAllowed",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int,
    ocpp_tag_pk: int,
) -> Response[bool]:
    """Checks whether the respective ocppTagPk is allowed to use the service at chargeBoxPk.
    We first check permission on Ocpp Tag level, and otherwise fall back to Ocpp Tag group level.

    Args:
        charge_box_pk (int):
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int,
    ocpp_tag_pk: int,
) -> bool | None:
    """Checks whether the respective ocppTagPk is allowed to use the service at chargeBoxPk.
    We first check permission on Ocpp Tag level, and otherwise fall back to Ocpp Tag group level.

    Args:
        charge_box_pk (int):
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return sync_detailed(
        client=client,
        charge_box_pk=charge_box_pk,
        ocpp_tag_pk=ocpp_tag_pk,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int,
    ocpp_tag_pk: int,
) -> Response[bool]:
    """Checks whether the respective ocppTagPk is allowed to use the service at chargeBoxPk.
    We first check permission on Ocpp Tag level, and otherwise fall back to Ocpp Tag group level.

    Args:
        charge_box_pk (int):
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int,
    ocpp_tag_pk: int,
) -> bool | None:
    """Checks whether the respective ocppTagPk is allowed to use the service at chargeBoxPk.
    We first check permission on Ocpp Tag level, and otherwise fall back to Ocpp Tag group level.

    Args:
        charge_box_pk (int):
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return (
        await asyncio_detailed(
            client=client,
            charge_box_pk=charge_box_pk,
            ocpp_tag_pk=ocpp_tag_pk,
        )
    ).parsed
