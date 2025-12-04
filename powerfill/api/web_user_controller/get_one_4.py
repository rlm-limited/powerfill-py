from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_user_dto import WebUserDto
from ...types import Response


def _get_kwargs(
    web_user_pk: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/webUsers/{web_user_pk}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebUserDto | None:
    if response.status_code == 200:
        response_200 = WebUserDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebUserDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    web_user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[WebUserDto]:
    """Returns a single web user based on the webUserPk.

    Args:
        web_user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebUserDto]
    """

    kwargs = _get_kwargs(
        web_user_pk=web_user_pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    web_user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> WebUserDto | None:
    """Returns a single web user based on the webUserPk.

    Args:
        web_user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebUserDto
    """

    return sync_detailed(
        web_user_pk=web_user_pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    web_user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[WebUserDto]:
    """Returns a single web user based on the webUserPk.

    Args:
        web_user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebUserDto]
    """

    kwargs = _get_kwargs(
        web_user_pk=web_user_pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    web_user_pk: int,
    *,
    client: AuthenticatedClient | Client,
) -> WebUserDto | None:
    """Returns a single web user based on the webUserPk.

    Args:
        web_user_pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebUserDto
    """

    return (
        await asyncio_detailed(
            web_user_pk=web_user_pk,
            client=client,
        )
    ).parsed
