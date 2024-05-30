# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from .._utils import maybe_transform, async_maybe_transform

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import report_asset_materialization_create_params

__all__ = ["ReportAssetMaterializationResource", "AsyncReportAssetMaterializationResource"]


class ReportAssetMaterializationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportAssetMaterializationResourceWithRawResponse:
        return ReportAssetMaterializationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportAssetMaterializationResourceWithStreamingResponse:
        return ReportAssetMaterializationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        asset_key: str,
        data_version: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        partition: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Report Asset Materialization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/report_asset_materialization",
            body=maybe_transform(
                {
                    "asset_key": asset_key,
                    "data_version": data_version,
                    "description": description,
                    "partition": partition,
                },
                report_asset_materialization_create_params.ReportAssetMaterializationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReportAssetMaterializationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportAssetMaterializationResourceWithRawResponse:
        return AsyncReportAssetMaterializationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportAssetMaterializationResourceWithStreamingResponse:
        return AsyncReportAssetMaterializationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        asset_key: str,
        data_version: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        partition: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Report Asset Materialization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/report_asset_materialization",
            body=await async_maybe_transform(
                {
                    "asset_key": asset_key,
                    "data_version": data_version,
                    "description": description,
                    "partition": partition,
                },
                report_asset_materialization_create_params.ReportAssetMaterializationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReportAssetMaterializationResourceWithRawResponse:
    def __init__(self, report_asset_materialization: ReportAssetMaterializationResource) -> None:
        self._report_asset_materialization = report_asset_materialization

        self.create = to_raw_response_wrapper(
            report_asset_materialization.create,
        )


class AsyncReportAssetMaterializationResourceWithRawResponse:
    def __init__(self, report_asset_materialization: AsyncReportAssetMaterializationResource) -> None:
        self._report_asset_materialization = report_asset_materialization

        self.create = async_to_raw_response_wrapper(
            report_asset_materialization.create,
        )


class ReportAssetMaterializationResourceWithStreamingResponse:
    def __init__(self, report_asset_materialization: ReportAssetMaterializationResource) -> None:
        self._report_asset_materialization = report_asset_materialization

        self.create = to_streamed_response_wrapper(
            report_asset_materialization.create,
        )


class AsyncReportAssetMaterializationResourceWithStreamingResponse:
    def __init__(self, report_asset_materialization: AsyncReportAssetMaterializationResource) -> None:
        self._report_asset_materialization = report_asset_materialization

        self.create = async_to_streamed_response_wrapper(
            report_asset_materialization.create,
        )
