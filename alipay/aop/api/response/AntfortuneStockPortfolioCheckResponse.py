#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockPortfolioCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockPortfolioCheckResponse, self).__init__()
        self._in_list = None
        self._out_list = None

    @property
    def in_list(self):
        return self._in_list

    @in_list.setter
    def in_list(self, value):
        if isinstance(value, list):
            self._in_list = list()
            for i in value:
                self._in_list.append(i)
    @property
    def out_list(self):
        return self._out_list

    @out_list.setter
    def out_list(self, value):
        if isinstance(value, list):
            self._out_list = list()
            for i in value:
                self._out_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockPortfolioCheckResponse, self).parse_response_content(response_content)
        if 'in_list' in response:
            self.in_list = response['in_list']
        if 'out_list' in response:
            self.out_list = response['out_list']
