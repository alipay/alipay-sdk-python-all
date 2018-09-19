#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialGiftStockQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialGiftStockQueryResponse, self).__init__()
        self._available_count = None
        self._exist_list = None
        self._not_exist_list = None
        self._total_count = None

    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
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
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialGiftStockQueryResponse, self).parse_response_content(response_content)
        if 'available_count' in response:
            self.available_count = response['available_count']
        if 'exist_list' in response:
            self.exist_list = response['exist_list']
        if 'not_exist_list' in response:
            self.not_exist_list = response['not_exist_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
