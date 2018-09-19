#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyDataQueryResponse, self).__init__()
        self._data = None
        self._data_time = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyDataQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'data_time' in response:
            self.data_time = response['data_time']
