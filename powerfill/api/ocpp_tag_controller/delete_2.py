from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.ocpp_tag_overview import OcppTagOverview
from ...types import Response


def _get_kwargs(
    ocpp_tag_pk: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/ocppTags/{ocpp_tag_pk}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiErrorResponse | OcppTagOverview | None:
    if response.status_code == 200:
        response_200 = OcppTagOverview.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiErrorResponse | OcppTagOverview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiErrorResponse | OcppTagOverview]:
    """Deletes an existing Ocpp Tag based on the ocppTagPk.
    Returns the deleted Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | OcppTagOverview]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> ApiErrorResponse | OcppTagOverview | None:
    """Deletes an existing Ocpp Tag based on the ocppTagPk.
    Returns the deleted Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | OcppTagOverview
    """

    return sync_detailed(
        ocpp_tag_pk=ocpp_tag_pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiErrorResponse | OcppTagOverview]:
    """Deletes an existing Ocpp Tag based on the ocppTagPk.
    Returns the deleted Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | OcppTagOverview]
    """

    kwargs = _get_kwargs(
        ocpp_tag_pk=ocpp_tag_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ocpp_tag_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> ApiErrorResponse | OcppTagOverview | None:
    """Deletes an existing Ocpp Tag based on the ocppTagPk.
    Returns the deleted Ocpp Tag.

    Args:
        ocpp_tag_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | OcppTagOverview
    """

    return (
        await asyncio_detailed(
            ocpp_tag_pk=ocpp_tag_pk,
            client=client,
        )
    ).parsed
