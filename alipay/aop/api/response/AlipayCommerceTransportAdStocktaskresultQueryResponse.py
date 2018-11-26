#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StockTaskResult import StockTaskResult


class AlipayCommerceTransportAdStocktaskresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdStocktaskresultQueryResponse, self).__init__()
        self._stock_task_result = None

    @property
    def stock_task_result(self):
        return self._stock_task_result

    @stock_task_result.setter
    def stock_task_result(self, value):
        if isinstance(value, StockTaskResult):
            self._stock_task_result = value
        else:
            self._stock_task_result = StockTaskResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdStocktaskresultQueryResponse, self).parse_response_content(response_content)
        if 'stock_task_result' in response:
            self.stock_task_result = response['stock_task_result']
