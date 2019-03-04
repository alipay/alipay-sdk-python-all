#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransRefundResponse, self).__init__()
        self._order_id = None
        self._out_request_no = None
        self._refund_amount = None
        self._refund_date = None
        self._refund_order_id = None
        self._status = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
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
    def refund_date(self):
        return self._refund_date

    @refund_date.setter
    def refund_date(self, value):
        self._refund_date = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransRefundResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_date' in response:
            self.refund_date = response['refund_date']
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
        if 'status' in response:
            self.status = response['status']
