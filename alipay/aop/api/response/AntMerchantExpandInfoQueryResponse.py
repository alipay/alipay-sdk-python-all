#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantQueryResult import MerchantQueryResult


class AntMerchantExpandInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandInfoQueryResponse, self).__init__()
        self._merchant_query_result = None

    @property
    def merchant_query_result(self):
        return self._merchant_query_result

    @merchant_query_result.setter
    def merchant_query_result(self, value):
        if isinstance(value, MerchantQueryResult):
            self._merchant_query_result = value
        else:
            self._merchant_query_result = MerchantQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandInfoQueryResponse, self).parse_response_content(response_content)
        if 'merchant_query_result' in response:
            self.merchant_query_result = response['merchant_query_result']
