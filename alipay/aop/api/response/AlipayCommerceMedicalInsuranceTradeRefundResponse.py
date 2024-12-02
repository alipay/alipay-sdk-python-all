#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceTradeRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceTradeRefundResponse, self).__init__()
        self._buyer_login_id = None
        self._buyer_user_id = None
        self._gmt_refund_pay = None
        self._open_id = None
        self._out_trade_no = None
        self._refund_fee = None
        self._trade_no = None

    @property
    def buyer_login_id(self):
        return self._buyer_login_id

    @buyer_login_id.setter
    def buyer_login_id(self, value):
        self._buyer_login_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceTradeRefundResponse, self).parse_response_content(response_content)
        if 'buyer_login_id' in response:
            self.buyer_login_id = response['buyer_login_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
