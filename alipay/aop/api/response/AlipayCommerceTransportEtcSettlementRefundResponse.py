#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcSettlementRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcSettlementRefundResponse, self).__init__()
        self._out_order_id = None
        self._out_request_no = None
        self._pay_time = None
        self._refund_amount = None
        self._refund_status = None
        self._refund_time = None
        self._trade_no = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcSettlementRefundResponse, self).parse_response_content(response_content)
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
