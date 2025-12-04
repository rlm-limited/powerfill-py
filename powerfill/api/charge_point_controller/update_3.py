from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_point_details import ChargePointDetails
from ...models.charge_point_form import ChargePointForm
from ...types import Response


def _get_kwargs(
    charge_box_pk: int,
    *,
    body: ChargePointForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/chargePoints/{charge_box_pk}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChargePointDetails | None:
    if response.status_code == 200:
        response_200 = ChargePointDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChargePointDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    charge_box_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargePointForm,
) -> Response[ChargePointDetails]:
    """Updates an existing Charge Point with the provided parameters.

    Args:
        charge_box_pk (int):
        body (ChargePointForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargePointDetails]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    charge_box_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargePointForm,
) -> ChargePointDetails | None:
    """Updates an existing Charge Point with the provided parameters.

    Args:
        charge_box_pk (int):
        body (ChargePointForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargePointDetails
    """

    return sync_detailed(
        charge_box_pk=charge_box_pk,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    charge_box_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargePointForm,
) -> Response[ChargePointDetails]:
    """Updates an existing Charge Point with the provided parameters.

    Args:
        charge_box_pk (int):
        body (ChargePointForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChargePointDetails]
    """

    kwargs = _get_kwargs(
        charge_box_pk=charge_box_pk,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    charge_box_pk: int,
    *,
    client: AuthenticatedClient | Client,
    body: ChargePointForm,
) -> ChargePointDetails | None:
    """Updates an existing Charge Point with the provided parameters.

    Args:
        charge_box_pk (int):
        body (ChargePointForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChargePointDetails
    """

    return (
        await asyncio_detailed(
            charge_box_pk=charge_box_pk,
            client=client,
            body=body,
        )
    ).parsed
