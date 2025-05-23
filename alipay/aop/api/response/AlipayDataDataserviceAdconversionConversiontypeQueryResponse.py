#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AssetDetail import AssetDetail


class AlipayDataDataserviceAdconversionConversiontypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdconversionConversiontypeQueryResponse, self).__init__()
        self._asset_detail_list = None

    @property
    def asset_detail_list(self):
        return self._asset_detail_list

    @asset_detail_list.setter
    def asset_detail_list(self, value):
        if isinstance(value, list):
            self._asset_detail_list = list()
            for i in value:
                if isinstance(i, AssetDetail):
                    self._asset_detail_list.append(i)
                else:
                    self._asset_detail_list.append(AssetDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdconversionConversiontypeQueryResponse, self).parse_response_content(response_content)
        if 'asset_detail_list' in response:
            self.asset_detail_list = response['asset_detail_list']
