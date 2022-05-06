#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetCallbackInfo import AssetCallbackInfo


class AntMerchantExpandAssetInteractSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetInteractSyncResponse, self).__init__()
        self._asset_callback_results = None

    @property
    def asset_callback_results(self):
        return self._asset_callback_results

    @asset_callback_results.setter
    def asset_callback_results(self, value):
        if isinstance(value, list):
            self._asset_callback_results = list()
            for i in value:
                if isinstance(i, AssetCallbackInfo):
                    self._asset_callback_results.append(i)
                else:
                    self._asset_callback_results.append(AssetCallbackInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetInteractSyncResponse, self).parse_response_content(response_content)
        if 'asset_callback_results' in response:
            self.asset_callback_results = response['asset_callback_results']
