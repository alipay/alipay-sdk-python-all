#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditFinanceRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditFinanceRefundResponse, self).__init__()
        self._amount = None
        self._biz_no = None
        self._currency = None
        self._gmt_refund_pay = None
        self._out_request_no = None
        self._status = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditFinanceRefundResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'currency' in response:
            self.currency = response['currency']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
