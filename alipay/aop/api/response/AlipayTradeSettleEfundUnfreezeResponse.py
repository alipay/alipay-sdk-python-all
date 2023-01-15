#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleEfundUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleEfundUnfreezeResponse, self).__init__()
        self._amount = None
        self._operation_time = None
        self._out_request_no = None
        self._settle_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSettleEfundUnfreezeResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'operation_time' in response:
            self.operation_time = response['operation_time']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
