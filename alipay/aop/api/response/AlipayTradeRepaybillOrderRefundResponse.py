#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillOrderRefundResponse, self).__init__()
        self._bill_no = None
        self._gmt_refund_pay = None
        self._out_request_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillOrderRefundResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
