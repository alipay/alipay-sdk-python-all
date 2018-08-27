#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetResult import AssetResult


class AntMerchantExpandAssetdeliveryAssignSyncResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAssetdeliveryAssignSyncResponse, self).__init__()
        self._delivery_results = None

    @property
    def delivery_results(self):
        return self._delivery_results

    @delivery_results.setter
    def delivery_results(self, value):
        if isinstance(value, list):
            self._delivery_results = list()
            for i in value:
                if isinstance(i, AssetResult):
                    self._delivery_results.append(i)
                else:
                    self._delivery_results.append(AssetResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAssetdeliveryAssignSyncResponse, self).parse_response_content(response_content)
        if 'delivery_results' in response:
            self.delivery_results = response['delivery_results']
