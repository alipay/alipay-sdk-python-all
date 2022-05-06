#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetBom import AssetBom


class AntMerchantExpandAssetBomQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetBomQueryResponse, self).__init__()
        self._asset_bom = None

    @property
    def asset_bom(self):
        return self._asset_bom

    @asset_bom.setter
    def asset_bom(self, value):
        if isinstance(value, AssetBom):
            self._asset_bom = value
        else:
            self._asset_bom = AssetBom.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetBomQueryResponse, self).parse_response_content(response_content)
        if 'asset_bom' in response:
            self.asset_bom = response['asset_bom']
