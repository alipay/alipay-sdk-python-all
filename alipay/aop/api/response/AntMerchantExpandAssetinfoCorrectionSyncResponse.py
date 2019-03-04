#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetinfoCorrectionSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetinfoCorrectionSyncResponse, self).__init__()
        self._correction_results = None

    @property
    def correction_results(self):
        return self._correction_results

    @correction_results.setter
    def correction_results(self, value):
        if isinstance(value, list):
            self._correction_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._correction_results.append(i)
                else:
                    self._correction_results.append(AssetResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetinfoCorrectionSyncResponse, self).parse_response_content(response_content)
        if 'correction_results' in response:
            self.correction_results = response['correction_results']
