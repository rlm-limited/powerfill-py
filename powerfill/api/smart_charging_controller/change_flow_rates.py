import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    transaction_pk: int,
    *,
    min_rate_ampere: float | Unset = UNSET,
    max_rate_ampere: float,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["minRateAmpere"] = min_rate_ampere

    params["maxRateAmpere"] = max_rate_ampere

    json_valid_from: str | Unset = UNSET
    if not isinstance(valid_from, Unset):
        json_valid_from = valid_from.isoformat()
    params["validFrom"] = json_valid_from

    json_valid_to: str | Unset = UNSET
    if not isinstance(valid_to, Unset):
        json_valid_to = valid_to.isoformat()
    params["validTo"] = json_valid_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/smart-charging/{transaction_pk}/changeFlowRates",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
    min_rate_ampere: float | Unset = UNSET,
    max_rate_ampere: float,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> Response[Any]:
    """Controls and changes the flow rate of an ongoing/active transaction.
    <code>minRateAmpere</code> and <code>maxRateAmpere</code> define the boundaries of the flow rate.
    The optional <code>validFrom</code> and <code>validTo</code> can be used to set the time window in
    which the new flow rates should be applied.
    Various combinations of these parameters can be used to achieve many use cases.

    Args:
        transaction_pk (int):
        min_rate_ampere (float | Unset): Can be omitted in most cases, since the minimum flow is
            rarely an issue.
        max_rate_ampere (float): Can be set to 0 to effectively stop the electricity flow.
        valid_from (datetime.datetime | Unset): Defines the time from which the new flow rates
            should be applied.
            If not set, the new flow rates will be applied immediately.
             Example: 2000-10-10T01:30:00.000+01:00.
        valid_to (datetime.datetime | Unset): Defines the time until which the new flow rates
            should be applied.
            If not set, the new flow rates will be applied until the end of the transaction.
             Example: 2000-10-10T01:30:00.000+01:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
        min_rate_ampere=min_rate_ampere,
        max_rate_ampere=max_rate_ampere,
        valid_from=valid_from,
        valid_to=valid_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    transaction_pk: int,
    *,
    client: AuthenticatedClient | Client,
    min_rate_ampere: float | Unset = UNSET,
    max_rate_ampere: float,
    valid_from: datetime.datetime | Unset = UNSET,
    valid_to: datetime.datetime | Unset = UNSET,
) -> Response[Any]:
    """Controls and changes the flow rate of an ongoing/active transaction.
    <code>minRateAmpere</code> and <code>maxRateAmpere</code> define the boundaries of the flow rate.
    The optional <code>validFrom</code> and <code>validTo</code> can be used to set the time window in
    which the new flow rates should be applied.
    Various combinations of these parameters can be used to achieve many use cases.

    Args:
        transaction_pk (int):
        min_rate_ampere (float | Unset): Can be omitted in most cases, since the minimum flow is
            rarely an issue.
        max_rate_ampere (float): Can be set to 0 to effectively stop the electricity flow.
        valid_from (datetime.datetime | Unset): Defines the time from which the new flow rates
            should be applied.
            If not set, the new flow rates will be applied immediately.
             Example: 2000-10-10T01:30:00.000+01:00.
        valid_to (datetime.datetime | Unset): Defines the time until which the new flow rates
            should be applied.
            If not set, the new flow rates will be applied until the end of the transaction.
             Example: 2000-10-10T01:30:00.000+01:00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        transaction_pk=transaction_pk,
        min_rate_ampere=min_rate_ampere,
        max_rate_ampere=max_rate_ampere,
        valid_from=valid_from,
        valid_to=valid_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
