#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StockTask import StockTask


class AlipayCommerceTransportAdStocktaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdStocktaskQueryResponse, self).__init__()
        self._stock_task = None

    @property
    def stock_task(self):
        return self._stock_task

    @stock_task.setter
    def stock_task(self, value):
        if isinstance(value, StockTask):
            self._stock_task = value
        else:
            self._stock_task = StockTask.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdStocktaskQueryResponse, self).parse_response_content(response_content)
        if 'stock_task' in response:
            self.stock_task = response['stock_task']
