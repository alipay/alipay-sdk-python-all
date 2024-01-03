#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantOrderReverseSupplierApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantOrderReverseSupplierApplyResponse, self).__init__()
        self._asset_results = None

    @property
    def asset_results(self):
        return self._asset_results

    @asset_results.setter
    def asset_results(self, value):
        if isinstance(value, AssetResult):
            self._asset_results = value
        else:
            self._asset_results = AssetResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantOrderReverseSupplierApplyResponse, self).parse_response_content(response_content)
        if 'asset_results' in response:
            self.asset_results = response['asset_results']
