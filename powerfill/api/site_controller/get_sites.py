from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_dto_list import SiteDtoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_details: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["withDetails"] = with_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/sites",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SiteDtoList | None:
    if response.status_code == 200:
        response_200 = SiteDtoList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SiteDtoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    with_details: bool | Unset = False,
) -> Response[SiteDtoList]:
    """Returns all sites.
    Depending on the number and complexity of the sites, this is potentially an expensive call.
    Please refer to <code>GET /api/v1/sites/{id}</code> for the details of how a site object looks like.

    Args:
        with_details (bool | Unset): Flag to control whether the returned data should contain the
            address information and the
            complete site structure tree or not. If the latter, only the site id and name will be
            returned.
             Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDtoList]
    """

    kwargs = _get_kwargs(
        with_details=with_details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    with_details: bool | Unset = False,
) -> SiteDtoList | None:
    """Returns all sites.
    Depending on the number and complexity of the sites, this is potentially an expensive call.
    Please refer to <code>GET /api/v1/sites/{id}</code> for the details of how a site object looks like.

    Args:
        with_details (bool | Unset): Flag to control whether the returned data should contain the
            address information and the
            complete site structure tree or not. If the latter, only the site id and name will be
            returned.
             Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDtoList
    """

    return sync_detailed(
        client=client,
        with_details=with_details,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    with_details: bool | Unset = False,
) -> Response[SiteDtoList]:
    """Returns all sites.
    Depending on the number and complexity of the sites, this is potentially an expensive call.
    Please refer to <code>GET /api/v1/sites/{id}</code> for the details of how a site object looks like.

    Args:
        with_details (bool | Unset): Flag to control whether the returned data should contain the
            address information and the
            complete site structure tree or not. If the latter, only the site id and name will be
            returned.
             Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SiteDtoList]
    """

    kwargs = _get_kwargs(
        with_details=with_details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    with_details: bool | Unset = False,
) -> SiteDtoList | None:
    """Returns all sites.
    Depending on the number and complexity of the sites, this is potentially an expensive call.
    Please refer to <code>GET /api/v1/sites/{id}</code> for the details of how a site object looks like.

    Args:
        with_details (bool | Unset): Flag to control whether the returned data should contain the
            address information and the
            complete site structure tree or not. If the latter, only the site id and name will be
            returned.
             Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SiteDtoList
    """

    return (
        await asyncio_detailed(
            client=client,
            with_details=with_details,
        )
    ).parsed
