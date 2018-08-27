#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetproduceAssignSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetproduceAssignSyncResponse, self).__init__()
        self._asset_results = None

    @property
    def asset_results(self):
        return self._asset_results

    @asset_results.setter
    def asset_results(self, value):
        if isinstance(value, list):
            self._asset_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._asset_results.append(i)
                else:
                    self._asset_results.append(AssetResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetproduceAssignSyncResponse, self).parse_response_content(response_content)
        if 'asset_results' in response:
            self.asset_results = response['asset_results']
