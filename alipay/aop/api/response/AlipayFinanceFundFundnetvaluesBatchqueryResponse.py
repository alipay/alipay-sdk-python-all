#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NetValueVO import NetValueVO


class AlipayFinanceFundFundnetvaluesBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundFundnetvaluesBatchqueryResponse, self).__init__()
        self._fund_code = None
        self._fund_type = None
        self._net_values = None

    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def net_values(self):
        return self._net_values

    @net_values.setter
    def net_values(self, value):
        if isinstance(value, list):
            self._net_values = list()
            for i in value:
                if isinstance(i, NetValueVO):
                    self._net_values.append(i)
                else:
                    self._net_values.append(NetValueVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundFundnetvaluesBatchqueryResponse, self).parse_response_content(response_content)
        if 'fund_code' in response:
            self.fund_code = response['fund_code']
        if 'fund_type' in response:
            self.fund_type = response['fund_type']
        if 'net_values' in response:
            self.net_values = response['net_values']
