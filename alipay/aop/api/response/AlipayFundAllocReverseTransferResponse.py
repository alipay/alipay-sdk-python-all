#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAllocReverseTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAllocReverseTransferResponse, self).__init__()
        self._amount = None
        self._order_id = None
        self._out_biz_no = None
        self._reverse_time = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reverse_time(self):
        return self._reverse_time

    @reverse_time.setter
    def reverse_time(self, value):
        self._reverse_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAllocReverseTransferResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'reverse_time' in response:
            self.reverse_time = response['reverse_time']
        if 'status' in response:
            self.status = response['status']
