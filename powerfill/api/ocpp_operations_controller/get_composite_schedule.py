from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_composite_schedule_params import GetCompositeScheduleParams
from ...models.ocpp_operation_response_get_composite_schedule_response import (
    OcppOperationResponseGetCompositeScheduleResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: GetCompositeScheduleParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/operations/GetCompositeSchedule",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OcppOperationResponseGetCompositeScheduleResponse | None:
    if response.status_code == 200:
        response_200 = OcppOperationResponseGetCompositeScheduleResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OcppOperationResponseGetCompositeScheduleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompositeScheduleParams,
) -> Response[OcppOperationResponseGetCompositeScheduleResponse]:
    """
    Args:
        body (GetCompositeScheduleParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OcppOperationResponseGetCompositeScheduleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompositeScheduleParams,
) -> OcppOperationResponseGetCompositeScheduleResponse | None:
    """
    Args:
        body (GetCompositeScheduleParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OcppOperationResponseGetCompositeScheduleResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompositeScheduleParams,
) -> Response[OcppOperationResponseGetCompositeScheduleResponse]:
    """
    Args:
        body (GetCompositeScheduleParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OcppOperationResponseGetCompositeScheduleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetCompositeScheduleParams,
) -> OcppOperationResponseGetCompositeScheduleResponse | None:
    """
    Args:
        body (GetCompositeScheduleParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OcppOperationResponseGetCompositeScheduleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
