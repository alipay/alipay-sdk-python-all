#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandCancelResultSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandCancelResultSyncResponse, self).__init__()
        self._asset_result = None

    @property
    def asset_result(self):
        return self._asset_result

    @asset_result.setter
    def asset_result(self, value):
        if isinstance(value, AssetResult):
            self._asset_result = value
        else:
            self._asset_result = AssetResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandCancelResultSyncResponse, self).parse_response_content(response_content)
        if 'asset_result' in response:
            self.asset_result = response['asset_result']
