from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charging_profile_assignment import ChargingProfileAssignment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    charge_box_pk: int | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    charging_profile_pk: int | Unset = UNSET,
    charging_profile_description: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chargeBoxPk"] = charge_box_pk

    params["chargeBoxId"] = charge_box_id

    params["chargingProfilePk"] = charging_profile_pk

    params["chargingProfileDescription"] = charging_profile_description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/smart-charging/profiles/assignments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ChargingProfileAssignment] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChargingProfileAssignment.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ChargingProfileAssignment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    charging_profile_pk: int | Unset = UNSET,
    charging_profile_description: str | Unset = UNSET,
) -> Response[list[ChargingProfileAssignment]]:
    """Returns an overview of smart charging profiles assigned to charging stations, filtered by query
    parameters.

    Args:
        charge_box_pk (int | Unset):
        charge_box_id (str | Unset):
        charging_profile_pk (int | Unset):
        charging_profile_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargingProfileAssignment]]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        charge_box_id=charge_box_id,
        charging_profile_pk=charging_profile_pk,
        charging_profile_description=charging_profile_description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    charging_profile_pk: int | Unset = UNSET,
    charging_profile_description: str | Unset = UNSET,
) -> list[ChargingProfileAssignment] | None:
    """Returns an overview of smart charging profiles assigned to charging stations, filtered by query
    parameters.

    Args:
        charge_box_pk (int | Unset):
        charge_box_id (str | Unset):
        charging_profile_pk (int | Unset):
        charging_profile_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargingProfileAssignment]
    """

    return sync_detailed(
        client=client,
        charge_box_pk=charge_box_pk,
        charge_box_id=charge_box_id,
        charging_profile_pk=charging_profile_pk,
        charging_profile_description=charging_profile_description,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    charging_profile_pk: int | Unset = UNSET,
    charging_profile_description: str | Unset = UNSET,
) -> Response[list[ChargingProfileAssignment]]:
    """Returns an overview of smart charging profiles assigned to charging stations, filtered by query
    parameters.

    Args:
        charge_box_pk (int | Unset):
        charge_box_id (str | Unset):
        charging_profile_pk (int | Unset):
        charging_profile_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargingProfileAssignment]]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        charge_box_id=charge_box_id,
        charging_profile_pk=charging_profile_pk,
        charging_profile_description=charging_profile_description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    charge_box_pk: int | Unset = UNSET,
    charge_box_id: str | Unset = UNSET,
    charging_profile_pk: int | Unset = UNSET,
    charging_profile_description: str | Unset = UNSET,
) -> list[ChargingProfileAssignment] | None:
    """Returns an overview of smart charging profiles assigned to charging stations, filtered by query
    parameters.

    Args:
        charge_box_pk (int | Unset):
        charge_box_id (str | Unset):
        charging_profile_pk (int | Unset):
        charging_profile_description (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargingProfileAssignment]
    """

    return (
        await asyncio_detailed(
            client=client,
            charge_box_pk=charge_box_pk,
            charge_box_id=charge_box_id,
            charging_profile_pk=charging_profile_pk,
            charging_profile_description=charging_profile_description,
        )
    ).parsed
