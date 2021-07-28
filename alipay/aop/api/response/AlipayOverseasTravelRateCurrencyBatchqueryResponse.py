#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RateCurrency import RateCurrency


class AlipayOverseasTravelRateCurrencyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelRateCurrencyBatchqueryResponse, self).__init__()
        self._currency_list = None

    @property
    def currency_list(self):
        return self._currency_list

    @currency_list.setter
    def currency_list(self, value):
        if isinstance(value, list):
            self._currency_list = list()
            for i in value:
                if isinstance(i, RateCurrency):
                    self._currency_list.append(i)
                else:
                    self._currency_list.append(RateCurrency.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelRateCurrencyBatchqueryResponse, self).parse_response_content(response_content)
        if 'currency_list' in response:
            self.currency_list = response['currency_list']
