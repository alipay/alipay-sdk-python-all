#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeItemorderRefundResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeItemorderRefundResponse, self).__init__()
        self._order_no = None
        self._out_request_no = None
        self._real_refund_amount = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def real_refund_amount(self):
        return self._real_refund_amount

    @real_refund_amount.setter
    def real_refund_amount(self, value):
        self._real_refund_amount = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeItemorderRefundResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'real_refund_amount' in response:
            self.real_refund_amount = response['real_refund_amount']
