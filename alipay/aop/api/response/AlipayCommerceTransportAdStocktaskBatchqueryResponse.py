#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StockTask import StockTask


class AlipayCommerceTransportAdStocktaskBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdStocktaskBatchqueryResponse, self).__init__()
        self._stock_task = None

    @property
    def stock_task(self):
        return self._stock_task

    @stock_task.setter
    def stock_task(self, value):
        if isinstance(value, list):
            self._stock_task = list()
            for i in value:
                if isinstance(i, StockTask):
                    self._stock_task.append(i)
                else:
                    self._stock_task.append(StockTask.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdStocktaskBatchqueryResponse, self).parse_response_content(response_content)
        if 'stock_task' in response:
            self.stock_task = response['stock_task']
