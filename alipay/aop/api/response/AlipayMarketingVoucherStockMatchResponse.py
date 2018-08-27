#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherStockMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherStockMatchResponse, self).__init__()
        self._exist_list = None
        self._not_exist_list = None

    @property
    def exist_list(self):
        return self._exist_list

    @exist_list.setter
    def exist_list(self, value):
        if isinstance(value, list):
            self._exist_list = list()
            for i in value:
                self._exist_list.append(i)
    @property
    def not_exist_list(self):
        return self._not_exist_list

    @not_exist_list.setter
    def not_exist_list(self, value):
        if isinstance(value, list):
            self._not_exist_list = list()
            for i in value:
                self._not_exist_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherStockMatchResponse, self).parse_response_content(response_content)
        if 'exist_list' in response:
            self.exist_list = response['exist_list']
        if 'not_exist_list' in response:
            self.not_exist_list = response['not_exist_list']
