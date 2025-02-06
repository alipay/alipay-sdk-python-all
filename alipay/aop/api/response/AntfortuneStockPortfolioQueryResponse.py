#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockPortfolioQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockPortfolioQueryResponse, self).__init__()
        self._symbol_list = None

    @property
    def symbol_list(self):
        return self._symbol_list

    @symbol_list.setter
    def symbol_list(self, value):
        if isinstance(value, list):
            self._symbol_list = list()
            for i in value:
                self._symbol_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockPortfolioQueryResponse, self).parse_response_content(response_content)
        if 'symbol_list' in response:
            self.symbol_list = response['symbol_list']
