#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetinfoSyncResponse, self).__init__()
        self._info_results = None

    @property
    def info_results(self):
        return self._info_results

    @info_results.setter
    def info_results(self, value):
        if isinstance(value, list):
            self._info_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._info_results.append(i)
                else:
                    self._info_results.append(AssetResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetinfoSyncResponse, self).parse_response_content(response_content)
        if 'info_results' in response:
            self.info_results = response['info_results']
