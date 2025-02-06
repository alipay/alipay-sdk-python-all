#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrossBorderEcomShopDetail import CrossBorderEcomShopDetail


class ZhimaCreditEpCrossborderEcomshopdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCrossborderEcomshopdetailQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, CrossBorderEcomShopDetail):
            self._data = value
        else:
            self._data = CrossBorderEcomShopDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCrossborderEcomshopdetailQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
