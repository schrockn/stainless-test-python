# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from dagster-plus-rest import DagsterPlusRest, AsyncDagsterPlusRest

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from dagster-plus-rest import DagsterPlusRest, AsyncDagsterPlusRest
from tests.utils import assert_matches_type
from dagster-plus-rest.types import report_asset_materialization_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestReportAssetMaterialization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: DagsterPlusRest) -> None:
        report_asset_materialization = client.report_asset_materialization.create(
            asset_key="string",
        )
        assert report_asset_materialization is None

    @parametrize
    def test_method_create_with_all_params(self, client: DagsterPlusRest) -> None:
        report_asset_materialization = client.report_asset_materialization.create(
            asset_key="string",
            data_version="string",
            description="string",
            partition="string",
        )
        assert report_asset_materialization is None

    @parametrize
    def test_raw_response_create(self, client: DagsterPlusRest) -> None:

        response = client.report_asset_materialization.with_raw_response.create(
            asset_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        report_asset_materialization = response.parse()
        assert report_asset_materialization is None

    @parametrize
    def test_streaming_response_create(self, client: DagsterPlusRest) -> None:
        with client.report_asset_materialization.with_streaming_response.create(
            asset_key="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            report_asset_materialization = response.parse()
            assert report_asset_materialization is None

        assert cast(Any, response.is_closed) is True
class TestAsyncReportAssetMaterialization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncDagsterPlusRest) -> None:
        report_asset_materialization = await async_client.report_asset_materialization.create(
            asset_key="string",
        )
        assert report_asset_materialization is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDagsterPlusRest) -> None:
        report_asset_materialization = await async_client.report_asset_materialization.create(
            asset_key="string",
            data_version="string",
            description="string",
            partition="string",
        )
        assert report_asset_materialization is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDagsterPlusRest) -> None:

        response = await async_client.report_asset_materialization.with_raw_response.create(
            asset_key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        report_asset_materialization = await response.parse()
        assert report_asset_materialization is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDagsterPlusRest) -> None:
        async with async_client.report_asset_materialization.with_streaming_response.create(
            asset_key="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            report_asset_materialization = await response.parse()
            assert report_asset_materialization is None

        assert cast(Any, response.is_closed) is True