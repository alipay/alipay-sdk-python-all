#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SnsTradeDataResult import SnsTradeDataResult


class AlipayMerchantOrderSnstradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderSnstradeQueryResponse, self).__init__()
        self._data_results = None

    @property
    def data_results(self):
        return self._data_results

    @data_results.setter
    def data_results(self, value):
        if isinstance(value, list):
            self._data_results = list()
            for i in value:
                if isinstance(i, SnsTradeDataResult):
                    self._data_results.append(i)
                else:
                    self._data_results.append(SnsTradeDataResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderSnstradeQueryResponse, self).parse_response_content(response_content)
        if 'data_results' in response:
            self.data_results = response['data_results']
