# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ReportAssetMaterializationCreateParams"]


class ReportAssetMaterializationCreateParams(TypedDict, total=False):
    asset_key: Required[str]

    data_version: str

    description: str

    partition: str
