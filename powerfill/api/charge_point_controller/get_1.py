from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.charge_point_overview import ChargePointOverview
from ...models.get_1_heartbeat_period import Get1HeartbeatPeriod
from ...models.get_1_ocpp_version import Get1OcppVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    charge_box_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    note: str | Unset = UNSET,
    ocpp_version: Get1OcppVersion | Unset = UNSET,
    heartbeat_period: Get1HeartbeatPeriod | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chargeBoxId"] = charge_box_id

    params["description"] = description

    params["note"] = note

    json_ocpp_version: str | Unset = UNSET
    if not isinstance(ocpp_version, Unset):
        json_ocpp_version = ocpp_version

    params["ocppVersion"] = json_ocpp_version

    json_heartbeat_period: str | Unset = UNSET
    if not isinstance(heartbeat_period, Unset):
        json_heartbeat_period = heartbeat_period

    params["heartbeatPeriod"] = json_heartbeat_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chargePoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ChargePointOverview] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChargePointOverview.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ChargePointOverview]]:
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
    description: str | Unset = UNSET,
    note: str | Unset = UNSET,
    ocpp_version: Get1OcppVersion | Unset = UNSET,
    heartbeat_period: Get1HeartbeatPeriod | Unset = UNSET,
) -> Response[list[ChargePointOverview]]:
    """Returns a list of Charge Points based on the query parameters.
    The query parameters can be used to filter the Charge Points.
    The response payload contains only an overview each Charge Point.
    Please refer to <code>GET /api/v1/chargePoints/{chargeBoxPk}</code> for the details of a Charge
    Point.

    Args:
        charge_box_id (str | Unset): The unique OCPP identifier of the Charge Point
        description (str | Unset): The description of the Charge Point
        note (str | Unset): Query by the note associated with the Charge Point. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        ocpp_version (Get1OcppVersion | Unset): The OCPP version of the Charge Point
        heartbeat_period (Get1HeartbeatPeriod | Unset): The heartbeat period of the Charge Point

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargePointOverview]]
    """

    kwargs = _get_kwargs(
        charge_box_id=charge_box_id,
        description=description,
        note=note,
        ocpp_version=ocpp_version,
        heartbeat_period=heartbeat_period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    note: str | Unset = UNSET,
    ocpp_version: Get1OcppVersion | Unset = UNSET,
    heartbeat_period: Get1HeartbeatPeriod | Unset = UNSET,
) -> list[ChargePointOverview] | None:
    """Returns a list of Charge Points based on the query parameters.
    The query parameters can be used to filter the Charge Points.
    The response payload contains only an overview each Charge Point.
    Please refer to <code>GET /api/v1/chargePoints/{chargeBoxPk}</code> for the details of a Charge
    Point.

    Args:
        charge_box_id (str | Unset): The unique OCPP identifier of the Charge Point
        description (str | Unset): The description of the Charge Point
        note (str | Unset): Query by the note associated with the Charge Point. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        ocpp_version (Get1OcppVersion | Unset): The OCPP version of the Charge Point
        heartbeat_period (Get1HeartbeatPeriod | Unset): The heartbeat period of the Charge Point

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargePointOverview]
    """

    return sync_detailed(
        client=client,
        charge_box_id=charge_box_id,
        description=description,
        note=note,
        ocpp_version=ocpp_version,
        heartbeat_period=heartbeat_period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    note: str | Unset = UNSET,
    ocpp_version: Get1OcppVersion | Unset = UNSET,
    heartbeat_period: Get1HeartbeatPeriod | Unset = UNSET,
) -> Response[list[ChargePointOverview]]:
    """Returns a list of Charge Points based on the query parameters.
    The query parameters can be used to filter the Charge Points.
    The response payload contains only an overview each Charge Point.
    Please refer to <code>GET /api/v1/chargePoints/{chargeBoxPk}</code> for the details of a Charge
    Point.

    Args:
        charge_box_id (str | Unset): The unique OCPP identifier of the Charge Point
        description (str | Unset): The description of the Charge Point
        note (str | Unset): Query by the note associated with the Charge Point. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        ocpp_version (Get1OcppVersion | Unset): The OCPP version of the Charge Point
        heartbeat_period (Get1HeartbeatPeriod | Unset): The heartbeat period of the Charge Point

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ChargePointOverview]]
    """

    kwargs = _get_kwargs(
        charge_box_id=charge_box_id,
        description=description,
        note=note,
        ocpp_version=ocpp_version,
        heartbeat_period=heartbeat_period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    charge_box_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    note: str | Unset = UNSET,
    ocpp_version: Get1OcppVersion | Unset = UNSET,
    heartbeat_period: Get1HeartbeatPeriod | Unset = UNSET,
) -> list[ChargePointOverview] | None:
    """Returns a list of Charge Points based on the query parameters.
    The query parameters can be used to filter the Charge Points.
    The response payload contains only an overview each Charge Point.
    Please refer to <code>GET /api/v1/chargePoints/{chargeBoxPk}</code> for the details of a Charge
    Point.

    Args:
        charge_box_id (str | Unset): The unique OCPP identifier of the Charge Point
        description (str | Unset): The description of the Charge Point
        note (str | Unset): Query by the note associated with the Charge Point. The value of this
            field does not have to exactly match the note. A substring is also accepted.
        ocpp_version (Get1OcppVersion | Unset): The OCPP version of the Charge Point
        heartbeat_period (Get1HeartbeatPeriod | Unset): The heartbeat period of the Charge Point

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ChargePointOverview]
    """

    return (
        await asyncio_detailed(
            client=client,
            charge_box_id=charge_box_id,
            description=description,
            note=note,
            ocpp_version=ocpp_version,
            heartbeat_period=heartbeat_period,
        )
    ).parsed
