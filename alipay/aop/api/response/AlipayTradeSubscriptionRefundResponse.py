#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionRefundResponse, self).__init__()
        self._out_request_no = None
        self._refund_amount = None
        self._refund_order_id = None
        self._refund_status = None
        self._subscription_id = None
        self._trade_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionRefundResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
