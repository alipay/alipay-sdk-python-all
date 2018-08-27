#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingOrderRefundResponse, self).__init__()
        self._order_no = None
        self._out_refund_no = None
        self._refund_fee = None
        self._refund_no = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_no(self):
        return self._refund_no

    @refund_no.setter
    def refund_no(self, value):
        self._refund_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingOrderRefundResponse, self).parse_response_content(response_content)
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'refund_no' in response:
            self.refund_no = response['refund_no']
