#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalRegisterPaytradenoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRegisterPaytradenoQueryResponse, self).__init__()
        self._out_order_id = None
        self._pay_prop = None
        self._trade_no = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_prop(self):
        return self._pay_prop

    @pay_prop.setter
    def pay_prop(self, value):
        self._pay_prop = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRegisterPaytradenoQueryResponse, self).parse_response_content(response_content)
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'pay_prop' in response:
            self.pay_prop = response['pay_prop']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
