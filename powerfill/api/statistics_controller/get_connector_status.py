from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connector_status_list import ConnectorStatusList
from ...models.get_connector_status_status import GetConnectorStatusStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    charge_box_id: str | Unset = UNSET,
    status: GetConnectorStatusStatus | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chargeBoxId"] = charge_box_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/statistics/status",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectorStatusList | None:
    if response.status_code == 200:
        response_200 = ConnectorStatusList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectorStatusList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    status: GetConnectorStatusStatus | Unset = UNSET,
) -> Response[ConnectorStatusList]:
    """Returns the latest status (and optionally the error code) information of connectors of Charge
    Points.
    The status information can be filtered by the given parameters.

    Args:
        charge_box_id (str | Unset):
        status (GetConnectorStatusStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorStatusList]
    """

    kwargs = _get_kwargs(
        charge_box_id=charge_box_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    status: GetConnectorStatusStatus | Unset = UNSET,
) -> ConnectorStatusList | None:
    """Returns the latest status (and optionally the error code) information of connectors of Charge
    Points.
    The status information can be filtered by the given parameters.

    Args:
        charge_box_id (str | Unset):
        status (GetConnectorStatusStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorStatusList
    """

    return sync_detailed(
        client=client,
        charge_box_id=charge_box_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    status: GetConnectorStatusStatus | Unset = UNSET,
) -> Response[ConnectorStatusList]:
    """Returns the latest status (and optionally the error code) information of connectors of Charge
    Points.
    The status information can be filtered by the given parameters.

    Args:
        charge_box_id (str | Unset):
        status (GetConnectorStatusStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorStatusList]
    """

    kwargs = _get_kwargs(
        charge_box_id=charge_box_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    status: GetConnectorStatusStatus | Unset = UNSET,
) -> ConnectorStatusList | None:
    """Returns the latest status (and optionally the error code) information of connectors of Charge
    Points.
    The status information can be filtered by the given parameters.

    Args:
        charge_box_id (str | Unset):
        status (GetConnectorStatusStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorStatusList
    """

    return (
        await asyncio_detailed(
            client=client,
            charge_box_id=charge_box_id,
            status=status,
        )
    ).parsed
